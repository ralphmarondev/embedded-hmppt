import time
i = 0
while True:
    try:
        f = open('hello.txt', 'w')
        f.write(f'123: {i}')
        f.close()
    except:
        print('Error')
    
    i += 1
    print('Writing to file...')
    time.sleep(2)
