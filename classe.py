class Animal():

    def __init__(self):
        print("animal created")

    def whoAmI(self):
        print("animal")

    def eat(self):
        print("eating")

class Dog(Animal):
    def __init__(self):
        #Animal.__init__(self):#mas eu posso comentar esse método
        print("dog created")

    def bark(self):
        print("wolf")

    def eat(self):#isso aqui vai sobescrever o método de cima, da classe animal
        print("dog eating")

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
"""
out: animal created
     dog created
     Animal
     eating
"""
#special methods sao os metodos que vc coloca __ antes do nome
class Book():
    def __init__(self,title,author,pages):#toda vez que alguém for criar a classe book terá que passas essas informações
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):#representação em string do meu objeto
        return "Title: {}, Author: {}, pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):#só posso saber qnts atributos meu método tem se tiver esse método, e tudo que eu colocar nele ele vai contar
        return self.pages

    def __del__(self):
        print("the book has been destroyed")

b = Book("python","jose",200)
#print(b) ele vai me dar o endereço de memória da classe, para printar terei que criar um def __str__
print(b)
print(len(b))
del b
