#include <stdio.h>
#include  <math.h>
#include <string.h>

int main(void){

    long N, M;
    long sum;
    
    scanf("%ld", &N);
    scanf("%ld", &M);
    
    sum = N-M;
    //printf("sum = N+M -> %d", sum);

    if(sum<0){
        printf("%ld", 0-sum);
    }
    else{
        printf("%ld", sum);
    }

    return 0;
}