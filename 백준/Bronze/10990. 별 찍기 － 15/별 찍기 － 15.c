#include <stdio.h>
#include  <math.h>
#include <string.h>

int main(void){

    int N;
    int b1, b2,s;
    
    scanf("%d", &N);
    b1 = N-1;
    b2 = 1;
    //s = 1;
    
    for(int j=0; j<b1; j++){
        printf(" ");
    }
    printf("*\n");
    b1--;
    for(int i=0; i<N-1; i++){
        
        //printf("%d %d\n", b1, b2);
        for(int j=0; j<b1; j++){
            printf(" ");
        }
        printf("*");
        for(int j=0; j<b2; j++){
            printf(" ");
        }
        printf("*");
        printf("\n");
        b1--;
        b2+=2;
    }


    return 0;
}