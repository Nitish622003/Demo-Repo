num = int(input('Enter a number'))
last_digit = num % 10
if last_digit % 3 == 0:
    print('its is dividible by 3')
else:
    print('it is not divisible by 3')
