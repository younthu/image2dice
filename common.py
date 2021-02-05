import numpy as np
def rgb2gray( argb):
    return int(0.3*argb[0] + 0.59*argb[1] + 0.11*argb[2])

def six_step_gray(x):
    if (0 <= x and x <= 41):
        return 1;
    if (41 < x and x <= 83):
        return 2;
    if (83 < x and x <= 124):
        return 3;
    if (124 < x and x <= 165):
        return 4;
    if (165 < x and x <= 206):
        return 5;
    if (206 < x and x <= 247):
        return 6;
    else:
        return 6;
#***
#* 一块图片取一个平均灰度值，1-6
#*
def patch2graydot(patch, width, height):
    total = 0
    for i in range(width):
        for j in range(height):
            total += rgb2gray(patch[i][j])
    return six_step_gray(int(total/width/height))

#***
# 图片转换成一个灰度矩阵，每个像素对应一个灰度整数，灰度取之为1-6
#
def patch2graymap(patch, width, height):
    ret = [height][width]
    for i in range(width):
        for j in range(height):
            total += rgb2gray(patch[i][j])
    return six_step_gray(int(total/width/height))

def patch2graymap(patch, width, height):
    ret = np.zeros((width,height), dtype='int32')
    for i in range(width):
        for j in range(height):
            ret[i,j] = rgb2gray(patch[i][j])
    return ret