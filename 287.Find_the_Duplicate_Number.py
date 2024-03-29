"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = nums[0]
        h = nums[0]
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break
        ptr1 = nums[0]
        ptr2 = t
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
if __name__ == "__main__":
  obj = Solution()
  ans = findDuplicate([1,3,4,2,2])
  print(ans)
  
