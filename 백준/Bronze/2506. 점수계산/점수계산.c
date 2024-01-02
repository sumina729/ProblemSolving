#include <stdio.h>
#include  <math.h>
#include <string.h>
#include <stdlib.h>

int main(void){

    int N;
    int *num;
    int j=0;
    int jumsu=0;

    scanf("%d", &N);
    num = (int*)malloc(sizeof(int) * N);
    for(int i=0; i<N; i++){
        scanf("%d", &num[i]);
    }

    for(int i=0; i<N; i++){
       if(num[i] == 1 ){
        j++;
       }
       else{
        j=0;
       } 
       jumsu+=j;
    }
    printf("%d", jumsu);

        
    


    return 0;
}