import datetime

# print (dir(datetime))
# print(help(datetime))

guido_van_rossum = datetime.date(1956, 1, 31)
# default format yyyy-mm-dd

print(guido_van_rossum.day)

var_date = datetime.date(2023, 1, 1)
dt = datetime.timedelta(90)

print(var_date+dt)

# Day name, month name, Day-number, Year
# case sensitive

print(guido_van_rossum.strftime("%A, %B, %d %Y"))

# open braces {} and : is mandatory

message = "Guido van Rossum was bord on {:%A, %B %d, %Y}."

print(message.format(guido_van_rossum))

ch_launch_date = datetime.date(2021, 1, 3)
ch_launch_time = datetime.time (18, 00, 00)

ch_launch_datetime = datetime.datetime(2021, 1, 3, 18, 00, 00)

print(ch_launch_date)
print(ch_launch_time)
print(ch_launch_datetime)

print(ch_launch_time.hour)

# current datetime today() method (microseconds)

now = datetime.datetime.today()
print(now)
print(now.day)

# parsing string into date and time and create a datetime object
# strptime()

default_date = "2/20/2023"
default_date_datetime = datetime.datetime.strptime(default_date, "%m/%d/%Y")
print (default_date_datetime)

print(type(default_date_datetime))