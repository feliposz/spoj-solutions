/*
SPOJ Problem Set (tutorial)

4138. Harry and big doughnuts

Problem code: DOUGHNUT




Young Harry was asked to buy some foodstuff to his neighbour - weird old lady who owned a lot of fat cats. But cats were weird too and they ate only doughnuts. So the lady wanted Harry to bring exactly one doughnut to each of her pets – and she had c of them. Harry had a rucksack with him but as he was a little boy he could hump only k kilograms. Harry knew that each doughnut weights w kilograms (big cats, big doughnuts). Help him decide whether he should go to supermarket and buy the foodstuff or just give up and dream he could do some magic...

Input

There is a single positive integer t (t <= 100) on the first line of input which corresponds to the number of tests (Harry was asked to buy doughnuts few times). Then t lines follow, each containing three numbers: c, k and w (1 <= c, k, w <= 100).

t [number of tests]
c k w [number of cats, Harry's hoisting capacity and weight of doughnut]
c k w [next test case]
...

Output

t lines containing word “yes” if Harry is capable of handling the task or “no” if doughnuts would cause his spine crack.

Example

Input:
3
5 15 3
1 5 4
13 25 2

Output:
yes
yes
no
*/
#include <stdio.h>

int main()
{
    int t, c, k, w;

    scanf("%d", &t);

    while (t-- > 0) {
        scanf("%d %d %d", &c, &k, &w);
        if (c * w <= k) {
            printf("yes\n");
        } else {
            printf("no\n");
        }
    }

    return 0;
}
