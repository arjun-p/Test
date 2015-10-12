# Test
Text Blocker and Race Average Calculator


1. Text Blocking

Method text_blocker takes a single argument, lines, which is a list of strings and returns a list of strings that is read "downward", as opposed to left-to-right. That is, the first element of lines will correspond to the first "column" of the returned list, and so forth.

Constraints

lines will contain between 1 and 50 elements, inclusive.

Each element of lines will contain between 1 and 50 characters, inclusive.

Each element of lines will contain the same number of characters.

Each character in lines will be an uppercase letter ([A-Z]).

Examples

Input:

["AAA",
 "BBB",
 "CCC"]
Output:

["ABC",
 "ABC",
 "ABC"]
So, rows of the input become columns of the output.

Input:

["AAAAAAAAAAAAA"]
Output:

["A",
 "A",
 "A",
 "A",
 "A",
 "A",
 "A",
 "A",
 "A",
 "A",
 "A",
 "A",
 "A"]
Input:

["A",
 "A",
 "A",
 "A",
 "A"]
Output:

["AAAAA"]

2. Race Average

A Method, avgMinutes, is defined in class RaceAverage. It takes a list of strings, times, and returns the average number of minutes taken by the competitors to complete the race. The result is rounded to the nearest minute, with .5 rounding up.

Each finish time in times is formatted as

hh:mm xM, DAY n
where hh is exactly 2 digits giving the hour, mm is exactly 2 digits giving the minute, x is either 'A' or 'P', and n is a positive integer less than 100 with no leading zeros. So each string has exactly 15 or 16 characters (depending on whether n is less than 10).

The race starts on day 1 at 8:00 AM.

Notes:

"12:00 AM, DAY d" refers to midnight between DAY d-1 and DAY d

"12:00 PM, DAY d" refers to noon on DAY d

Constraints:

times contains between 1 and 50 elements inclusive

each element of times is formatted as specified above, with hh between 01 and 12 inclusive, mm between 00 and 59 inclusive, and d between 1 and 99 inclusive

each element of times represents a time later than the start of the race.

Examples:

Input:

["12:00 PM, DAY 1",
 "12:01 PM, DAY 1"]
Output:

241
From 8:00 AM to noon is 4 hours, so we have 4 hours for one competitor, and 4 hours, 1 minute for the other. These two values average to 240.5 minutes, which is rounded up.

Input:

["12:00 AM, DAY 2"]
Output:

960
The one competitor finished in 16 hours, just at the start of DAY 2.

Input:

["02:00 PM, DAY 19",
 "02:00 PM, DAY 20",
 "01:58 PM, DAY 20"]
Output:

27239
