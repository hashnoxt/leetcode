"""
1012. Numbers With Repeated Digits

Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

 

Example 1:

Input: n = 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: n = 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: n = 1000
Output: 262
 

Constraints:

1 <= n <= 10^9
"""

# Solution

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        if n < 11:
            return 0
        count: int = 0
        number_list: list[int] = [ int(i) for i in str(n) ]
        print(number_list)
        

    def factorial(self,n: int) -> int:

        if n ==0 or n==1:
            return 1
        
        return n * self.factorial(n=n-1)


# Solution().numDupDigitsAtMostN(n = 20)
# Solution().numDupDigitsAtMostN(n = 100)
print(Solution().factorial(n= 3))
Solution().numDupDigitsAtMostN(n = 1000)
