#include <stdio.h>
#include  <math.h>


int main(void){

    int DD, H, W;
    double D;

    scanf("%d", &DD);
    scanf("%d", &H);
    scanf("%d", &W);

    D = sqrt( (H*H) + (W*W));

    
    int HH = H*DD/D;
    int WW = W*DD/D;

    printf("%d %d", HH, WW);

    return 0;
}