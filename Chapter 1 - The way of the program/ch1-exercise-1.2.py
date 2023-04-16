## Exercise 1.2
print('\n')

## How many seconds are there in 42 minutes 42 seconds?

seconds = (42 * 60) + 42

print('There are ' + str(seconds) + ' seconds in 42 minutes and 42 seconds.')
print('\n')

## How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

kilometers = 10
miles = kilometers / 1.61

print('There are ' + str(miles) + ' miles in 10 kilometers.')
print('\n')


## If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)?

pace = seconds / miles


print('My average pace is ' + str(pace) + ' seconds per mile and ' + str(pace / 60) + ' minutes per mile.')

## What is your average speed in miles per hour?
speed = miles / (seconds / 3600)

print('My average speed is ' + str(speed) + ' miles per hour.')
