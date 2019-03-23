#1) use a string django e print "d" "o" "djan" use indexing to reverse the strings
x = "django"
print(x[0])
print(x[-1])
print(x[0:4])
#to reverse the string
xtwo = x[::-1]

#2)dado a lista abaixo, mude hello por goodbye
l = [3,7,[1,4,"hello"]]
l[2][2] = "goodbye"
print(l)

#3)print na palavra hello do dicionário
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])#é necessário colocar este 0 adicional 
