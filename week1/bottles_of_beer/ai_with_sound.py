from time import sleep
import sys

TOTAL_BOTTLES = 99

def print_with_beat(text, beat_pattern, base_delay=0.05):
    """
    Print text following a musical beat pattern
    beat_pattern: list of multipliers for base_delay
    """
    chars = list(text.replace(' ', '•'))  # Use bullet for spaces to show rhythm

    for i, char in enumerate(chars):
        if char == '•':
            print(' ', end='', flush=True)
        else:
            print(char, end='', flush=True)

        if i < len(beat_pattern):
            sleep(base_delay * beat_pattern[i])
        else:
            sleep(base_delay)
    print()

def countdown_effect(number):
    """Add dramatic countdown for low numbers"""
    if number <= 5:
        for i in range(3):
            print("♪", end='', flush=True)
            sleep(0.2)
        print(" ", end='')

def main():
    bottles = TOTAL_BOTTLES

    # Musical beat patterns (1.0 = normal, 2.0 = twice as long, 0.5 = half time)
    # These patterns can be adjusted to match the actual song rhythm
    verse_beat = [1.0, 0.8, 1.2, 0.8, 1.5, 0.8, 1.0, 0.8, 2.0]  # "99 bottles of beer"
    action_beat = [1.0, 0.8, 1.0, 0.8, 1.5, 0.8, 1.0, 0.8, 2.5]  # "Take one down"
    ending_beat = [1.2, 0.8, 1.0, 0.8, 1.5, 0.8, 1.0, 0.8, 3.0]  # Final line

    while bottles > 0:
        # Visual separator
        print("\n" + "🍺" * 20)
        countdown_effect(bottles)

        # Verse line 1
        line1 = f"{bottles} bottles of beer on the wall, {bottles} bottles of beer."
        print_with_beat(line1, verse_beat, 0.06)
        sleep(1.0)

        # Verse line 2
        print_with_beat("Take one down, pass it around,", action_beat, 0.05)
        sleep(0.8)

        bottles -= 1

        # Verse line 3
        line3 = f"{bottles} bottles of beer on the wall."
        print_with_beat(line3, ending_beat, 0.07)

        # Special effects for milestone numbers
        if bottles in [50, 25, 10, 5, 1]:
            print(f"\n🎉 Only {bottles} bottles left! 🎉")
            sleep(0.5)

        sleep(2.0 if bottles > 10 else 3.0)  # Longer pauses near the end

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🎵 Song interrupted! Thanks for listening! 🎵")
