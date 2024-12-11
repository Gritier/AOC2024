import re

def get_input(file="input.txt"):
    with open(file, "r") as f:
        return f.read().splitlines()

def analyze_memory(memory):
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)

def advanced_analysis(memory):
    pattern = r"(do\(\)|don't\(\))|mul\(\d{1,3},\d{1,3}\)"
    return re.finditer(pattern, memory)

def multiply(mul):
    factors = [int(number) for number in mul.replace("mul(","").replace(")","").split(",")]
    return factors[0]*factors[1]

def part_two():
    input = get_input("input.txt")
    total = 0
    context = "do"
    for memory in input:
        matches = advanced_analysis(memory)
        category = {
            "do":[],
            "don't":[]
        }

        for match in matches:
            value = match.group()
            if "do()" in value:
                context = "do"
            elif "don't()" in value:
                context = "don't"
            else:
                category[context].append(value)

        for mul in category["do"]:
            total += multiply(mul)

    print(total)

def main():
    input = get_input()
    total = 0
    for el in input:
        mul = analyze_memory(el)
        for m in mul:
            total += multiply(m)
    print(total)
    part_two()

main()
