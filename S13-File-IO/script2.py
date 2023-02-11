# mode
# read = r
# write = w
# append = a
# read + write = r+

# read
# with open('test.txt', mode='r') as my_file:
#     print(my_file.readlines())

# read + write
with open('tes.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me!')
    print(text)