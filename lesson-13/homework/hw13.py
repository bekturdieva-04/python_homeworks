from datetime import datetime, timedelta
import re
import pytz
import time

# 1. Age Calculator
def calculate_age():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age_months = (today.year - birthdate.year) * 12 + today.month - birthdate.month
    age_days = (today - birthdate).days
    print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

calculate_age()
    
# 2. Days Until Next Birthday
def days_until_birthday():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_remaining = (next_birthday - today).days
    print(f"Days until your next birthday: {days_remaining}")

days_until_birthday()

# 3. Meeting Scheduler
def meeting_scheduler():
    current_datetime = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Enter meeting duration (hours): "))
    duration_minutes = int(input("Enter meeting duration (minutes): "))
    start_time = datetime.strptime(current_datetime, "%Y-%m-%d %H:%M")
    end_time = start_time + timedelta(hours=duration_hours, minutes=duration_minutes)
    print(f"The meeting will end at {end_time.strftime('%Y-%m-%d %H:%M')}")

meeting_scheduler()
 
# 4. Timezone Converter
def timezone_converter():
    dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_tz = input("Enter your current timezone (e.g., UTC, Asia/Tashkent): ")
    to_tz = input("Enter the target timezone: ")
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    dt = from_zone.localize(dt)
    converted_dt = dt.astimezone(to_zone)
    print(f"Converted time: {converted_dt.strftime('%Y-%m-%d %H:%M %Z')}")

timezone_converter()

# 5. Countdown Timer
def countdown_timer():
    target_time = input("Enter the future date and time (YYYY-MM-DD HH:MM:SS): ")
    target_time = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
    while True:
        remaining = target_time - datetime.now()
        if remaining.total_seconds() <= 0:
            print("Time's up!")
            break
        print(f"Time remaining: {remaining}", end="\r")
        time.sleep(1)

countdown_timer()

# 6. Email Validator
def email_validator():
    email = input("Enter an email address: ")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        print("Valid email.")
    else:
        print("Invalid email.")

email_validator()
 
# 7. Phone Number Formatter
def phone_formatter():
    phone = input("Enter a 10-digit phone number: ")
    formatted_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print(f"Formatted phone number: {formatted_phone}")

phone_formatter()

# 8. Password Strength Checker
def password_checker():
    password = input("Enter a password: ")
    if (len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password)):
        print("Strong password.")
    else:
        print("Weak password. Use at least 8 characters with uppercase, lowercase, and a number.")

password_checker()

# 9. Word Finder
def word_finder():
    text = input("Enter a text: ")
    word = input("Enter a word to find: ")
    matches = [m.start() for m in re.finditer(rf'\b{word}\b', text, re.IGNORECASE)]
    print(f"Word found at positions: {matches}")

word_finder()

# 10. Date Extractor
def date_extractor():
    text = input("Enter a text: ")
    dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
    print(f"Extracted dates: {dates}")

date_extractor()
