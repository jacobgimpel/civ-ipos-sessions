# Activity 1
# What are the major step to solving the task?
# some kind of algorithm

def most_frequent_letter(text):
    # TODO need a count starting point of zero
    max_count = 0
    most_frequent = ''

    # TODO we will need to change the letter to lowercase
    text_lower = text.lower()

    # TODO these letters need to be in a collection we can loop over
    letters = []

    # TODO break the string into letters
    for letter in text_lower:
        letters.append(letter)

    # TODO our loop structure checks each letter
    for i in range(len(letters)):
        # TODO we will need to check the current letter is a member of the alphabet
        # TODO store the count change somehow
        count = 0
        current_letter = letters[i]
        # pass
        for j in range(len(letters)):
            # TODO add 1 if the letter is equal or found
            if letters[j] == current_letter:
                count += 1
            # TODO once we have completed the loop find the largest
            if count > max_count:
                max_count = count
                most_frequent = current_letter

    return most_frequent

mystring = "Hello there! How are you today?"
print(f"Most frequent letter is: {most_frequent_letter(mystring)}")