plain=input()
key=int(input())

for r in range(len(plain)):
    if plain[r].isdigit():
        plain[r]=str(int(plain[r])+1)
print(plain)