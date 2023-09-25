from function import doubleIt
from kargs_multiple import fullName as name
from default_args import *  # import all

result = doubleIt(500)
print(result)

fName = name('Tomato', 'Morich')
print(fName)
