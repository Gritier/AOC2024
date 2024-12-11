from functools import cache

def get_input(file="input.txt"):
    with open(file, "r") as f:
        return f.read().splitlines()

@cache
def calculate_stones(value, blinks_remaining):
    while blinks_remaining > 0:
        blinks_remaining -= 1
        if value != 0 and len(str(value))%2!=0 :
            value *= 2024
        elif value == 0:
            value = 1
        elif len(str(value))%2==0:
            str_value = str(value)
            lenght = len(str_value)
            left = int(str_value[:int(lenght/2)])
            right = int(str_value[int(lenght/2):])
            return calculate_stones(left, blinks_remaining) + calculate_stones(right, blinks_remaining)
    return 1

def main():
    input = [int(value) for value in get_input()[0].split(" ")]
    blinks = 75
    stones = 0
    for value in input:
        stones += calculate_stones(value, blinks)
    print(stones)

if __name__ == "__main__": main()
