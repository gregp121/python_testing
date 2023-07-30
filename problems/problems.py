class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in nums:
            if nums[i] >= target:
                print("I is: " + i)
                continue
            else:
                x = i + 1
                while x < len(nums):
                    if (nums[i] + nums[x]) == target:
                        print("Value is: ", nums[i] + nums[x])
                        return [nums[i], nums[i + 1]]
                    else:
                        print("X incremented: ", x)
                        x += 1

# testInstance = Solution()
# testInstance.twoSum(nums = [1, 2, 4, 8], target = 6)

# Above we used a brute force. Can we do better?
## Yes: hash tables
            
### 3 billion possible hash codes?

### Collision - two strings get same hash, two hashes are mapped to same index
### Chaining - One collision solution were you put linked list in index

## What is it:    Key => Value lookup (fast lookups)
## For example, a HASH function takes a STRINg and converts it into some INTEGER and remaps that integer into an INDEX in an ARRAY
### Faster because the index value behaves as a key for the data value

## O(1) *Constant time?* for a "good" hashtable
## O(n) *linear time* for a bad hashtable

# class Solution2:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         numMap = {} # Dictionary represent pythons hash table
#         n = len(nums)

#         # Build hash table
#         for i in range(n): # Note: We do have a for loop here, which slows things a little
#             numMap(nums{i}) = i
        
#         for i in range(n):
#             complement = target - nums(i)
#             if complement in numMap and numMap[complement] != i:
#                 return [i, numMap[complement]]
            
class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {} # Dictionary represent pythons hash table
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i # So we build the table as we go?

class romanInteger: # Focus on what matters, order does not
    def romanToInt(self, s: str) -> int:
        intMap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        n = len(s)
        value = 0
        
        for i in range(n):
            if i < (n - 1) and intMap[s[i]] < intMap[s[i+1]]:
                value -= intMap[s[i]] # Since we are using addition/substraction, we can substract this value right away, order doesn't matter
            else:
                value += intMap[s[i]]
    
# testInstance = romanInteger()
# testInstance.romanToInt(s = "IIIVC")

class Pallindrome: # Focus on what matters, order does not
    def pallindrome(self, i: int) -> bool:
        stringX = str(i)
        stringY = stringX[::-1]
        if stringX == stringY:
            print("True")
            return True
        else:
            print("False")
            return False
    
testInstance = Pallindrome()
testInstance.pallindrome(i = 111)