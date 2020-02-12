def solve(m, n, slices):
    total = 0
    pos = []

    for i in range(n - 1, -1, -1):
        if total + slices[i] <= m:
            total += slices[i]
            pos.append(i)

        if total == m:
            break

    pos.reverse()

    return pos


if __name__ == "__main__":
    m, n = map(int, input().split())
    slices = list(map(int, input().split()))

    pos = solve(m, n, slices)
    print(len(pos))
    print(*pos)
