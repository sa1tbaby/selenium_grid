def createGenerator() :
    mylist = range(1)
    for i in mylist :
        yield i*i
        print('a')

mygenerator = createGenerator() # создаём генератор
print(mygenerator) # mygenerator является объектом!

for i in mygenerator:
    print(i)
    print('s')