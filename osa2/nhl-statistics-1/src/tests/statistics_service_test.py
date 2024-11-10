import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_konstruktori(self):
        self.assertNotEqual(self.stats, None)

    def test_search_players(self):
        p = self.stats.search("Semenko")
        self.assertAlmostEqual( p.name, "Semenko")
        p = self.stats.search("LOL")
        self.assertAlmostEqual(p, None)
    def test_team(self):
        t = self.stats.team("EDM")
        self.assertNotEqual(t, None)
    def test_top(self):
        top = self.stats.top(1)

    

