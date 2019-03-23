#dictionaries
my_stuff = {"key1":"value","key2":123,"key3":{"123":[1,2,"grabMe"]}}
#printar grabMe em maiusculo
print(my_stuff["key3"]["123"][2].upper())
#mudando valor de key1
my_stuff['key1'] = "burger"
#adicionando termos ao dicionario
my_stuff["dinner"] = "pasta"

pins = {"Mike":1234, "Joe":1111, "Jack":2222}
pins.keys()
#out: will give me the names
pins.values()
#out: will give me the number or the arguments in the right

person97 = {"name":"Jack", "surname":"Smith", "age":"29"}
#remove the key name
person97.pop(“name”)


#mapping two lists to a dictionary
keys = [“a”, ”b”, ”c”]
values = [1, 2, 3]
mydict = dict(zip(keys, values))
