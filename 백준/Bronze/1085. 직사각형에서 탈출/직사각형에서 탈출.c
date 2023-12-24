#include <stdio.h>

//직사각형에서 탈출
int main() {
    int x, y, w, h;
    int gap[4];
    int min=1000;

    scanf("%d %d %d %d", &x, &y, &w, &h);

    gap[0]=y;
    gap[1]=h-y;
    gap[2]=x;
    gap[3]=w-x;

    for(int i=0; i<4; i++){
        if(gap[i]<min){
            min=gap[i];
        }
    }

    printf("%d", min);
    
    return 0;
}