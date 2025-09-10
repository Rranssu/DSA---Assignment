import string

def remove_punctuation(sentence: string) -> string:
    newSentence = str.maketrans('', '', string.punctuation)
    return sentence.translate(newSentence)

sent = input("Type A sentence: ")
print(remove_punctuation(sent))