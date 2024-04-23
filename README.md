# Birthday Greeter

This script helps you greet colleagues with upcoming birthdays for the week. Given a list of users with their names and birthdays, it returns a dictionary where each key represents a day of the week ('Monday', 'Tuesday', etc.) and the corresponding value is a list of names of users whose birthdays fall within the upcoming week, including the current day.

## Usage

1. **Function: `get_birthdays_per_week`**
   - Input: List of dictionaries, where each dictionary contains the keys 'name' (string) and 'birthday' (datetime.date object).
   - Output: Dictionary with days of the week as keys and lists of names as values.

2. **Example Usage**
   ```python
   from datetime import datetime

   # Sample user data
   users = [
       {"name": "Jan Koum", "birthday": datetime(1976, 4, 24).date()},
       {"name": "John", "birthday": datetime(1980, 12, 31).date()},
       # ...
   ]

   # Get birthdays for the week
   result = get_birthdays_per_week(users)
   
   # Print the result
   for day_name, names in result.items():
       print(f"{day_name}: {', '.join(names)}")

    Example Output

    Monday: Kim, Jan Koum
    Tuesday: Alice
    Wednesday: John