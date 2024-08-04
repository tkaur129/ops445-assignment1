import sys
from datetime import datetime, timedelta

def leap_year(year: int) -> bool:
    """Return True if the given year is a leap year, otherwise False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """Return the number of days in the given month of the given year."""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) and month == 2:
        return 29
    return days_in_month[month - 1]

def after(today: str) -> str:
    """Return the next day's date in DD/MM/YYYY format."""
    day, month, year = map(int, today.split('/'))
    day += 1
    if day > mon_max(month, year):
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1
    return f"{day:02d}/{month:02d}/{year:04d}"

def before(today: str) -> str:
    """Return the previous day's date in DD/MM/YYYY format."""
    day, month, year = map(int, today.split('/'))
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = mon_max(month, year)
    return f"{day:02d}/{month:02d}/{year:04d}"

def valid_date(date: str) -> bool:
    """Check if the given date is valid."""
    try:
        day, month, year = map(int, date.split('/'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False
        return True
    except ValueError:
        return False

def day_of_week(date: str) -> str:
    """Return the day of the week for a given date in DD/MM/YYYY format."""
    day, month, year = map(int, date.split('/'))
    date_obj = datetime(year, month, day)
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return days[date_obj.weekday()]

def day_count(start_date: str, end_date: str) -> int:
    """Count the number of weekends between the start date and end date inclusive."""
    start = datetime.strptime(start_date, "%d/%m/%Y")
    end = datetime.strptime(end_date, "%d/%m/%Y")
    weekend_count = 0
    
    current_date = start
    while current_date <= end:
        if current_date.weekday() in [5, 6]:  # 5 = Saturday, 6 = Sunday
            weekend_count += 1
        current_date += timedelta(days=1)
    
    return weekend_count

def usage():
    """Print usage message."""
    print("Usage: python milestone2.py DD/MM/YYYY DD/MM/YYYY")

def main():
    if len(sys.argv) != 3:
        usage()
        return
    
    start_date = sys.argv[1]
    end_date = sys.argv[2]

    if not valid_date(start_date) or not valid_date(end_date):
        usage()
        return
    
    # Ensure start_date is earlier than end_date
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    weekends = day_count(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")

if __name__ == "__main__":
    main()
