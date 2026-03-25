class Solution(object):
    def sortArray(self, nums):
        def merg_sort(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=merg_sort(arr[:mid])
            right=merg_sort(arr[mid:])
            return merg(left,right)
        def merg(left,right):
            result=[]
            i=j=0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return merg_sort(nums)

        
        