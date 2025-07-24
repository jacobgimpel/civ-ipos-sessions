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

def bottle_text(count):
    """Return properly formatted bottle text with correct plural/singular"""
    if count == 0:
        return "no more bottles"
    elif count == 1:
        return "1 bottle"
    else:
        return f"{count} bottles"

def main():
    bottles = TOTAL_BOTTLES
    while bottles > 0:
        print()
        print_with_rhythm("\n\n" + "🍺" * min(bottles, 26),
            char_delay=0.01)  # Limit visual bottles to prevent screen overflow

        # First line - slower, more deliberate
        bottle_text_current = bottle_text(bottles)
        print_with_rhythm(
            f"{bottle_text_current.title()} of beer on the wall, {bottle_text_current} of beer.",
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
        print()
        bottles -= 1

        # Third line - concluding, with emphasis
        bottle_text_remaining = bottle_text(bottles)
        print_with_rhythm(
            f"{bottle_text_remaining} of beer on the wall.",
            char_delay=0.05,
            word_pause=0.15,
            end_pause=1
        )

    # Final verse when no bottles are left
    print("\n🍺💔 No more bottles! 💔🍺")
    print_with_rhythm(
        "No more bottles of beer on the wall, no more bottles of beer.",
        char_delay=0.05,
        word_pause=0.10,
        end_pause=0.8
    )

    print_with_rhythm(
        "Go to the store and buy some more,",
        char_delay=0.04,
        word_pause=0.08,
        end_pause=0.6
    )

    print_with_rhythm(
        f"{TOTAL_BOTTLES} bottles of beer on the wall.",
        char_delay=0.05,
        word_pause=0.15,
        end_pause=2.0
    )

    print("\n🎉 The End! 🎉")

if __name__ == "__main__":
    main()
