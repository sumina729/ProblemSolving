#include<stdio.h>
#include<stdlib.h>

int main(){
    float* num; //각 과목의 점수 배열로 사용.
    int N; //과목수
    float max_num=-10; // 가장 높은 점수.
    float sum_num=0; 

    scanf("%d", &N);
    num =(float*)malloc(N*sizeof(int));

    for(int i=0; i<N; i++){
        scanf("%f", &num[i]);
        if(max_num<num[i]){
            max_num=num[i];
        }
    }
 

    for(int i=0; i<N; i++){
        num[i]= num[i]/max_num*100;
        sum_num+=num[i];
    }

    printf("%f", sum_num/N);



}