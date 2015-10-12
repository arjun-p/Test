import math
import re
from datetime import timedelta


class RaceAverage:
    """ Class to calculate average number of minutes taken by the competitors to complete the race."""

    def __init__(self):
        self.start_time = "08:00 AM, DAY 1"

    @staticmethod
    def validator(times):
        """ Validates race end times.
        times contains between 1 and 50 elements inclusive.
        Each finish time in times is formatted as: hh:mm xM, DAY n.
        hh is exactly 2 digits giving the hour, mm is exactly 2 digits giving the minute, x is either 'A' or 'P'.
        n is a positive integer less than 100 with no leading zeros.

        Args:
            times : list of strings to validate
        Returns:
            True if all race times are in the correct format
        Raises:
            ValueError: if times is empty or contains more than 50 elements
            ValueError: if end time is not in the correct format.
        """
        if not times and len(times) > 50:
            raise ValueError('End Times should contain between 1 and 50 elements inclusive')

        for end_time in times:
            time_pattern = re.compile('^(0[1-9]|1[0-2]):([0-5][0-9])\s[AP]M,\sDAY\s([1-9]|[1-9][0-9])$')
            validate_pattern = re.search(time_pattern, end_time)
            if not validate_pattern:
                raise ValueError('Incorrect Time Format')

    @staticmethod
    def timeParser(t):
        """Splits the input into days, hours and minutes.
        Hours are calculated by converting 12 hour format to 24 hour format.

        Args:
            input (str): time to parse.
        Returns:
            days, hours and minutes as a list of int.
        """
        time = t.split()
        hours = int(time[0].split(':')[0])
        minutes = int(time[0].split(':')[1])
        days = int(time[3])
        meridiem = time[1][:2]

        # Convert to 24 Hour Format
        if meridiem == 'PM' and not hours == 12:
            hours += 12
        else:
            if meridiem == 'AM' and hours == 12:
                hours = 0
        return [days, hours, minutes]

    @staticmethod
    def roundUp(n):
        """Rounds the value to the nearest minute, with .5 rounding up.

        Args:
            n (int): number to be rounded.
        Returns:
            rounded value of n (int).
        """
        decimal = (str(n)).split('.')
        if decimal:
            if int(decimal[1][0]) >= 5:
                n = math.ceil(n)
        return int(n)

    def avgMinutes(self, times):
        """ Takes a list of race end times and calculates the average number of minutes.

        Args:
            times : list of strings representing race end time for each competitor.
        Returns:
            average number of minutes (int).
        Raises:
            ValueError: if end time is before start time.
        """

        try:
            self.validator(times)
            race_times = []
            start_time = self.timeParser(self.start_time)
            start_timedelta = timedelta(days=start_time[0], hours=start_time[1], minutes=start_time[2])
            for time in times:
                end_time = self.timeParser(time)
                end_timedelta = timedelta(days=end_time[0], hours=end_time[1], minutes=end_time[2])
                race_time = (end_timedelta - start_timedelta)
                if str(race_time)[0] == '-':
                    raise ValueError('End time should be after start time')
                race_time = race_time.total_seconds()//60
                race_times.append(race_time)

            total_minutes = 0
            for race_time in race_times:
                total_minutes += int(race_time)

            race_average = self.roundUp(total_minutes / len(race_times))
            return race_average
        except ValueError as e:
            print('Error: ', e)
