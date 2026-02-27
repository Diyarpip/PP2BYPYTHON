
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield str(i)

def solve():
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
        print(",".join(even_generator(n)))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()