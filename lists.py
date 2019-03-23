#lists
mylist = [[1,2,3],"abcd",True,4.4]
print(len(mylist))
mylist[0] = "hello"#isso muda o valor da posição 0 da lista
mylist.append("oi")#vai adicionar na última posição da lista o oi

mylistone = [1,2,3]
mylisttwo = ["oi",1.2,3]
mylistone.extend(mylisttwo)#ele vai fazer com que a lista 2 entre na lista 1, n como uma outro lista mas com os parametros
                        #out: [1,2,3,"oi",1.2,3]
                        #mylistone.append(mylisttwo), out:[1,2,3,[]"oi",1.2,3]]

#remove item of the list
item = mylist.pop(0)# or i can use mylist.remove(“True”)
#put the list in crescent order
numberlist = [1,5,6,3,66,54]
numberlist.sort()#out:a lista com os números em ordem crescente

anotherlist = [1,2,["aa","b","c"]]
#i want to print the letter b
print(anotherlist[2][1])

#criar matriz
matrix = [[1,5,6],[1,5,6],[1,5,6]]#isso cria uma matriz na qual cada elemento é um linha
first_col = [row[0] for row in matrix]#pega o primeiro elemento de cada linha
print(first_col)#out:1,1,1

#creating a list using range
list(range(0,20,2))#out: [0,2,4,6,8,...,20]os dois primeiros numeros indicam o
                   #tamanho da lista e o terceiro indica que ele pula de 2 em 2

for item in range(10)
    print(item)#ele vai printar do numero 0 ate o 9

#colocar numa lista o valor ao quadrado da outra
lone = [1,2,3,4]
out = []
for num in lone:
    out.append(num**2)

print(out)#out:[1,4,9,16]
#another way to do that
out = [num**2 for num in lone]
print(out)#out:[1,4,9,16]
