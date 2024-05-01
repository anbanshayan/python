# for i in range(1,6):
#     print("$"*10)
for x in range(0,5):
    for y in range(0,10):
        print('$',end='')
    print('')
# The end='' argument suppresses the automatic newline character that would normally be added after each print statement. 
# This allows multiple dollar signs to be printed on the same line.