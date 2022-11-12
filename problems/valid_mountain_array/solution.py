class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3 or arr[1] < arr[0]:
            return False
        if len(arr) == 3:
            if arr[0] < arr[1] and arr[1] > arr[2]:
                return True
            else:
                return False
            
        max = arr[0]
        min = None
        
        stop_index = None
        
        for i in range(1, len(arr)):
            if arr[i] == max:
                return False
            elif arr[i] > max:
                max = arr[i]
            elif arr[i] < max:
                min = arr[i]
                stop_index = i
                break
        
        if i == arr[-1]:
            return False
        
        for i in range(stop_index + 1, len(arr)):
                if arr[i] >= min:
                    return False
                else:
                    min = arr[i]
                    
        return True
        
                