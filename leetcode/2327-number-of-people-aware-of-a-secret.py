# loop through 0, n
# usign a queue data structure
# if d = n, add one more with add another with d = n + 2 and f = n + 4
# if f = n, deque
# if d > n - 2

def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:

    # p noOfPeopleForgetingSecret = dp[day - forget]
    # q noOfPeopleSharingSecret += noOfNewPeopleSharingSecret - noOfPeopleForgetingSecret
    # r noOfNewPeopleSharingSecret = dp[day - delay]

    mod = 10 ** 9 + 7
    dp = [0] * (n + 1)
    dp[1] = 1
    q = 0

    for i in range(2, n + 1):
        p = dp[max(0, i - forget)]
        r = dp[max(0, i - delay)]
        q += (r - p + mod) % mod

        dp[i] = q

    print(dp)
    ans = 0
    for i in range(n - forget + 1, n + 1):
        ans = (ans + dp[i]) % mod



    return ans


print(peopleAwareOfSecret(6,2,4))