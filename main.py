def sort_sentence(sentence):
    sentence = sentence.split()
    sentence.sort(key=len)
    sentence = ' '.join(sentence)
    print(sentence.capitalize())
sort_sentence(sentence)