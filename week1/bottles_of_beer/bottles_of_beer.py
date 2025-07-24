from time import sleep

TOTAL_BOTTLES = 99

def main():
    bottle_or_bottles = "bottle"
    for bottles in range(TOTAL_BOTTLES, 0, -1):
        print("\n" + "🍺" * bottles)

        for c in f"{bottles} {bottle_or_bottles} of beer on the wall, {bottles} bottles of beer.":
            print(c, end='', flush=True)
            sleep(0.08)
        print()
        for c in "Take one down, pass it around,":
            print(c, end='', flush=True)
            sleep(0.1)
        bottles -= 1
        bottle_or_bottles = "bottle" if bottles == 1 else "bottles"
        print()
        sleep(0.05)
        for c in f"{bottles} {bottle_or_bottles} of beer on the wall.":
            print(c, end='', flush=True)
            sleep(0.05)
        print()
        sleep(1)
    else:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, {TOTAL_BOTTLES} bottles of beer on the wall.")


if __name__ == "__main__":
    main()
