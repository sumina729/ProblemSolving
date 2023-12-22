#include <stdio.h> 

/*
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
*/

//최소공약수 최대공약수 리뷰
#define SIZE 2

int getGCD(int numArr[]){ 

   int i;
   int j;
   int gcd=1;
   int min=10001;
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

   for(i = 1; i <= 100000000; i++){ 

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
    int num[SIZE];

    for(int i=0; i<SIZE; i++){
        scanf("%d", &num[i]);
    }

    printf("%d\n", getGCD(num));
    printf("%d\n", getLCM(num));


    
  

    return 0; 
}