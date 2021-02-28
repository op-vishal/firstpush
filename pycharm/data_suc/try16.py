import sys
s = sys.stdin.read()
print(s)

for i in s.split('\n'):
    string = i.split(' ')
    if len(string) != 4:
        print('')
    else:
        x, y, a, b = string
        x = int(x)
        y = int(y)
        a = int(a)
        b = int(b)

        if (x * y == a + b):
            print('Yes')
        else:
            print('No')
