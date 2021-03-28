def cq(t):
    global q, n, sr, c, ci
    ci += 1
    if t < n:
        for q[t] in range(0, n):
            for tt in range(t - 1, -1, -1):
                if q[t] == q[tt] or abs(q[t] - q[tt]) == (t - tt):
                    break
            else:
                cq(t + 1)
    elif n > 0:
        c += 1
        if sr:
            for tt in range(0, n - 1):
                print('{}{}, '.format(chr(tt + 65), q[tt] + 1), end='')
            else:
                print('{}{}'.format(chr(n - 1 + 65), q[n - 1] + 1))


import sys

q = []
n = int(input('n='))
for t in range(0, n):
    q.append(0)
if len(sys.argv) > 1:
    sr = False
else:
    sr = True
c = 0
ci = 0
print('Подождите, идет поиск вариантов.')
cq(0)
print('n={}\nВсего вариантов = {}\nВызов функции  = {}'.format(n, c, ci))
