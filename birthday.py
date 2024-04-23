from datetime import date, datetime, timedelta
from typing import Dict, List, Any


def get_birthdays_per_week(users: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    result = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    # current_date = date.today()
    current_date = datetime(year=2023, month=12, day=26)
    current_weekday = current_date.weekday()

    start = None
    end = None

    if current_weekday == 0:
        start, end = 2, 5
    elif current_weekday in [1, 2, 3, 4, 5]:
        start, end = 0, 7
    elif current_weekday == 6:
        start, end = 1, 6

    date_range = [(current_date + timedelta(i)).date() for i in range(start, end)]

    for user in users:
        if current_date.month == 12 and user["birthday"].month == 1:
            user_birthday_this_year = datetime(year=current_date.year + 1, month=user["birthday"].month,
                                               day=user["birthday"].day).date()
        else:
            user_birthday_this_year = datetime(year=current_date.year, month=user["birthday"].month,
                                               day=user["birthday"].day).date()

        if user_birthday_this_year in date_range:
            if (user_birthday_this_year.weekday() == 0 or user_birthday_this_year.weekday() == 5
                    or user_birthday_this_year.weekday() == 6):
                result["Monday"].append(user["name"])
            elif user_birthday_this_year.weekday() == 1:
                result["Tuesday"].append(user["name"])
            elif user_birthday_this_year.weekday() == 2:
                result["Wednesday"].append(user["name"])
            elif user_birthday_this_year.weekday() == 3:
                result["Thursday"].append(user["name"])
            elif user_birthday_this_year.weekday() == 4:
                result["Friday"].append(user["name"])

    keys_to_delete = [key for key, value in result.items() if not value]

    for k in keys_to_delete:
        result.pop(k)

    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 4, 24).date()},
        {"name": "John", "birthday": datetime(1980, 12, 31).date()},  # sunday
        {"name": "Doe", "birthday": datetime(1990, 12, 27).date()},  # wednesday
        {"name": "Alice", "birthday": datetime(2022, 1, 2).date()},  # tuesday
        {"name": "Kim", "birthday": datetime(2022, 1, 1).date()},  # monday
        {"name": "Bill", "birthday": datetime(2022, 12, 26).date()},  # tuesday
        {"name": "Jane", "birthday": datetime(2022, 12, 30).date()},  # saturday
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 29).date()},  # friday
        {"name": "John", "birthday": datetime(1980, 12, 28).date()},  # thursday
        {"name": "Doe", "birthday": datetime(1990, 4, 24).date()},
        {"name": "Alice", "birthday": datetime(2024, 1, 24).date()},
        {"name": "Kim", "birthday": datetime(2024, 4, 21).date()},
        {"name": "Bill", "birthday": datetime(2024, 4, 20).date()},
        {"name": "Jane", "birthday": datetime(2024, 4, 22).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
