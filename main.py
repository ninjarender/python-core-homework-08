from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()

    period_start = today
    period_end = today + timedelta(days=6)

    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }

    for user in users:
        name = user["name"].split()[0]
        birthday = user["birthday"]

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if period_start <= birthday_this_year <= period_end:
            day_of_week = birthday_this_year.strftime('%A')

            if day_of_week in ['Saturday', 'Sunday']:
                birthdays_per_week['Monday'].append(name)
            elif day_of_week in birthdays_per_week:
                birthdays_per_week[day_of_week].append(name)

    return {day: names for day, names in birthdays_per_week.items() if names}

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
