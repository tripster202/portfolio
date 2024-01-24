# convert datetime object to epoch time

import datetime as dt

time_sample = '2023-05-13T13:49:37.207898Z'
dt_conversion = dt.datetime.strptime(time_sample.split('.')[0],'%Y-%m-%dT%H:%M:%S')
timestamp = int(dt_conversion.timestamp())

print(f'The time sample is {dt_conversion}\nThe timestamp is {timestamp}')

# print the datetime object in a different timezone
dt_timezone = dt_conversion-dt.timedelta(hours=5)
print(f'The time sample is {dt_conversion}\nThe timezone adjustment is {dt_timezone}')

# print the datetime object in a particular format
dt_formatted = dt_conversion.strftime('%y-%m-%d %H:%M:%S')
print(f'The time sample is {dt_conversion}\nThe formatted version is {dt_formatted}')