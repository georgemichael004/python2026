# Task: Count the frequency of each word in a sentence.
def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    return word_count

print(count_words("This is a sample sentence. This sentence is a sample."))
