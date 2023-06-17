# CHAPTER 8 - IMPORTING LIBRARIES 
# DOING MATHEMATICS - page 102/103

# Import math and random modules to make their features available
import math , random

# display two rounded values - rounded up and down from 9.5
print('Rounded Up 9.5 : ' , math.ceil(9.5))
print('Rounded Down 9.5 : ' , math.floor(9.5))

# inialize a variable with an integer value
num = 4

# display the square and the square root of the variable value
print(num , 'Squared : ' , math.pow(num, 2))
print(num , 'Square Root : ' , math.sqrt(num))

# produve a random list of 6 unique numbers between 1 and 59 inclusive
nums = random.sample(range(1,60),6)

# display the random list
print('Your lucky Lotto numbers are : ',nums)
