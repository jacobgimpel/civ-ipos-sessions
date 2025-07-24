from time import sleep

TOTAL_BOTTLES = 99

def print_with_rhythm(text, char_delay=0.08, word_pause=0.2, end_pause=0.5):
    """Print text with musical timing"""
    words = text.split()
    for i, word in enumerate(words):
        for char in word:
            print(char, end='', flush=True)
            sleep(char_delay)
        if i < len(words) - 1:  # Don't pause after the last word
            print(' ', end='', flush=True)
            sleep(word_pause)
    print()
    sleep(end_pause)

def main():
    bottles = TOTAL_BOTTLES
    while bottles > 0:
        print("\n🍺" * bottles)
        # First line - slower, more deliberate
        print_with_rhythm(
            f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.",
            char_delay=0.05,
            word_pause=0.10,
            end_pause=0.8
        )

        # Second line - slightly faster, more conversational
        print_with_rhythm(
            "Take one down, pass it around,",
            char_delay=0.04,
            word_pause=0.08,
            end_pause=0.6
        )

        bottles -= 1

        # Third line - concluding, with emphasis
        print_with_rhythm(
            f"{bottles} bottles of beer on the wall.",
            char_delay=0.05,
            word_pause=0.15,
            end_pause=1
        )

if __name__ == "__main__":
    main()
