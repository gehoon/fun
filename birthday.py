#!~/bin/python
## Simulation of the birthday paradox (https://en.wikipedia.org/wiki/Birthday_problem)
import random

## Each Birthdays class comprises n number of birthdays
class Birthdays:
    def __init__(self, n=23): # initialization
        self.birthday = []
        for x in range(n):
            self.birthday.append(int(random.random()*365))
    def shared(self): # this function returns whether or not there's redundant birthdays
        seen = []
        for value in self.birthday:
            if value not in seen:
                seen.append(value)
            else:
                return True
        return False

## main script
## Generate 10000 groups with n number of birthdays, and count how many have redundant birthdays in them.
total = 10000
shared = 0

for x in range(total):
    birthdays = Birthdays()
    if birthdays.shared():
        shared = shared +1

print shared, "groups out of", total, "have members sharing the same birthday."

'''
## Another algorithm for birthday paradox

person = 23
odd = 1.0

for x in range(2,person+1):
    odd = odd * (366 - x)/365
    print x, "person:", (1-odd)*100, "%"

'''
