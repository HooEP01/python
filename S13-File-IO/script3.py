# file path
with open ('file/test.txt', mode='w') as my_file:
    print(my_file.write('write something here')) 

with open ('file/test.txt', mode='r') as my_file:
    print(my_file.read()) 