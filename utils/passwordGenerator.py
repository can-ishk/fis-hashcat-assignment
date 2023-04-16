from random import choice, randint
from math import ceil

symbol_set = set({"*", "$", "@", "%", "#"})


def generate_string(string: str, position: int, character: str):
    return "".join((string[:position], character, string[position:]))


def randomize_string(string: str, type: str, count: int, count_alt: int = 0):
    if (count_alt == 0):
        count_alt = randint(0, count)
    words = []
    if (type == "all"):
        if (randint(0, 1)):
            first_type = "numbers"
            second_type = "symbols"
        else:
            first_type = "symbols"
            second_type = "numbers"
        for s1 in randomize_string(string=string, type=first_type, count=count):
            words.append(s1)
            for s2 in randomize_string(string=s1, type=second_type, count=count_alt):
                words.append(s2)
        return words

    for i in range(count):
        pos = randint(0, len(string)-1)
        char = ""
        if (type == "symbols"):
            char = choice(tuple(symbol_set))
        if (type == "numbers"):
            char = str(randint(0, 9))
        string = generate_string(string=string, position=pos, character=char)
        words.append(string)
    # print(words)
    return words


def generate_passwords(word_set, multiply: bool = False, multiplier: int = 2, numbers: bool = False, symbols: bool = False, max_chars_added: int = 8):
    words = set({})
    for word in word_set:
        words.add(word)
        if numbers and symbols:
            for w in randomize_string(string=word, type="all", count=ceil(max_chars_added/2)):
                words.add(w)
            for w in randomize_string(string=word, type="numbers", count=max_chars_added):
                words.add(w)
            for w in randomize_string(string=word, type="symbols", count=max_chars_added):
                words.add(w)
        elif numbers:
            for w in randomize_string(string=word, type="numbers", count=max_chars_added):
                words.add(w)
        elif symbols:
            for w in randomize_string(string=word, type="symbols", count=max_chars_added):
                words.add(w)
    print(len(word_set))
    print(len(words))
    if multiply:
        multiplied = set({})
        for word in words:
            temp = word
            for i in range(multiplier-1):
                temp += choice(tuple(words))
                multiplied.add(temp)
    print(len(words)+len(multiplied))
    with open("passwords.txt", "w") as file:
        for word in words:
            file.write(word+"\n")
        for word in multiplied:
            file.write(word+"\n")


word_list = []
with open("words-from-api.txt", "r") as file:
    count = 0
    for line in file.readlines():
        count+=1
        # :-1 removes the \n at the end
        word_list.append(line[:-1])
        # print(line[:-1])
print(word_list)

generate_passwords(word_set=word_list, numbers=True, symbols=True, multiply=True, multiplier=4)
