n = int(input())
values = [n]

while n != 1:
    if (n % 2) == 0: 
        n = n/2
    else: 
        n = (n*3)+1
    values.append(int(n))

s = ""

for x in values:
    s += str(x) + " "

print(s[:-1])