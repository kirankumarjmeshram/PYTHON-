# Python Command Line Arguments

import sys

print(type(sys.argv))
print('The command line arguments are:')
for i in sys.argv:
    print(i)


# for cammand : python pythonCLA.py "my" "name" "is" "kirankumar" 21
# output is =>
    # <class 'list'>
    # The command line arguments are:
    # pythonCLA.py
    # my
    # name
    # is
    # kirankumar
    # 21