#lambda expression eu posso usar como se fosse um if
my_list = [1,2,3,4,5,6,7,8]

evens = filter(lambda num:num%2 == 0, mylist)
print(list(evens))
#isso é igual a condicional abaixo
def even_bool(num):
    return num%2 == 0

evensone = filter(even_bool,my_list)
print(list(evensone))
#this exercise i will have to check if the sequence ["1""2""3"] apper in the array
def arrayCheck(nums):
    for i in range(len(nums)-2):#esse for ele começa da posição 0 e compara as duas posiçoes posteriores
                                #eu usei o -2 pq não tem como comparar a penultima e ultima posiçao com duas posiçoes posteriores
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

#problema 2 printar os valores da string que a posiçao for par
def string_bits(mystring):
    result = ''
    for i in range(len(mystring)):
        if i%2 == 0:
            result = result +mystring[i]
    return result
    #or we can do like that result = mystring[::2]

#problema 3 verificar de o final de uma string é igual o final da outra independente de tiver em upper or lower
#ex: end_other("AbC","HiaBc") -> True
def end_other(a,b):
    a = a.lower()
    b = b.lower()

    return a[-(len(b)):] == b or a == b[-(len(a)):]

#problema 4 duplicar cada caracter de uma strings
def doubleChar(mystring):
    result = ''
    for char in mystring:
        result += char*2
    return result

#problema 5 criar um somador com os valores da lista, só que ele nao pode somar os seguintes números 13,14,17,18,19
def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):

    if n [13,14,17,18,19]:
        return 0
    else:
        return n
