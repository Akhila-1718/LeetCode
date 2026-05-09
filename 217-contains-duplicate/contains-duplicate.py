class Solution(object):
    def containsDuplicate(self, nums):
        hashmap={}
        for n in nums:
            if n in hashmap:
                return True
            else:
               hashmap[n]=1
        return False

           