import ctypes
import time

a = []
c = 0
x = 4

# display


while True:
    with open('file.txt', 'a') as the_file:
        the_file.write('{}\n'.format(c))
        c += 1
        time.sleep(1)




