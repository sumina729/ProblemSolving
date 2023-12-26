#include <stdio.h>
#include  <math.h>
#include <string.h>

int main(void){

    int N;
    int b,s;
    
    scanf("%d", &N);
    b = 0;
    s = N;
    

    for(int i=0; i<N; i++){
        /*
        for(int j=0; j<b; j++){
            printf(" ");
        }
        */
        for(int j=0; j<s; j++){
            printf("*");
        }
        printf("\n");
        //b++;
        s--;
    }

    return 0;
}