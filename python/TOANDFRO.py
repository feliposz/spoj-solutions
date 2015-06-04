"""SPOJ Problem Set (classical)
http://www.spoj.com/problems/TOANDFRO/

400. To and Fro

Problem code: TOANDFRO

Mo and Larry have devised a way of encrypting messages. They first decide secretly on the number of columns and write the message (letters only) down the columns, padding with extra random letters so as to make a rectangular array of letters. For example, if the message is “There’s no place like home on a snowy night” and there are five columns, Mo would write down

t o i o y
h p k n n
e l e a i
r a h s g
e c o n h
s e m o t
n l e w x

Note that Mo includes only letters and writes them all in lower case. In this example, Mo used the character ‘x’ to pad the message out to make a rectangle, although he could have used any letter. Mo then sends the message to Larry by writing the letters in each row, alternating left-to-right and right-to-left. So, the above would be encrypted as

toioynnkpheleaigshareconhtomesnlewx

Your job is to recover for Larry the original message (along with any extra padding letters) from the encrypted one.

Input

There will be multiple input sets. Input for each set will consist of two lines. The first line will contain an integer in the range 2...20 indicating the number of columns used. The next line is a string of up to 200 lower case letters. The last input set is followed by a line containing a single 0, indicating end of input.

Output

Each input set should generate one line of output, giving the original plaintext message, with no spaces.

Example

Input:

5
toioynnkpheleaigshareconhtomesnlewx
3
ttyohhieneesiaabss
0

Output:

theresnoplacelikehomeonasnowynightx
thisistheeasyoneab
"""


def test():
    assert decrypt(5, "toioynnkpheleaigshareconhtomesnlewx") == "theresnoplacelikehomeonasnowynightx", "Test 1 failed"
    assert decrypt(3, "ttyohhieneesiaabss") == "thisistheeasyoneab", "Test 2 failed"
    assert "helloworldab" == decrypt(2, crypt(2, "helloworldab")), "Test 3 failed"
    assert "helloworldab" == decrypt(3, crypt(3, "helloworldab")), "Test 4 failed"
    assert "helloworldabcde" == decrypt(5, crypt(5, "helloworldabcde")), "Test 4 failed"
    print("All tests passed.")

def crypt(size, s):
    assert len(s) % size == 0, "Lenght of string must be a multiple of size."

    step = len(s) // size

    u = ""
    for i in range(step):
        for j in range(len(s)//step):
            if i % 2 == 0:
                k = i + j * step
            else:
                #k = i + (size - i - 1) * step
                k = i + (size - j - 1) * step
            u += s[k]

    return u

def decrypt(size, s):
    t = ""
    for i in range(len(s)//size):
        v = s[i*size:(i+1)*size]
        if i % 2 == 1:
            v = list(v)
            v.reverse()
            v = "".join(v)
        t += v
    u = ""
    for i in range(size):
        for j in range(len(s)//size):
            u += t[i+j*size]
    return u

##if __name__ == "__main__":
##    while True:
##        size = int(input())
##        if size == 0:
##            break
##        s = input()
##        print(decrypt(size, s))
##

test()