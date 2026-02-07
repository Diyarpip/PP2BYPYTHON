n = int(input())

doramas = {} 

for _ in range(n):
    s, k = input().split()
    k = int(k)
    
    if s in doramas:
        doramas[s] += k
    else:
        doramas[s] = k


for name in sorted(doramas):
    print(name, doramas[name])
