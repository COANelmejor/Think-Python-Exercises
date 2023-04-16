## Exercise 1.1
## Responses are for python 3
print('\n')

# ---------------------------------------------------------------
## In a print statement, what happens if you leave out one of the parentheses, or both?

## It  will not run the print statement if you leave out one of the parentheses, or both.
## This is because python 3 the print statement is a function and not a statement.
print('This is a print statement with one parenthesis.')

# ---------------------------------------------------------------
## If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?

## If you leave out one of the quotation marks, or both, python will not run the print statement.
## Because python will think that the string is not closed.
## 
## Example:
## This will not run.
## print('This is a print statement with one quotation mark.) 
## This will run.
print('This is a print statement with both quotation marks.')

# ---------------------------------------------------------------
# You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?

## If you put a plus sign before a number, python will sum the number with the number after the plus sign.
## Python will treat the number as a positive number.
## Example:
## This will run.
print(+ 2 + 2)

## The same thing happens if you put a plus sign after a number.
## Example:
## This will run.
print(2 + + 2)

# ---------------------------------------------------------------
# In math notation, leading zeros are ok, as in 02. What happens if you try this in Python?

## If you try to use a leading zero in python, python will think that the number is an octal number.
## Example:
## This will not run.
## print(02 + 2)

## To fix this, you can use the following syntax:
## This will run.
print(0o2 + 2)

## You can also use the following syntax:
## This will run.
print(0x2 + 2)

# ---------------------------------------------------------------
# What happens if you have two values with no operator between them?

## If you have two values with no operator between them, it will lean to a syntax error.
## Example:
## This will not run.
## print(2 2)


