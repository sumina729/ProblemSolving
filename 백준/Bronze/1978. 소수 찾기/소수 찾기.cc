#include <stdio.h>

int main(void) {
  int N;
  int num[100];
  int chek=0; // 소수가 아니면 1.
  int num_n=0;
  

  scanf("%d", &N);
  for(int i=0; i<N; i++){
    scanf("%d", &num[i]);
    if(num[i]==1) continue;
    for(int j=2; j<num[i]; j++){
      if(num[i]==j) continue;
      if(num[i]%j==0){
        chek=1;
      }     
    }

    if(chek==0 || num[i]==2){
      num_n++;
    }
    chek=0;
  }

  printf("%d", num_n);

  
  
  return 0;
}