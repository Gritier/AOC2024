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

def dampener(report):
    direction = 0
    errors = []
    for idx, el in enumerate(report):
        if idx != 0:
            diff = el - report[idx-1]
            if diff < 0 or diff < -3:
                if direction > 0:
                    errors.append(idx)
                    errors.append(idx-1)
                direction = -1
            elif diff > 0 or diff > 3:
                if direction < 0:
                    errors.append(idx)
                    errors.append(idx-1)
                direction = 1
            else:
                errors.append(idx)
                errors.append(idx-1)
                direction = 0
        if len(errors) > 4:
            return 0
    for error in errors:
        temp = list(report)
        temp.pop(error)
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
        elif dampener(report):
            safe_reports += 1
    print(safe_reports)

main()

def test():
    input = get_input()
    safe = 0

    for line in input:
        errors = []
        report = [int(value) for value in line.split(" ")]
        for i in range(len(report)-1):
            diff = report[i] - report[i+1]
            if diff not in [-3, -2, -1, 1, 2, 3]:
                error.append((i,i+1))


#test()


