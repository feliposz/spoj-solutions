"""SPOJ Problem Set (classical)

4300. Rectangles

Problem code: AE00




Byteman has a collection of N squares with side 1. How many different rectangles can he form using these squares?

Two rectangles are considered different if none of them can be rotated and moved to obtain the second one. During rectangle construction, Byteman can neither deform the squares nor put any squares upon any other ones.

Input

The first and only line of the standard input contains one integer N (1 ≤ N ≤ 10000).

Output

The first and only line of the standard output should contain a single integer equal to the number of different rectangles that Byteman can form using his squares.

Example

For the input data:

6
the correct result is:

8

# ## ####

## ## # #
## ## # #
   ## # #
        #
######  #

Task author: Jakub Radoszewski.
"""

"""
Meus estudos...

# ## ### #### ##### ######

# ## ### #### ##### ######
  ## ### #### ##### ######
     ### #### ##### ######
         #### ##### ######
              ##### ######
                    ######

n = 20

retangulos de lado 1 = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20...

retangulos de lado 2 = 4 6 8 10 12 14 16 18 20 ...

retangulos de lado 3 = 9 12 15 18 21 ...

retangulos de lado 4 = 16 20 24 ...

retangulos de lado 5 = 25 30 35 ...

retangulos de lado 6 = 36 42 48 ...

...
"""

# original
def rectangles(n):
    count = n
    for i in range(2, n+1):
        x = i*i
        while x <= n:
            count += 1
            x += i
    return count

# melhorada
#  - os retangulos com lado maior que 1, são uma progressão geométrica
#  - com fator f
#  - primeiro termo p (quadrado de f)
#  - último termo u é o maior retangulo possível de área <= n
#  - o loop testa todos os quadrados de lado sqrt(n) + 1 e calcula a quantidade de respectivos retangulos
def rectangles2(n):
    count = n
    for f in range(2, int(n**0.5) + 1):
##        p = f * f
##        u = (n // f) * f
##        q = (u - p) // f + 1
        q = ((n // f) - f ) + 1
        count += q
    return count

def test():
    for i in range(1, 2000):
        a = rectangles(i)
        b = rectangles2(i)
        if (a != b):
            print(i, a, b)
            return
    print("tests passed")

#print(rectangles2(int(input())))
test()
