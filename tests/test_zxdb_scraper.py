from classes.zxdb_scraper import *
from classes.database import *
import unittest

zxdb = ZXDBScraper()
db = Database()

class TestZXDBScraper(unittest.TestCase):

    def test_crime_busters(self):
        where_clause = 'AND entries.id=1155'
        games = zxdb.getGames(where_clause)
        for game in games:
            db.addGame(game)
        db.commit()
        game = db.getGameByWosID(1155)
        self.assertTrue(len(game.releases[0].aliases), 2)
        self.assertTrue('Crime Busters' in game.releases[0].aliases)

    def test_multirelease_game(self):
        where_clause = 'AND entries.id=4'
        games = zxdb.getGames(where_clause)
        game = games[0]
        self.assertEqual(len(game.releases), 4)
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(4)
        self.assertEqual(len(game.releases), 4)
        print(game.releases)

    def test_square_brackets_elimination(self):
        where_clause = 'AND entries.id = 26303'
        games = zxdb.getGames(where_clause)
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(26303)
        release = game.releases[0]
        self.assertEqual(release.publisher, "Load 'n' Run")
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
                self.assertEqual(file.format, 'z80')

    def test_multiplayer_type(self):
        where_clause = 'AND entries.id = 30265'
        games = zxdb.getGames(where_clause)
        for release in games[0].releases:
            release.getInfoFromLocalFiles()
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(30265)
        self.assertEqual(game.getMultiplayerType(), 'Vs')

    def test_cousin_horace(self):
        where_clause = 'AND entries.id = 30155'
        games = zxdb.getGames(where_clause)
        s = Scraper()
        for game in games:
            for file in game.getFiles():
                local_path = file.getLocalPath()
                if os.path.exists(local_path) and \
                        os.path.getsize(local_path):
                    continue
                elif os.path.exists(local_path) and \
                                os.path.getsize(local_path) != file.size:
                    print('wrong file size:', local_path)
                else:
                    for mirror in WOS_MIRRORS:
                        try:
                            status = s.downloadFile(file.getWosPath(wos_mirror_root=mirror), local_path)
                        except:
                            print(traceback.format_exc())
                        if status == 200:
                            break
        for release in games[0].releases:
            release.getInfoFromLocalFiles()
        # db.addGame(games[0])
        # db.commit()
        game = db.getGameByWosID(30265)

    def test_side(self):
        where_clause = 'AND entries.id = 5856'
        games = zxdb.getGames(where_clause)
        for release in games[0].releases:
            release.getInfoFromLocalFiles()
            pass
        wos_names = [file.wos_name for file in games[0].getFiles()]
        self.assertIn('Zip-Zap - Alternate - Side 1.tzx', wos_names)
        self.assertIn('Zip-Zap - Alternate - Side 2.tzx', wos_names)
        db.addGame(games[0])
        db.commit()
        game = db.getGameByWosID(5856)
        wos_names = [file.wos_name for file in game.getFiles()]
        self.assertIn('Zip-Zap - Alternate - Side 1.tzx', wos_names)
        self.assertIn('Zip-Zap - Alternate - Side 2.tzx', wos_names)
