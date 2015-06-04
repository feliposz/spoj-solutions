/*
SPOJ Problem Set (classical)

1025. Fashion Shows

Problem code: FASHION

A fashion show rates participants according to their level of hotness. Two different fashion shows were organized, one for men and the other for women. A date for the third is yet to be decided ;) .

Now the results of both fashion shows are out. The participants of both the fashion shows have decided to date each other, but as usual they have difficuly in choosing their partners. The Maximum Match dating serive (MMDS) comes to their rescue and matches them in such a way that that maximizes the hotness bonds for all couples.

If a man has been rated at hotness level x and a women at hotness level y, the value of their hotness bond is x*y.

Both fashion shows contain N participants each. MMDS has done its job and your job is to find the sum of hotness bonds for all the couples that MMDS has proposed.

Input

The first line of the input contains an integer t, the number of test cases. t test cases follow.

Each test case consists of 3 lines:

The first line contains a single integer N (1 <= N <= 1000).
The second line contains N integers separated by single spaces denoting the hotness levels of the men.
The third line contains N integers separated by single spaces denoting the hotness levels of the women.
All hotness ratings are on a scale of 0 to 10.

Output

For each test case output a single line containing a single integer denoting the sum of the hotness bonds for all pairs that MMDS has proposed.

Example

Input:
2
2
1 1
3 2
3
2 3 2
1 3 2

Output:
5
15
*/

#include <stdio.h>
#include <stdlib.h>

int compareInt(const void* p1, const void* p2)
{
    /*
    if ( *(int*)p1 < *(int*)p2 ) return -1;
    if ( *(int*)p1 == *(int*)p2 ) return 0;
    if ( *(int*)p1 > *(int*)p2 ) return 1;
    */

    return *(int*)p1 - *(int*)p2;
}

int main()
{
    int tests, couples, i, total;
    int men[1000], women[1000];

    scanf("%d", &tests);

    while (tests-- > 0) {
        scanf("%d", &couples);
        for (i = 0; i < couples; i++) {
            scanf("%d", &men[i]);
        }
        for (i = 0; i < couples; i++) {
            scanf("%d", &women[i]);
        }
        qsort((void*) men, couples, sizeof(men[0]), compareInt);
        qsort((void*) women, couples, sizeof(women[0]), compareInt);
        total = 0;
        for (i = 0; i < couples; i++) {
            total += men[i] * women[i];
        }
        printf("%d\n", total);
    }

    return 0;
}
