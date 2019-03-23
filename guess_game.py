import random
def get_guess():
    return input("what is your guess: ")

#gerar os 3 números aleatórios
def generate_code():
    digits = [str(num) for num in range(10)]#ele vai gerar uma lista com 10 posições e valores de 0 - 9
    random.shuffle(digits)#ele vai embaralhar os valores da lista
    return digits[:3]

#gerar as mensagens
def generate_clues(code, user_guess):
    if user_guess == code:
        return "code cracked"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if clues == []:
        return ["nope"]
    else:
        return clues


#run game logic
print("welcome code breaker")

secret_code = generate_code()

clue_report = []

while clue_report != "code cracked":
    guess = get_guess()

    clue_report = generate_clues(secret_code,guess)
    print("here is the result of your guess")

    for clue in clue_report:
        print(clue)

"""
este trecho de código é como se usa enumerate em uma lista
l = ['hello', 'world', 'hi', 'earth']
for i, word in enumerate(l):
    print i, word
ou
def posicoesQueIniciamCom(lista,letra='a'):
    result = []
    for i,palavra in enumerate(lista):
        if palavra.startwith(letra):
            result.append(i)
        return result
        
nomes = ["abc","123","456","bbb","aaa"]

print(posicoesQueIniciamCom(nomes))
"""
