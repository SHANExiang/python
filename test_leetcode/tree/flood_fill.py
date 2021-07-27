

# 图像渲染
# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
#
# 给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
#
# 为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
#
# 最后返回经过上色渲染后的图像。
#
# 示例 1:
#
# 输入:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析:
# 在图像的正中间，(坐标(sr,sc)=(1,1)),
# 在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，
# 因为它不是在上下左右四个方向上与初始点相连的像素点。


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        target = image[sr][sc]
        m, n = len(image), len(image[0])
        destination = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(image, x, y):
            if image[x][y] == target:
                image[x][y] = newColor
                for d in destination:
                    i = d[0] + x
                    j = d[1] + y
                    if 0 <= i < m and 0 <= j < n and image[i][j] == target:
                        dfs(image, i, j)
        if newColor != target:
            dfs(image, sr, sc)
        return image

    def flood_fill(self, image, sr, sc, newColor):
        current_color = image[sr][sc]
        if current_color == newColor:
            return image
        m, n = len(image), len(image[0])
        from collections import deque
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = newColor
        while queue:
            x, y = queue.popleft()
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= i < m and 0 <= j < n and current_color == image[x][y]:
                    queue.append((i, j))
                    image[i][j] = newColor
        return image


