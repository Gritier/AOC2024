import re

def get_input(file="input.txt"):
    with open(file, "r") as f:
        return f.read().splitlines()

def analyze_memory(memory):
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)

def advanced_analysis(memory):
    pattern = r"(do\(\)|don't\(\))|mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, memory)

def multiply(mul):
    factors = [int(number) for number in mul.replace("mul(","").replace(")","").split(",")]
    return factors[0]*factors[1]
 
def main():
    input = get_input()
    total = 0
    for el in input:
        mul = analyze_memory(el)
        for m in mul:
            total += multiply(m)
    print(total)

#main()

def test():
    input = get_input("example.txt")
    total = 0
    for memory in input:
        matches = advanced_analysis(memory)
        print(matches)
        
        context = "do"
        category = {
            "do":[],
            "don't":[]
        }

        for match in matches:
            print(match)
            if match[0] and ("do" in match[0] or "don't" in match[0]):
                context = "do" if "do" in match[0] else "don't"
            elif match[1]:
                category[context].append(match[1])
        
        for mul in category["do"]:
            total += multiply(mul)
    print(total)



test()
