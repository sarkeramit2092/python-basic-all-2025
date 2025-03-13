# Python datetime Module

## Importing datetime
To work with dates and times in Python, import the `datetime` module:
```python
import datetime
```

## Getting the Current Date and Time
- **Current Date:**
  ```python
  today = datetime.date.today()
  print(today)  # Outputs: YYYY-MM-DD
  ```
- **Current Date & Time:**
  ```python
  now = datetime.datetime.now()
  print(now)  # Outputs: YYYY-MM-DD HH:MM:SS.microseconds
  ```
- **Current Time Only:**
  ```python
  current_time = datetime.datetime.now().time()
  print(current_time)  # Outputs: HH:MM:SS.microseconds
  ```

## Creating a Specific Date and Time
- **Date:**
  ```python
  specific_date = datetime.date(2025, 3, 12)
  print(specific_date)  # 2025-03-12
  ```
- **Time:**
  ```python
  specific_time = datetime.time(12, 30, 0)
  print(specific_time)  # 12:30:00
  ```
- **Date and Time:**
  ```python
  specific_datetime = datetime.datetime(2023, 1, 2, 12, 30, 1)
  print(specific_datetime)  # 2023-01-02 12:30:01
  ```

## Comparing Dates
```python
current_datetime = datetime.datetime.now()
target_datetime = datetime.datetime(2023, 1, 2, 12, 30, 1)

if target_datetime < current_datetime:
    print("Target date has passed! 😒")
else:
    print("Target date has NOT passed! 😁")
```

## Formatting Dates and Times
- **Using `strftime()` to Format:**
  ```python
  formatted_date = now.strftime("%H:%M:%S %d-%m-%Y")
  print(formatted_date)  # Outputs formatted date
  ```
- **Available format specifiers:**
  | Format | Meaning |
  |--------|---------|
  | %Y | Full year (e.g., 2025) |
  | %m | Month (01-12) |
  | %d | Day (01-31) |
  | %H | Hour (00-23) |
  | %M | Minute (00-59) |
  | %S | Second (00-59) |
  | %A | Full weekday name (e.g., Monday) |
  | %B | Full month name (e.g., March) |

Example:
```python
print(now.strftime("%A, %B %d, %Y"))  # e.g., "Wednesday, March 12, 2025"
```

## Using `timedelta` for Date Arithmetic
- **Adding 90 days to a date:**
  ```python
  var_date = datetime.date(2023, 1, 1)
  dt = datetime.timedelta(days=90)
  new_date = var_date + dt
  print(new_date)  # Outputs: 2023-04-01
  ```

## Parsing a Date String
- **Using `strptime()` to Parse Dates:**
  ```python
  default_date = "2/20/2023"
  parsed_date = datetime.datetime.strptime(default_date, "%m/%d/%Y")
  print(parsed_date)  # Outputs: 2023-02-20 00:00:00
  ```

## Summary
The `datetime` module is useful for handling dates and times in Python. It provides functions for:
- Retrieving the current date/time
- Creating specific dates/times
- Comparing dates
- Formatting and parsing date strings
- Performing date arithmetic with `timedelta`

### Example Usage:
```python
import datetime

today = datetime.date.today()
print("Today's date:", today)

future_date = today + datetime.timedelta(days=10)
print("Date after 10 days:", future_date)
```

