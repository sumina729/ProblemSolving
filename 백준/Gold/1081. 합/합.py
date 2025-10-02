L, U = map(int, input().split())


def digit_sum_upto(n):
    """0 ~ n까지 모든 수의 각 자리수 합"""
    if n < 0:
        return 0
    if n < 10:
        return n * (n + 1) // 2

    # p = 10^k (n의 최상위 자리수 자릿값)
    p = 1
    while p * 10 <= n:
        p *= 10

    msd = n // p   # most significant digit
    r = n % p      # remainder

    # S(10^d - 1) = d * 45 * 10^(d-1)
    d = len(str(p)) - 1
    S_p_minus_1 = d * 45 * (p // 10) if d > 0 else 0

    return (msd * S_p_minus_1
            + (msd * (msd - 1) // 2) * p
            + msd * (r + 1)
            + digit_sum_upto(r))


print(digit_sum_upto(U)-digit_sum_upto(L-1))
