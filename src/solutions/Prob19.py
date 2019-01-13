import src.EulerHelpers as Euler
import math
weekdays = \
        [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
        ]


months = \
        [

            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]


def gen_cycle(cycle_list):

    cycle_len = len(cycle_list)
    cycle_index = 0
    while True:
        yield cycle_list[cycle_index]
        cycle_index = (cycle_index + 1) % cycle_len


def gen_date():

    weekday_iter = gen_cycle(weekdays)
    month_iter = gen_cycle(months)

    year = 1900 - 1
    while True:

        # start year
        year += 1

        # start Jan 1 1900
        for month in months:

            # get month length
            if month in ('February', ):

                # century divisible by 400
                if year % 400 == 0:
                    day_count = 29
                # year divisible by four but not a century
                elif year % 4 == 0 and year % 100 != 0:
                    day_count = 29
                else:
                    day_count = 28

            elif month in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
                day_count = 31
            else:
                day_count = 30

            # finally know number of days in month
            for day in range(1, day_count + 1):
                weekday = weekday_iter.__next__()
                date_str = '{weekday:<9}, {month:<10} {day:>2}, {year:>4}'.format(day=day, month=month, year=year, weekday=weekday)
                yield date_str


if __name__ == '__main__':

    year_iter = gen_date()

    # go to Jan. 1, 1901
    date_str = ''
    while '1901' not in date_str:
        date_str = year_iter.__next__()
        print(date_str)

    # count Sundays
    sunday_count = 0
    date_str = ''
    while '2001' not in date_str:
        date_str = year_iter.__next__()
        print(date_str)
        if 'Sunday' in date_str and ' 1,' in date_str:
            sunday_count += 1

    print("answer =", sunday_count)
