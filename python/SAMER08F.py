def test():
    assert squares(2) == 5, "Test 1 passed"
    assert squares(1) == 1, "Test 2 passed"
    assert squares(8) == 204, "Test 3 passed"
    print("All tests passed")

def squares(n):
    if n == 0:
        return 0
    else:
        return n*n + squares(n-1)

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        print(squares(n))

#test()
