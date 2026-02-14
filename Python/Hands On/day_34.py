class Solution:
    def isPrime(self, n):
        # code here
        start=2
        end=n//2
        for divisor in range(start,end):
            if n%divisor==0:
                return 0
            else:
                continue
        return 1

Solution().isPrime(4)