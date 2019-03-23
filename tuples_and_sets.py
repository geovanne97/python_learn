#tuples é parecido com uma lista, só que n pode ser modificado
t = (1, "oi")

#i will create a list od tuples
mypairs = [(1,2),(3,4),(5,6)]
for (tup1,tup2) in mypairs:
    print(tup2)#este vai receber o valor do segundo termo da tupla
    print(tup1)#este vai receber o valor do primeiro
#set
x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(4)
x.add(4)
print(x)#vai me dar um out: {1,2,4} ele não repete o número e coloca em ordem crescente

#converter uma lista em um set
converted = set([1,1,1,2,2,2,3,3,3,4,4,4])
print(converted)#vai me dar o seguinte out: {1,2,3,4}
