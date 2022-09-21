for i in range(4):
    filename = str(i) +'.txt'
    f = open(filename, 'w')
    f.write('text')
    f.close()