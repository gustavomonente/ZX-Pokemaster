from classes.zxdb_scraper import *
from classes.database import *
import unittest

zxdb = ZXDBScraper()
db = Database()

class TestZXDBScraper(unittest.TestCase):

    def test_cheesy_chase(self):
        where_clause = 'AND entries.id=35141'
        games = zxdb.getGames(where_clause)
        for game in games:
            for release in game.releases:
                release.getInfoFromLocalFiles()
            db.addGame(game)
        db.commit()
        game = db.getGameByWosID(35141)
        self.assertNotEqual('', game.name)


    def test_crime_busters(self):
        where_clause = 'AND entries.id=1155'
        games = zxdb.getGames(where_clause)
        for game in games:
            for release in game.releases:
                release.getInfoFromLocalFiles()
            db.addGame(game)
        db.commit()
        game = db.getGameByWosID(1155)
        self.assertEqual(2, len(game.releases[0].aliases))
        self.assertTrue('Crime Busters' in game.releases[0].aliases)
        for file in game.getFiles():
            if file.md5=='c358b7b95459f583c9e2bc11d9830d68':
                self.assertGreater(len(file.wos_path),0)
                self.assertGreater(len(file.wos_name), 0)


    def test_multirelease_game(self):
        where_clause = 'AND entries.id=4'
        games = zxdb.getGames(where_clause)
        game = games[0]
        for release in game.releases:
            release.getInfoFromLocalFiles()
        self.assertEqual(4, len(game.releases))
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(4)
        self.assertEqual(4, len(game.releases))
        print(game.releases)

    def test_square_brackets_elimination(self):
        where_clause = 'AND entries.id = 26303'
        games = zxdb.getGames(where_clause)
        for game in games:
            for release in game.releases:
                release.getInfoFromLocalFiles()
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(26303)
        release = game.releases[0]
        self.assertEqual("Load 'n' Run", release.publisher)
        self.assertIn('Tombola', release.aliases)
        self.assertNotIn('Tombola [2]', release.aliases)

    def test_crc32_and_sha1_hashes(self):
        where_clause = 'AND entries.id = 10'
        games= zxdb.getGames(where_clause)
        for release in games[0].releases:
            release.getInfoFromLocalFiles()
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(10)
        for file in game.getFiles():
            self.assertGreater(len(file.crc32), 0)
            self.assertGreater(len(file.sha1), 0)

    def test_games_with_format_mismatch(self):
        where_clause = 'AND entries.id = 26541'
        games= zxdb.getGames(where_clause)
        for release in games[0].releases:
            release.getInfoFromLocalFiles()
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(26541)
        for file in game.getFiles():
            if file.md5 == '4c279cc851f59bcffffd6a34c7236b75':
                self.assertEqual('z80', file.format)

    # multiplayer_type column is obsolete in ZXDB
    # def test_multiplayer_type(self):
    #     where_clause = 'AND entries.id = 30265'
    #     games = zxdb.getGames(where_clause)
    #     for release in games[0].releases:
    #         release.getInfoFromLocalFiles()
    #     db.addGame(games[0])
    #     db.commit()
    #     game = db.getGameByWosID(30265)
    #     self.assertEqual('Vs', game.getMultiplayerType())

    def test_side(self):
        where_clause = 'AND entries.id = 5856'
        games = zxdb.getGames(where_clause)
        for release in games[0].releases:
            release.getInfoFromLocalFiles()
        wos_names = [file.wos_name for file in games[0].getFiles()]
        self.assertIn('Zip-Zap - Alternate - Side 1.tzx', wos_names)
        self.assertIn('Zip-Zap - Alternate - Side 2.tzx', wos_names)
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(5856)
        wos_names = [file.wos_name for file in game.getFiles()]
        self.assertIn('Zip-Zap - Alternate - Side 1.tzx', wos_names)
        self.assertIn('Zip-Zap - Alternate - Side 2.tzx', wos_names)

    def test_home_computer_club_the(self):
        where_clause = 'AND entries.id = 22695'
        games = zxdb.getGames(where_clause)
        self.assertEqual(games[0].getPublisher(), 'Home Computer Club, The')
        for release in games[0].releases:
            self.assertEqual(release.getPublisher(), 'Home Computer Club, The')

    def test_3d_games(self):
        where_clause = 'AND entries.id = 25677'
        games = zxdb.getGames(where_clause)
        aliases = games[0].releases[0].getAllAliases()
        self.assertEqual(aliases, ['3D Plotter', 'Technical Drawing'])
        where_clause = 'AND entries.id = 5140'
        games = zxdb.getGames(where_clause)
        aliases = games[0].releases[2].getAllAliases()
        self.assertEqual(aliases, ['3D Tanks', '3D-Tanx'])

    def test_multitape_game(self):
        where_clause = 'AND entries.id = 11433'
        games = zxdb.getGames(where_clause)
        release = games[0].releases[0]
        release.getInfoFromLocalFiles()
        for file in release.files:
            self.assertGreater(file.part, 0)

    def test_sanitizing_alias(self):
        alias = 'Jet Set Willy (again)'
        new_alias = zxdb.sanitizeAlias(alias)
        game = Game(new_alias)
        self.assertEqual(game.name, 'Jet Set Willy - again')

    def test_alt_content_desc(self):
        where_clause = 'AND entries.id IN (30155, 11170)'
        games = zxdb.getGames(where_clause)
        for game in games:
            for release in game.releases:
                release.getInfoFromLocalFiles()
            game.setContentDescForZXDBFiles(zxdb.manually_corrected_content_descriptions)
            for file in game.getFiles():
                if game.zxdb_id==30155:
                    self.assertGreater(len(file.content_desc), 0)
                else:
                    self.assertEqual(len(file.content_desc), 0)

    def test_file_release_date(self):
        where_clause = 'AND entries.id = 20176'
        games = zxdb.getGames(where_clause)
        for game in games:
            for release in game.releases:
                release.getInfoFromLocalFiles()
        game.setContentDescForZXDBFiles(zxdb.manually_corrected_content_descriptions)
        # for file in game.getFiles():
        #     self.assertEqual(file.release_date, '')
        db.addGame(game)
        db.commit()
        game = db.getGameByWosID(20176)
        for file in game.getFiles():
            if file.getMD5() == 'aeac4c85b51cc34dad9275abdfd09837':
                self.assertEqual(file.content_desc, ' V4.7')
                self.assertEqual('2017-03-06', file.release_date)
            # else:
            #     self.assertEqual(file.content_desc, '')
            #     self.assertEqual(file.release_date, '')

    def test_authors_as_publishers(self):
        where_clause = 'AND entries.id IN (30155, 21575, 7727)'
        games = zxdb.getGames(where_clause)
        for game in games:
            if game.zxdb_id == 30155:
                self.assertEqual('Grussu, Alessandro', game.getPublisher())
            elif game.zxdb_id == 21575:
                self.assertEqual('Owen, Andrew S.', game.getPublisher())
            elif game.zxdb_id == 7727:
                self.assertEqual('Mad Max', game.getPublisher())

    def test_authors_teams(self):
        where_clause = 'AND entries.id IN (5448)'
        games = zxdb.getGames(where_clause)
        for game in games:
            self.assertEqual('Orpheus', game.getAuthor())

    def test_downloading(self):
        where_clause = 'AND entries.id IN (24888)'
        games = zxdb.getGames(where_clause)
        zxdb.downloadMissingFilesForGames(games)

    def test_alt_publisher(self):
        where_clause = 'AND entries.id IN (24406)'
        games = zxdb.getGames(where_clause)
        zxdb.getInfoFromLocalFiles(games)
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(24406)
        self.assertEqual('Baldomero, Garcia', game.publisher)
        self.assertEqual('Baldomero, Garcia', game.author)
        self.assertEqual('Baldomero, Garcia', game.releases[0].publisher)

    def test_original_publisher(self):
        where_clause = 'AND entries.id IN (128)'
        games = zxdb.getGames(where_clause)
        zxdb.getInfoFromLocalFiles(games)
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(128)
        self.assertEqual('Hit-Pak', game.publisher)

    def test_santa_clause(self):
        where_clause = 'AND entries.id IN (12789)'
        games = zxdb.getGames(where_clause)
        zxdb.getInfoFromLocalFiles(games)
        self.assertEqual('Crime Santa Claus', games[0].name)
        self.assertEqual(['Crime Santa Claus'], games[0].releases[0].aliases)
        db.addGame(games[0])
        db.commit()

    def test_un_dos_tres(self):
        where_clause = 'AND entries.id IN (5512)'
        games = zxdb.getGames(where_clause)
        self.assertEqual(['3-2-1', 'Un, Dos, Tres Responda Otra Vez'], games[0].releases[1].getAllAliases())

    def test_semanal(self):
        where_clause = 'AND entries.id IN (13615)'
        games = zxdb.getGames(where_clause)
        game_file = games[0].getFiles()[0]
        self.assertFalse('aka' in game_file.notes)

    def test_multipublisher(self):
        where_clause = 'AND entries.id in (10959)'
        games = zxdb.getGames(where_clause)
        publisher = games[0].publisher
        self.assertEqual('Davie, C. - Yacomine, Gordon', publisher)


    def test_multiauthor(self):
        where_clause = 'AND entries.id in (19089)'
        games = zxdb.getGames(where_clause)
        author = games[0].author
        self.assertEqual('Myslivec, Jaroslav - Zyxoft', author)
        where_clause = 'AND entries.id in (9332)'
        games = zxdb.getGames(where_clause)
        author = games[0].author
        self.assertEqual('Eldridge, Jon Paul - Fletcher, Nigel - Oliver Twins, The', author)
        where_clause = 'AND entries.id in (4559)'
        games = zxdb.getGames(where_clause)
        author = games[0].author
        # self.assertEqual('Lewis, John - Martin, Ian - Orpheus - Redmond, Damon', author)
        self.assertEqual('Lewis, John - Orpheus', author)

    def test_pozycje_milosne(self):
        where_clause = 'AND entries.id in (3861)'
        games = zxdb.getGames(where_clause)
        self.assertGreater(len(games), 0)
        self.assertEqual(3861, games[0].zxdb_id)

    def test_lost_in_my_spectrum(self):
        where_clause = 'AND entries.id in (27974)'
        games = zxdb.getGames(where_clause)
        game = games[0]
        for file in game.getFiles():
            # print(file.wos_name, file.wos_path)
            # print(file.getTOSECName(), file.language)
            if 'DE' in file.wos_path:
                self.assertTrue('(IT)(de)' in file.getTOSECName())

