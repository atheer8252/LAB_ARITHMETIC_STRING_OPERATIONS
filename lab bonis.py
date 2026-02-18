sentence = "Learning Python is very useful and Python makes programming easier and more enjoyable."

# Define a word that appears in the sentence
word = "Python"

# Print the length of the sentence
print("Length of sentence:", len(sentence))

# Print the index of the first occurrence of the word
print("First occurrence index:", sentence.find(word))

# Print the number of times the word appears
print("Number of occurrences:", sentence.count(word))

# Print the sentence in all uppercase letters
print("Uppercase:", sentence.upper())

# Print the sentence in all lowercase letters
print("Lowercase:", sentence.lower())

# Replace the word with a new word
new_sentence = sentence.replace(word, "Coding")
print("Replaced sentence:", new_sentence)

# Print the last character of the sentence
print("Last character:", sentence[-1])