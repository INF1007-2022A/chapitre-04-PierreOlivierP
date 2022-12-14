#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    miaou = len(string)
    if miaou%2 == 0:
        return("La fonction contient un nombre de caractères pair.")
    else:
        return("La fonction ne contient pas un nombre de caractères pair.")
    pass


def remove_third_char(string: str) -> str:
    return (string[0:2] + string[3:])
    pass


def replace_char(string: str, old_char: str, new_char: str) -> str:
    a = 0
    for element in string:
        if element == old_char:
            newstring = string[0:a] + new_char + string[a+1:]
        a +=1
    return newstring
    pass


def get_number_of_char(string: str, char: str) -> int:
    i = -1
    for charactere in string:
        if charactere == char:
            i = i+1
    return i

    pass


def get_number_of_words(sentence: str, word: str) -> int:
    i = 0
    a = 0
    b = 0
    for element in sentence:
        a = len(word)

        if sentence[b:b+a] == word:
            i +=1
        if b+a == len(sentence):
            break
        b+=1
    return i
    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
