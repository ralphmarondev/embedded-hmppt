import time
# f = open('hello.txt','a')

i = 0
while True:
    f = open('hello.txt', 'w')
    f.write(f'{i}\n')
    f.close()
    i += 1
    print(f'Value [console]: {i}')
    time.sleep(2)
    
