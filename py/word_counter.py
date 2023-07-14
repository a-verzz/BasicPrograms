def count_words(sentence):
    words = sentence.split()  # Split the sentence into words using whitespace as the delimiter
    return len(words)

# Count the number of words in a sentence or paragraph
sentence = input("Enter a sentence or paragraph: ")
word_count = count_words(sentence)

print("Word count:", word_count)