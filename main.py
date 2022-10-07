

chaine = input("type a sentence")

def word_count(words):
    words = len(words.split(" "))

    return words

final = word_count(chaine)
print(final)