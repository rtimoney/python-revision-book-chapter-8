# CHAPTER 8 - IMPORTING LIBRARIES 
# CALCULATING DECIMALS - Page 104/105

# import the decimal module
from decimal import *

# initialize two variables as Decimal objects
item = Decimal(0.70)
rate = Decimal(1.05)

# initialize two more variables by attempting floating point arithmetic with the first two variables
tax = item * rate
total = item + tax

# Display variable values formatted to have two decimal places so trailing 
print('Item:\t','{:.2f}'.format(item))
print('Tax:\t','{:.2f}'.format(tax))
print('Total:\t','{:.2f}'.format(total))

# always use the Decimal object to calculate monetary values or anywhere that accuracy is essential

