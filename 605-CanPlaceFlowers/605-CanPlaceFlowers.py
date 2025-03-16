class Solution:
    def noFlowerLeft(self,flowerbed,index):

        if index == 0 or flowerbed[index-1] == 0:
            return True
        else:
            return False
        
    def noFlowerRight(self,flowerbed,index):

        if index == (len(flowerbed)-1) or flowerbed[index+1] == 0:
            return True
        else:
            return False

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count  = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and self.noFlowerLeft(flowerbed,i) and self.noFlowerRight(flowerbed,i):
                count += 1
                flowerbed[i] = 1

        return count >= n
            
        