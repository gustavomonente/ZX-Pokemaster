from classes.database import *
from functions.game_name_functions import *
from settings import *
import os
import stat
import shutil
import zipfile
import hashlib
import json
import time

class Sorter():

    db = Database()
    gui = None
    input_files = []
    collected_files = []
    should_cancel = False
    original_output_location = None
    too_long_path = None

    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = self.loadSettings()
        self.input_locations = kwargs.get('input_locations', [])
        self.traverse_subfolders= kwargs.get('traverse_subfolders', True)
        self.output_location = kwargs.get('output_location', 'sorted')
        self.formats_preference = kwargs.get('formats_preference', [])
        if not self.formats_preference:
            self.formats_preference = GAME_EXTENSIONS
        self.languages = kwargs.get('languages', [])
        self.max_files_per_folder = kwargs.get('max_files_per_folder', None)
        self.output_folder_structure = kwargs.get('output_folder_structure', '')
        self.output_filename_structure = kwargs.get('output_filename_structure', TOSEC_COMPLIANT_FILENAME_STRUCTURE)
        self.delete_original_files = kwargs.get('delete_original_files', False)
        self.ignore_alternate = kwargs.get('ignore_alternate', True)
        self.ignore_alternate_formats = kwargs.get('ignore_alternate_formats', False)
        self.ignore_rereleases = kwargs.get('ignore_rereleases', False)
        self.ignore_hacks = kwargs.get('ignore_hacks', False)
        self.ignore_xrated = kwargs.get('ignore_xrated', False)
        self.ignore_bad_dumps = kwargs.get('ignore_bad_dumps', True)
        # self.ignore_unknown = kwargs.get('ignore_unknown', False)
        self.short_filenames = kwargs.get('short_filenames', False)
        self.use_camel_case = kwargs.get('use_camel_case', False)
        self.place_pok_files_in_pokes_subfolders = kwargs.get('place_pok_files_in_pokes_subfolders', True)
        self.gui = kwargs.get('gui', None)
        if kwargs.get('cache', True):
            if self.gui:
                self.gui.updateProgressBar(0, 0, 'Loading database cache...')
            self.db.loadCache()
        if self.output_location in self.input_locations:
            self.original_output_location = self.output_location
            self.output_location = os.path.join(os.path.dirname(self.output_location), '%s_temp' % self.output_location)

    def loadSettings(self):
        if not os.path.exists('settings.json'):
            return {}
        with open('settings.json', 'r', encoding='utf-8') as f:
            settings = json.load(f)
        return settings

    def sortFiles(self):
        if not self.input_files:
            self.input_files = self.getInputFiles()
        print('Got', len(self.input_files), 'raw input files')
        self.collected_files = self.collectFiles(self.input_files)
        print('Files collected')
        if self.too_long_path:
            print('Path', self.too_long_path, 'is too long. Exiting prematurely.')
            return
        if self.ignore_hacks or \
            self.ignore_alternate or \
            self.ignore_rereleases or \
            self.languages:
            self.collected_files = self.filterCollectedFiles()
            print('Files filtered')
        if self.max_files_per_folder:
            self.collected_files = self.bundleFilesInEqualFolders()
        print('Redistributing...')
        self.redistributeFiles()

        if self.original_output_location:
            backup_location_name = self.original_output_location+'_old'
            if os.path.exists(backup_location_name):
                i = 2
                while os.path.exists(backup_location_name+'_'+str(i)):
                    i += 1
                backup_location_name = backup_location_name + '_' + str(i)
            os.rename(self.original_output_location, backup_location_name)
            os.rename(self.output_location, self.original_output_location)

    def collectFiles(self, input_files):
        if self.gui:
            self.gui.updateProgressBar(0, len(input_files), 'Examining files...')
        collected_files = {}
        tosec_compliant = self.output_filename_structure==TOSEC_COMPLIANT_FILENAME_STRUCTURE
        for i, file_path in enumerate(input_files):
            if self.should_cancel:
                break
            if i % 100 == 0:
                print('Examined', i, 'files of', len(input_files))
                if self.gui:
                    self.gui.updateProgressBar(i)
            game_files = self.getGameFilesFromInputPath(file_path)
            if not self.short_filenames:
                for game_file in game_files:
                    self.shortenGameFileDestination(game_file)
            if self.too_long_path:
                print('Path', self.too_long_path, 'is too long. Exiting prematurely.')
                break
            if not game_files:
                print('Nothing found for', file_path)
                continue
            for game_file in game_files:
                wos_id = game_file.game.wos_id
                if wos_id not in collected_files.keys():
                    collected_files[game_file.game.wos_id] = []
                else:
                    if game_file in collected_files[game_file.game.wos_id]:
                        continue
                    copies_count = game_file.countAlternateDumpsIn(collected_files[wos_id])
                    if not tosec_compliant:
                        copies_count = game_file.countFilesWithSameDestIn(collected_files[wos_id])
                    game_file.addAlternateModFlag(copies_count,
                                                  tosec_compliant=tosec_compliant,
                                                  short_filenames=self.short_filenames)
                collected_files[game_file.game.wos_id].append(game_file)
        return collected_files

    def shortenGameFileDestination(self, game_file):
        abs_dest = game_file.getAbsoluteDestPath()
        if len(abs_dest) > MAX_DESTINATION_PATH_LENGTH:
            for game_name_length in range(MAX_GAME_NAME_LENGTH, MIN_GAME_NAME_LENGTH, -10):
                game_file.dest = self.getDestination(game_file,
                                                     game_name_length=game_name_length)
                abs_dest = game_file.getAbsoluteDestPath()
                if len(abs_dest) <= MAX_DESTINATION_PATH_LENGTH:
                    break
        if len(abs_dest) > MAX_DESTINATION_PATH_LENGTH:
            self.too_long_path = abs_dest

    def getCamelCasePath(self, path):
        path = ''.join([x[0].upper() + x[1:] for x in path.split(' ') if x])
        path = path.replace(',', '')
        return path

    def getInputFiles(self, input_locations=None):
        if not input_locations:
            input_locations = self.input_locations
        input_files = []
        formats = ['zip']+GAME_EXTENSIONS
        for location in input_locations:
            if self.should_cancel:
                break
            if self.gui:
                self.gui.updateProgressBar(0, 0, 'Traversing '+location)
            for root, dirs, files in os.walk(location):
                for file in files:
                    if file[-3:].lower() in formats:
                        input_files.append(os.path.join(root, file))
                if not self.traverse_subfolders:
                    break
        return input_files

    def getGameFilesFromInputPath(self, file_path):
        game_files = []
        ext = os.path.splitext(file_path)[1][1:].lower()
        if ext in self.formats_preference:
            game_file = GameFile(file_path)
            game = self.db.getGameByFile(game_file)
            if game:
                game_file.importCredentialsFromGame(game, overwrite = True)
            game_file.src = file_path
            game_file.dest = self.getDestination(game_file)
            game_files.append(game_file)
        elif ext=='zip':
            if os.path.getsize(file_path)>MAX_ZIP_FILE_SIZE:
                return []
            with zipfile.ZipFile(file_path) as zf:
                for zfname in zf.namelist():
                    zfext = os.path.splitext(zfname)[1][1:].lower()
                    if zfext not in self.formats_preference:
                        continue
                    game_file = GameFile(file_path)
                    game_file.format = zfext
                    game_file.crc32 = hex(zf.getinfo(zfname).CRC)[2:]
                    unzipped_file = zf.read(zfname)
                    unzipped_file_md5 = hashlib.md5(unzipped_file).hexdigest()
                    game_file.md5 = unzipped_file_md5
                    game = self.db.getGameByFileMD5(unzipped_file_md5)
                    if game:
                        game_file = game.findFileByMD5(unzipped_file_md5)
                        game_file.release = game.releases[game_file.release_seq]
                        game_file.tosec_path = None
                    game_file.src = file_path
                    game_file.dest = self.getDestination(game_file)
                    game_file.alt_dest = ''
                    game_files.append(game_file)
        return game_files

    def getDestination(self, game_file, game_name_length=MAX_GAME_NAME_LENGTH):
        #Publisher name will be cropped to 3 words if dest length is too long
        subfolders_dict = game_file.getOutputPathFormatKwargs(
            game_name_length=game_name_length)
        dest_dir = self.output_folder_structure.format(**subfolders_dict)
        dest_filename = game_file.getOutputName(structure=self.output_filename_structure,
                                                game_name_length=game_name_length)
        if self.short_filenames:
            dest_filename = os.path.splitext(dest_filename)
            print(dest_filename)
            dest_filename = ''.join((get_meaningful_8letter_name(game_file.getGameName()), '.', game_file.format.upper()))
            dest_dir = dest_dir.split(os.sep)
            print(dest_dir)
            dest_dir = [get_meaningful_8letter_name(x) for x in dest_dir]
            dest_dir = os.path.join(*dest_dir)
        dest = os.path.join(dest_dir, dest_filename)
        dest = os.sep.join([x for x in dest.split(os.sep) if x])
        if self.use_camel_case:
            dest = self.getCamelCasePath(dest)
        dest = os.path.join(self.output_location, dest)
        return dest

    def filterCollectedFiles(self):
        for game_wos_id, files in self.collected_files.items():
            min_release = min([file.getReleaseSeq() for file in files])
            for i, file in enumerate(files):
                if self.ignore_rereleases and file.getReleaseSeq()>min_release:
                    self.collected_files[game_wos_id][i] = None
                if self.ignore_alternate and file.isAlternate():
                    self.collected_files[game_wos_id][i] = None
                if self.ignore_hacks and file.isHack():
                    self.collected_files[game_wos_id][i] = None
                if self.ignore_bad_dumps and file.isBadDump():
                    self.collected_files[game_wos_id][i] = None
                if self.ignore_xrated and file.isXRated():
                    self.collected_files[game_wos_id][i] = None
                if self.languages and file.getLanguage() not in self.languages:
                    self.collected_files[game_wos_id][i] = None
            files = [file for file in files if file]
            if self.ignore_alternate_formats and files and game_wos_id:
                self.collected_files[game_wos_id] = self.filterOutAlternateFormats(files)
        return self.collected_files

    def bundleFilesInEqualFolders(self):
        folders = {}
        for game_wos_id, files in self.collected_files.items():
            for i, file in enumerate(files):
                if not file:
                    continue
                file_dest_dir = os.path.dirname(file.getDestPath())
                if not folders.get(file_dest_dir):
                    folders[file_dest_dir]=[]
                folders[file_dest_dir].append(file)

        bundles = {}
        mini_bundles = {}
        for folder_name, files in folders.items():
            if len(files)<=self.max_files_per_folder:
                continue
            bundles = {}
            mini_bundles = {}
            for file in files:
                mini_bundle_name = file.getBundleName()
                if not mini_bundles.get(mini_bundle_name):
                    mini_bundles[mini_bundle_name] = []
                mini_bundles[mini_bundle_name].append(file)

            current_bundle = []
            mini_bundles = [{
                'name':key,
                'files':value
            } for key, value in mini_bundles.items()]
            mini_bundles = sorted(mini_bundles, key=lambda x: x['name'])
            while True:
                if mini_bundles:
                    current_bundle.append(mini_bundles.pop(0)['files'])
                files_in_current_bundle = sum([len(bundle) for bundle in current_bundle])
                if not mini_bundles or \
                    len(mini_bundles[0]['files'])+files_in_current_bundle>=self.max_files_per_folder:
                    if current_bundle:
                        current_bundle_name = '{}-{}'.format(current_bundle[0][0].getBundleName(),
                                                             current_bundle[-1][-1].getBundleName())
                        bundles[current_bundle_name] = [file for file in current_bundle]
                    current_bundle = []
                if not mini_bundles:
                    break

            for bundle_name, mini_bundles in bundles.items():
                for mini_bundle in mini_bundles:
                    for file in mini_bundle:
                        file.setBundle(bundle_name)
        return self.collected_files

    def filterOutAlternateFormats(self, files):
        equals_found_flag = True
        while equals_found_flag == True:
            equals_found_flag = False
            best_candidate = None
            equals = []
            for file in files:
                equals = file.getEquals(files)
                if len(equals)==1:
                    continue
                elif equals==0:
                    print(files)
                    raise Exception('Equals not found!')
                else:
                    equals_found_flag = True
                    best_candidate = self.getBestCandidate(equals)
                    break
            if best_candidate:
                for file in equals:
                    if file in files and file!=best_candidate:
                        files.remove(file)
        return files

    def getBestCandidate(self, files):
        files = sorted(files, key=lambda file: file.getSortIndex(self.formats_preference))
        return files[0]

    def redistributeFiles(self):
        if self.gui:
            self.gui.updateProgressBar(0, self.getCollectedFilesCount(), 'Redistributing files...')
        files_array = self.getFilesArray(self.collected_files)
        for i, file in enumerate(files_array):
            if self.should_cancel:
                break
            if i % 100 == 0:
                print('Redistributed files:', i-1, 'of', len(files_array))
                if self.gui:
                    self.gui.updateProgressBar(i)
            dest = file.getDestPath()
            try:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
            except OSError:
                print('Could not make dirs:', dest, 'for', file.src)
                print(traceback.format_exc())
                continue
            if file.src.lower().endswith('zip'):
                self.unpackFile(file)
            else:
                try:
                    if self.delete_original_files:
                        shutil.move(file.src, dest)
                    else:
                        shutil.copy(file.src, dest)
                except PermissionError:
                    os.chmod(file.dest, stat.S_IWRITE)
                    if self.delete_original_files:
                        shutil.move(file.src, dest)
                    else:
                        shutil.copy(file.src, dest)

            if file.game.cheats:
                pok_dir_path = os.path.dirname(dest)
                pok_file_name = os.path.splitext(os.path.basename(dest))[0]+'.pok'
                if self.place_pok_files_in_pokes_subfolders:
                    pok_dir_path = os.path.join(pok_dir_path, 'POKES')
                    os.makedirs(pok_dir_path, exist_ok=True)
                pok_file_path = os.path.join(pok_dir_path, pok_file_name)
                file.game.exportPokFile(pok_file_path)

    def getFilesArray(self, collected_files):
        files_array = []
        for files in collected_files.values():
            for file in files:
                if not file:
                    continue
                else:
                    files_array.append(file)
        return files_array

    def getInputFilesCount(self):
        return len(self.input_files)

    def getCollectedFilesCount(self):
        return sum([len(x) for x in self.collected_files.values()])

    def unpackFile(self, game_file):
        with zipfile.ZipFile(game_file.src) as zf:
            for zfname in zf.namelist():
                crc32 = hex(zf.getinfo(zfname).CRC)[2:].zfill(8)
                if crc32 == game_file.crc32.zfill(8):
                    data = zf.read(zfname)
                    dest = game_file.getDestPath()
                    try:
                        with open(dest, 'wb') as output:
                            output.write(data)
                    except PermissionError:
                        os.chmod(dest, stat.S_IWRITE)
                        with open(dest, 'wb') as output:
                            output.write(data)
                    break

    def cancel(self):
        self.should_cancel = True