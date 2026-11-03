class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height)-1
        Area_list = []

        while(left != right):
            if(height[left] < height[right]):
                area = height[left] * (right - left)
                left += 1
                Area_list.append(area)

            elif(height[left] > height[right]):
                area = height[right] * (right - left)
                right -= 1    
                Area_list.append(area)

            else:
                area = height[left] * (right - left)   
                Area_list.append(area)
                left += 1 

        Area_list.sort(reverse=True)
    

        return int(Area_list[0])        

     
Answer = Solution()

heights = [1,7,2,5,4,7,3,6]
Most_area_for_water = Answer.maxArea(heights)  

print(Most_area_for_water)
