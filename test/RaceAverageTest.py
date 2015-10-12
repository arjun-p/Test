import unittest
from Test import RaceAvg


class TestRaceAvg(unittest.TestCase):
    """Tests for RaceAvg.py"""

    def test_roundUp(self):
        race = RaceAvg.RaceAverage()
        self.assertEqual(race.roundUp(4.0), 4)
        self.assertEqual(race.roundUp(4.01), 4)
        self.assertEqual(race.roundUp(4.2), 4)
        self.assertEqual(race.roundUp(4.495), 4)
        self.assertEqual(race.roundUp(4.5), 5)
        self.assertEqual(race.roundUp(4.51), 5)
        self.assertEqual(race.roundUp(4.9), 5)
        self.assertEqual(race.roundUp(4.99), 5)

    def test_timeParser(self):
        race = RaceAvg.RaceAverage()
        self.assertEqual(race.timeParser("08:00 AM, DAY 1"), [1, 8, 0])
        self.assertEqual(race.timeParser("12:00 AM, DAY 1"), [1, 0, 0])
        self.assertEqual(race.timeParser("12:25 PM, DAY 1"), [1, 12, 25])
        self.assertEqual(race.timeParser("10:00 PM, DAY 2"), [2, 22, 0])
        self.assertEqual(race.timeParser("04:00 PM, DAY 99"), [99, 16, 0])
        self.assertEqual(race.timeParser("04:00 PM, DAY 99"), [99, 16, 0])

    def test_validator_negative(self):
        race = RaceAvg.RaceAverage()
        self.assertRaises(ValueError, race.validator, ["13:00 PM, DAY 1"])
        self.assertRaises(ValueError, race.validator, ["13:00 AM, DAY 1"])
        self.assertRaises(ValueError, race.validator, ["8:00 AM, DAY 10"])
        self.assertRaises(ValueError, race.validator, ["00:00 AM, DAY 10"])
        self.assertRaises(ValueError, race.validator, ["01:00 AM, DAY 120"])
        self.assertRaises(ValueError, race.validator, ["01:00 AM, DAY 99.5"])
        self.assertRaises(ValueError, race.validator, ["01:00 AM, DAY 0"])
        self.assertRaises(ValueError, race.validator, ["DAY"])

    def test_avgMinutes_incorrectEndTime(self):
        end_times = ["12:00 PM, DAY 1", "12:01 PM, DAY 0"]
        race = RaceAvg.RaceAverage()
        self.assertRaises(ValueError, race.avgMinutes(end_times))

    def test_avgMinutes_exceedDaysLimit(self):
        end_times = ["12:00 PM, DAY 1", "12:01 PM, DAY 100"]
        race = RaceAvg.RaceAverage()
        self.assertRaises(ValueError, race.avgMinutes(end_times))

    def test_avgMinutes_endingSameDay(self):
        end_times = ["12:00 PM, DAY 1", "12:01 PM, DAY 1"]
        race = RaceAvg.RaceAverage()
        self.assertEqual(race.avgMinutes(end_times), 241)

    def test_avgMinutes_endingBefore24Hours(self):
        end_times = ["12:00 AM, DAY 2"]
        race = RaceAvg.RaceAverage()
        self.assertEqual(race.avgMinutes(end_times), 960)

    def test_avgMinutes_endingNextDay(self):
        end_times = ["10:00 PM, DAY 2", "11:00 PM, DAY 2"]
        race = RaceAvg.RaceAverage()
        self.assertEqual(race.avgMinutes(end_times), 2310)

    def test_avgMinutes_endingAfterWeeks(self):
        end_times = ["02:00 PM, DAY 19", "02:00 PM, DAY 20", "01:58 PM, DAY 20"]
        race = RaceAvg.RaceAverage()
        self.assertEqual(race.avgMinutes(end_times), 27239)

if __name__ == '__main__':
    unittest.main()
