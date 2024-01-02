#include <stdio.h>
#include  <math.h>
#include <string.h>

int main(void){

    int n[3][4];
    int num[3];
    
    
    for(int j = 0; j <3; j++){
        num[j] = 0;
        for(int i=0; i<4; i++){
            scanf("%d", &n[j][i]);
            if(n[j][i] == 0 ){
                num[j]++;
            }
        }

    }
    for(int j = 0; j <3; j++){
        if(num[j] == 1) printf("A\n");
        else if(num[j] == 2) printf("B\n");
        else if(num[j] == 3) printf("C\n");
        else if(num[j] == 4) printf("D\n");
        else printf("E\n");
    }

        
    
    
    
    


    return 0;
}