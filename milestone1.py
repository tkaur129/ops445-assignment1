def leap_year(year: int) -> bool:
    """Return True if the year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def before(today: str) -> str:
    """Return the previous day's date in DD/MM/YYYY format."""
    # Split the date string into day, month, and year
    day, month, year = map(int, today.split('/'))
    
    # Define the number of days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust for leap years
    if leap_year(year):
        days_in_month[1] = 29
    
    # Decrement the day
    day -= 1
    
    # Check if we need to roll over to the previous month
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
            # Adjust for leap year on the previous year
            if leap_year(year):
                days_in_month[1] = 29
            else:
                days_in_month[1] = 28
        day = days_in_month[month - 1]
    
    # Return the new date in DD/MM/YYYY format
    return f"{day:02d}/{month:02d}/{year:04d}"
