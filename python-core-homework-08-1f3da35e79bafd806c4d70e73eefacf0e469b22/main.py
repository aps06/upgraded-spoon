from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    birthday = {}

    today = date.today()

    if len(users) == 0:
        return {}
    for dicts in users:
        today = date.today()
        if dicts['birthday'].strftime('%Y') < today.strftime('%Y'):
            dicts['birthday'] = datetime(
                int(today.strftime('%Y')),
                int(dicts['birthday'].strftime('%m')),
                int(dicts['birthday'].strftime('%d'))).date()

        if today.strftime('%A') == "Sunday":
            today += timedelta(days=1)

        elif today.strftime('%A') == "Saturday":
            today += timedelta(days=2)

        for i in range(7):
            date_days = today
            date_days += timedelta(days=i)
            date_m_d = [date_days.strftime('%m %d'),
                        dicts['birthday'].strftime('%m %d')]

            if date_m_d[0] == date_m_d[1]:
                day_week = dicts['birthday'].strftime('%A')

                if day_week in ["Monday", "Tuesday", "Wednesday",
                                "Thursday", "Friday"]:

                    try:
                        birthday[day_week] += [dicts['name'].split()[0]]

                    except KeyError:
                        birthday[day_week] = [dicts['name'].split()[0]]

                else:

                    try:
                        birthday['Monday'] += [dicts['name'].split()[0]]

                    except KeyError:
                        birthday['Monday'] = [dicts['name'].split()[0]]

    users = birthday
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum",
         "birthday": datetime(1976, 1, 11).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
