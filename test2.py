import ctypes
import time

# a = []
# c = 0
# x = 4
#
# # display
#
#
# while True:
#     with open('file.txt', 'a') as the_file:
#         the_file.write('{}\n'.format(c))
#         c += 1
#         time.sleep(1)
#
#

# s = 0
# with open("file.txt") as file_in:
#     lines = []
#     for line in file_in:
#         if line == 'EndSpread':
#             last_value = 'EndSpread'
#             break
#         else:
#             symbol, target_price, volume = line.strip('\n').split(',')
#             # print(symbol, target_price, volume)
#             print(symbol.split('-')[0],symbol)
#             s += float(volume)
#
# print(s)
# print(s*0.01*(1-0.001))

with open('file.txt', 'a') as the_file:
    the_file.write('EndSpread')