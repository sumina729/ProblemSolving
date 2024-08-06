n = int(input())

number = 0
tmp_g = 0
while(True):
    if(tmp_g > n): break
    tmp_g+=5
    number+=1

while(True):
    tmp_g-=5
    number-=1
    if(tmp_g<0):
        num = -1
        break

    if (n-tmp_g)%3==0: 
        number = number +((n-tmp_g)/3)
        break

print(int(number))