def count_alpha_in_string(sentence_to_count : str):
    sentence = sentence_to_count.lower()
    letters = set(sentence)
    print(letters)
    highest = (None, 0)
    while letters:
        letter = letters.pop()
        if letter.isalpha():
            count_in_sentence = sentence.count(letter)
            if count_in_sentence > highest[1]:
                highest = (letter, count_in_sentence)
    return highest

print(count_alpha_in_string("Hello there! How are you today?"))

phrase = "Hello there! How are you today?"

# Reinas set solution
def set_solution(line):
    split_line = list(line)
    chr_set = set(split_line)
    most_frequent = ('a', 0)
    for i in chr_set:
        if i.isalpha():
            print(i, split_line.count(i))
            most_frequent = (i, split_line.count(i)) \
                if split_line.count(i) > most_frequent[1] else most_frequent
    return most_frequent


print(f"set solution: {set_solution(phrase)}")