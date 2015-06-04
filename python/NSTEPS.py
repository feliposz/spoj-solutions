def plot(width, height):
    for j in range(height):
        y = height - j - 1
        print("y = {0:3} |".format(y), end="")
        for x in range(width):
            print("{0:3}".format(f(x,y)), end="")
        print()

    print("        +", end="")
    for x in range(width):
        print("---", end="")
    print()

    print("         ", end="")
    for x in range(width):
        print("{0:3}".format(x), end="")
    print()

def f(x, y):
    if x == y:
        if x % 2 == 0:
            return x + y
        else:
            return 1 + f(x-1, y-1)
    elif x - 2 == y:
        return f(x, y + 2) - 2
    return ""

def test():
    assert f(4, 2) == 6, "Test 1 failed"
    assert f(6, 6) == 12, "Test 2 failed"
    assert f(3, 4) == "", "Test 3 failed"
    print("All tests passed")

if __name__ == '__main__':
    lines = int(input())
    for i in range(lines):
        x, y = input().split()
        n = f(int(x), int(y))
        if n == "":
            print("No Number")
        else:
            print(n)

#plot(20, 20)
