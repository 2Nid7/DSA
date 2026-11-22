class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        l_spiral=[]
        total_elements=len(matrix)*len(matrix[0])
        element_count=0
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                l_spiral.append(matrix[top][i])
                element_count+=1
            top+=1
            for i  in range(top,bottom+1):
                l_spiral.append(matrix[i][right])
                element_count+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    l_spiral.append(matrix[bottom][i])
                    element_count+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    l_spiral.append(matrix[i][left])
                    element_count+=1
                left+=1
        return l_spiral
        