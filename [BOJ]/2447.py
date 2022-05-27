def star(x):
    if x == 1:
        return '*'
    else:
        s = star(x // 3)
        l = []

        for i in s:
            l.append(i * 3)
        for i in s:
            l.append(i + ' '*(x//3) + i)
        for i in s:
            l.append(i * 3)
        return l


n = int(input())
print('\n'.join(star(n)))