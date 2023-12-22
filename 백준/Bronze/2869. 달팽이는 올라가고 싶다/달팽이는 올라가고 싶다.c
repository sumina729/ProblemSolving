#include <stdio.h>
#include  <math.h>
#include <string.h>

/*
문제
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

출력
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
*/

int main(void){

    int A, B, V;
    int num;
    int day = 0;

    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &V);

    /*
    while(1){
        day++;

        cm+=A;
        if(cm >= V){
            break;
        }
        cm-=B;
        if(cm >= V){
            break;
        }
    }
    */

    if (V <= A){
        printf("1");
    }else{
        if ((V-A) % (A-B) == 0){
            printf("%d", (V-A)/(A-B) +1); // (A-B) +1
        }
        else{
            printf("%d", (V-A)/(A-B) +2); // (A-B) +2
        }
        
    }


    return 0;
}