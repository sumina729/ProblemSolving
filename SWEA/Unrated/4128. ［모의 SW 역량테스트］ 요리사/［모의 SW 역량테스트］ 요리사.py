'''
두 명의 손님에게 음식을 제공하려고 한다.
두 명의 손님은 식성이 비슷하기 때문에, 최대한 비슷한 맛의 음식을 만들어 내야 한다.

N개의 식재료가 있다.
식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)

이때, 각각의 음식을 A음식, B음식이라고 하자.
비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분해야한다.

음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다르게 된다.
식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생한다. (1 ≤ i ≤ N, 1 ≤ j ≤ N, i ≠ j)
각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합이다.

식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고, 가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때, 두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 그 최솟값을 정답으로 출력하는 프로그램을 작성하라.

'''


# import sys
# sys.stdin = open("input.txt", "r")


def cal(mat_list):
    global N, match
    mat = list(mat_list)
    cnt = 0

    for i in range(N//2):
        for j in range(N // 2):
            cnt+= match[mat[i]][mat[j]]

    return cnt
def devide_2(mat_list1):
    global N, ans
    mat_list2 = set()

    for i in range(N):
        if not i in mat_list1:
            mat_list2.add(i)

    cnt1 = cal(mat_list1)
    cnt2 = cal(mat_list2)
    
    ans = min(ans, abs(cnt1-cnt2))


def dfs(cnt, mat_list, sn):
    global N

    if cnt == N//2:
        # print(mat_list)
        devide_2(mat_list)
        return

    for i in range(sn, N):
        mat_list.add(i)
        dfs(cnt+1, mat_list, i+1)
        mat_list.remove(i)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    match = [list(map(int, input().split())) for _ in range(N)]
    ans = int(2e9) #무한대


    # 두 분류로 어떻게 나눌 건지 조합 구하기 (dfs)
    mat_list = set()
    dfs(0, mat_list, 0)

    # 각각에 분류에 따라 그 분류에 따라 맛 구하기
    # 차이 게산해서 차이랑 분류 저장하기
    
    print("#", end="")
    print(test_case, end=" ")
    print(ans)

