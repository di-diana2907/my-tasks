from datetime import datetime
from datetime import timedelta
from calendar import monthrange, isleap


DATE_TEMPLATE = '%Y-%m-%d'


def week_period_end(start):
    return start + timedelta(days=6 - start.weekday())


def month_period_end(start):
    month_days_count = monthrange(start.year, start.month)[1]
    return datetime(start.year, start.month, month_days_count)


def year_period_end(start):
    return datetime(start.year, 12, 31)


def quarter_period_end(start):
    quart_end_month = ((start.month - 1) // 3 + 1) * 3
    days_num = monthrange(start.year, quart_end_month)[1]
    return datetime(start.year, quart_end_month, days_num)


def review_period_end(start):
    return datetime(start.year, 9, 30) if start.month in range(4, 10) \
            else datetime(start.year + 1, 3, 31)


def get_period_end(label, start):
    case_dict = {
        'WEEK': week_period_end,
        'MONTH': month_period_end,
        'YEAR': year_period_end,
        'QUARTER': quarter_period_end,
        'REVIEW': review_period_end,
    }
    return case_dict[label](start)


def get_result(label, start, end):
    periods = []
    while True:
        period_end = get_period_end(label, start)
        start_str = start.strftime(DATE_TEMPLATE)
        end_str = period_end.strftime(DATE_TEMPLATE)
        if period_end >= end:
            end_str = end.strftime(DATE_TEMPLATE)
            periods.append(f'{start_str} {end_str}')
            break
        periods.append(f'{start_str} {end_str}')
        start = period_end + timedelta(days=1)
    return periods


def print_result(periods):
    print(len(periods))
    for period in periods:
        print(period)


type = input().strip()
start_date, end_date = [datetime.strptime(s, DATE_TEMPLATE)
                        for s in input().strip().split(' ')]
result = get_result(type, start_date, end_date)
print_result(result)

