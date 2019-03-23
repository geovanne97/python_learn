#strings
mystring = "abcdefg"
print(mystring[0])
#slicing
print(mystring[:3])
#agora com o print abaixo dará a seguinte saída, out: aceg
print(mystring[::2])
#basic methods
x = mystring.upper()
y = mystring.lower()

word = "hello world"
spl = word.split()#o split ele vai montar um vetor dividindo as palavros pelo parametro que colocar dentro do method
                  #como não tem nada ele irá dividir pelo espaço
print(spl)
#outro exemplo utilizando split
tweet = "go sports! #sports"
results = tweet.split('#')[1]
print(results)#out:sports

#print format
test = "Item one: {b} Item two: {m}".format(b = "book",m = "milk")
print(test)
