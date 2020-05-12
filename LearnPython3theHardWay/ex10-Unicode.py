# I want to print as much unicode as python can
import unicodedata
import codecs
import os

# The range of unicode in 10
# min_code = int(input("The minimum unicode in 10: "))
# max_code = int(input("The maximum unicode in 10: "))
min_code = int("0xf900", 16)
max_code = int("0x10ffff", 16) + 1
# print the unicodes in hex and the corresponding characters

#for i in range(min_code, max_code):
#    try:
#        unicodedata.name(chr(i))
#        print("Order: {} => Unicode: {} => Character: {} => Name: {}".format(i, hex(i), chr(i), unicodedata.name(chr(i))))
#    except ValueError:
#        print("Order: {} => Unicode: {} => Character: {} => Name: {}".format(i, hex(i), chr(i), "No Character Name"))

f = open("UCD_All.txt", "a")

for i in range(min_code, max_code):
    try:
        unicodedata.name(chr(i))
        newline = u"Order: {} => Unicode: {} => Character: {} => Name: {}\n".format(i, hex(i), chr(i), unicodedata.name(chr(i)))
        # newline = newline.encode("utf-8")
        f.write(newline)
    except ValueError:
        newline = u"Order: {} => Unicode: {} => Character: {} => Name: {}\n".format(i, hex(i), chr(i), "No Character Name")
        # newline = newline.encode("utf-8")
        f.write(newline)

f.close()
