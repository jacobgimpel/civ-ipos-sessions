def letter_count(string):
    output = {}
    for letter in string:
        if not letter.isalpha():
            continue
        letter = letter.lower()
        if letter not in output.keys():
            output[letter] = 1
        else:
            output[letter] += 1

    # print(output)
    most_frequent = ''
    for key, value in output.items():
        print(output.items())
        if value == max(output.values()):
            most_frequent = f'< {key}: {value} >'
    return most_frequent


sentence = input('Enter a sentence: ')
print(f'Most frequent: {letter_count(sentence)}')

# Hello there! How are you today?

# Find the most frequent letter (case insensitive)
def most_frequent_letter(text):
    frequency = {}
    for char in text.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return max(frequency, key=frequency.get)

print("Most frequent letter:", most_frequent_letter("Hello there! How are you today?"))