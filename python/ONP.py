
# Convert algebraic infix notation to revese polish notation (postfix)
def infixToPostfix(expr):
    rpn = ""
    stack = []
    oper = "(+-*/^"
    for e in expr:
        if e.lower() >= "a" and e <= "z":
            rpn += e
        elif e == ")":
            while len(stack) > 0:
                op = stack.pop()
                if op == "(":
                    break
                rpn += op
        elif e == "(":
            stack.append(e)
        else:
            while len(stack) > 0 and oper.index(stack[-1]) > oper.index(e):
                rpn += stack.pop()
            stack.append(e)
    while len(stack) > 0:
        rpn += stack.pop()
    return rpn

def test():
    assert infixToPostfix("(a+(b*c))") == "abc*+", "Test 1 failed"
    assert infixToPostfix("((a+b)*(z+x))") == "ab+zx+*", "Test 2 failed"
    assert infixToPostfix("((a+t)*((b+(a+c))^(c+d)))") == "at+bac++cd+^*", "Test 3 failed"
    print("All tests passed.")

if __name__ == "__main__":
    lines = int(input())
    for i in range(lines):
        print(infixToPostfix(input()))

