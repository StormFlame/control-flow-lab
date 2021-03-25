input_month = input('Enter the month of the year (Jan - Dec): ')
input_day = int(input('Enter the day of the month: '))

if input_month in ('Jan', 'Feb', 'Mar'):
    season = 'Winter'
    if input_day > 19 and input_month == 'Mar':
        season = 'Spring'

elif input_month in ('Apr', 'May', 'Jun'):
    season = 'Spring'
    if input_day > 20 and input_month == 'Jun':
        season = 'Summer'

elif input_month in ('Jul', 'Aug', 'Sep'):
    season = 'Summer'
    if input_day > 21 and input_month == 'Sep':
        season = 'Fall'

elif input_month in ('Oct', 'Nov', 'Dec'):
    season = 'Fall'
    if input_day > 20 and input_month == 'Dec':
        season = 'Winter'

print(f'{input_month} {input_day} is in {season}')