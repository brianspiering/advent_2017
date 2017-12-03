"Utilities for Advent of Code"

def load_data(day):
    try: 
        with open(f'data/day_{day}.txt') as f:
            data = f.read().splitlines()
        return data
    except FileNotFoundError:
        print(f"Go to the Adevent of Code website and manually save this day's data: http://adventofcode.com/2017/day/{day}/input")
        