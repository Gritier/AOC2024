def read_file(file="input.txt"):
    with open(file, "r") as f:
        return f.readlines()

input = read_file()
left = []
right = []

for line in input:
    l,r = line.split("   ")
    left.append(int(l))
    right.append(int(r))
    
left.sort()
right.sort()

result_p1 = 0

for i in range(len(left)):
    if left[i] < right[i]:
        result_p1 += right[i]-left[i]
    else:
        result_p1 += left[i]-right[i]

print(result_p1)

left_dict = {}

for l in left:
    if l not in left_dict.keys():
        left_dict[l] = 0
    for r in right:
        if l == r:
            left_dict[l] += 1

result_p2 = 0

for key in left_dict.keys():
    result_p2 += key*left_dict[key]

print(result_p2)
