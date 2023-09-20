import sys
# sys.stdin = open('input.txt')

def dfs(cnt):
    if cnt == 6:
        if set(example) not in sets:
            sets.append(set(example))
            print(*example)
        return
    for i in range(len(m)):
        if m[i] in example:
            continue
        example[cnt] = m[i]
        dfs(cnt+1)

inputs = []
while True:
    try:
        arr = list(map(int, input().split()))
    except:
        break
    if arr == [0]:
        exit()
    n = arr[0]
    m = arr[1:]
    example = [0]*6
    sets = []
    dfs(0)
    print()