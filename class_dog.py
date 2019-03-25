class Dog():
    species = "mamifero"#este atributo não pode ser modificado

    def __init__(self,breed,name):#self é um parametro padrao que vai primeiro, o resto sao atributos da classe
        self.breed = breed
        self.name = name

mydog = Dog("Lab","Sammy")#quando for criar um objeto dog, tem que colocar as informações de todos os atributos
