#include <stdio.h> 


#define SIZE 3

int getGCD(int numArr[]){ 

   int i;
   int j;
   int gcd=1;
   int min=999999;
   int cnt;

   for(i = 0; i < SIZE; i++){
        if(numArr[i] < min){
            min = numArr[i]; 
        } 
   }

   for(i = 2; i <= min; i++){ 
      cnt = 0; 
      for(j = 0; j < SIZE; j++){
        if(numArr[j] % i == 0){
            cnt++; 
        }
      }
      if(cnt == SIZE){
        gcd = i;
      } 
   } 

   return gcd; // 그렇게 마지막에 저장된 공약수를 반환 즉 최대공약수 

} 
int getLCM(int numArr[]){ 

   int i; // 반복을 위한 변수 i는 가장 큰 수의 배수를 나타내기 위해 반복 
   int j; // 반복을 위한 변수 j는 입력된 모든 수를 확인하기 위해 0부터 SIZE-1까지만 반복 
   int lcm=1; // 최소공배수를 저장할 변수 
   int max=0; // 제일 큰 수를 저장할 변수 초기 값을 제일 작은 수로 지정 
   int cnt; // 정확히 나뉘는 값을 세기 위한 변수 

   for(i = 0; i < SIZE; i++){
        if(numArr[i] > max){
            max = numArr[i]; 
        }
   }

   for(i = 1; i < 485101; i++){ 

      cnt = 0; 
      for(j = 0; j < SIZE; j++){
        if((max * i) % numArr[j] == 0){
            cnt++;
        }
      }

      if(cnt == SIZE){ 
        lcm = max*i; // 처음에 저장된 값이 최소공배수 이므로 반복종료 
        break; 
      }
   } 
   

   return lcm; 

} 

int main(void){ 
    int num[5];
    int LCM_num[SIZE];
    int LCM_min = 9999999;
    int LCM;

    for(int i=0; i<5; i++){
        scanf("%d", &num[i]);
    }

    for(int i=0; i<5; i++){
        for(int j=i+1; j<5; j++){
            for(int k=j+1; k<5; k++){
                LCM_num[0] = num[i];
                LCM_num[1] = num[j];
                LCM_num[2] = num[k];
                LCM = getLCM(LCM_num);

                //printf("%d %d %d = %d\n", LCM_num[0], LCM_num[1], LCM_num[2], LCM);

                if(LCM==1){
                    break;
                }
                
                if(LCM<LCM_min){
                    
                    LCM_min = LCM;
                }
            }
        }
    }

    printf("%d", LCM_min);
    
  

    return 0; 
}