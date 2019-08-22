class Solution:
    def getRange(self, arr, target):
        self.star = 0
        self.end = 0
        self.store= []
        for x in range(0, len(arr)):
            if arr[x] == target:
                self.store.append(x)

        self.star = min(self.store)
        self.end = max(self.store)
        return ("starting index = {}, ending index = {}".format(self.star, self.end))

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))

