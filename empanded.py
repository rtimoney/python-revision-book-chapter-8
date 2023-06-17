# CHAPTER 8 - IMPORTING LIBRARIES 
# CALCULATING DECIMALS - Page 104/105

# initialize two variables with floating-point values
item = 0.70
rate = 1.05

# initialize two more variables by attempting floating point arithmetic with the first two variables
tax = item * rate
total = item + tax

# Display variable values formatted to have two decimal places so trailing 
print('Item:\t','{:.20f}'.format(item))
print('Tax:\t','{:.20f}'.format(tax))
print('Total:\t','{:.20f}'.format(total))