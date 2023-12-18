#include <stdio.h>
#include  <math.h>
#include  <string.h>

/*
문제
영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

입력
첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.

출력
첫째 줄에 단어의 개수를 출력한다.
*/

int main(void){

    char string_n[1000000];
    int chek = 0;
    int num = 0;

    scanf("%[^\n]s", string_n);
    for(int i=0; i<strlen(string_n); i++){
        int b_chek = chek;

        if(string_n[i] != ' '){
            chek = 1;
        }
        else{
            chek = 0;
        }

        if((b_chek == 1 && chek == 0) || (chek == 1 && (strlen(string_n) == i+1))){
            num++;
        }

    }

    printf("%d", num);

    
    return 0;
}