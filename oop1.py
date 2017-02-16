import random

file = open('sometextfile.txt', 'a')

iteration = 0

while iteration < 1000:

    file.write(str(random.randrange(0, 9999)) + ';')
    iteration += 1

file.close()