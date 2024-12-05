def get_input(file="input.txt"):
    with open(file, "r") as f:
        return f.read().splitlines()

def verify_report(report):
    if not (all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(report[i] >= report[i + 1] for i in range(len(report) - 1))):
        return 0
    else:
        for i in range(len(report) - 1):
            diff = report[i] - report[i + 1]
            if  diff not in [3,2,1,-1,-2,-3]:
                return 0
    return 1

def full_damp(report):
    for idx,el in enumerate(report):
        temp = list(report)
        temp.pop(idx)
        if verify_report(temp):
            return 1
    return 0

def main():
    input = get_input()
    safe_reports = 0
    for line in input:
        report = [int(value) for value in line.split(" ")]
        if verify_report(report):
            safe_reports += 1
        elif full_damp(report):
            safe_reports += 1
    print(safe_reports)

main()


