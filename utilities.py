"Utilities for Advent of Code"

def load_data(day, split=False):
    try: 
        with open(f'data/day_{day}.txt') as f:
            if split:
                return [line.strip() for line in f.readlines()]
            else:
                return f.read().strip()
    except FileNotFoundError:
        print(f"Go to the Adevent of Code website and manually save this day's data: http://adventofcode.com/2017/day/{day}/input")
        

cat = ''.join