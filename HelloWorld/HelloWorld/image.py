import numpy as np
import matplotlib.pyplot as plt
import cv2

input_image_path='./../static/images/yaojing-1.jpg'
input_image_rgb = cv2.imread(input_image_path)

# blank_image ='./../static/images/gb.png'
# blank_image_rgb = cv2.imread(blank_image)


blank_image_rgb = np.full((input_image_rgb.shape[0],input_image_rgb.shape[1],input_image_rgb.shape[2]),255)

age = 18
one_num = age//10
two_num = age%10

# 012345678
#0 *** ***
#1 * * * *
#2 *** ***
#3 * * * *
#4 *** ***
#5
points = np.array([[[0,1],[0,2],[0,3],[1,1],[1,3],[2,1],[2,3],[3,1],[3,3],[4,1],[4,3]],
                 [[0,3],[1,3],[2,3],[3,3],[4,3]],
                 [[0,1],[0,2],[0,3],[1,3],[2,1],[2,2],[2,3],[3,1],[4,1],[4,2],[4,3]],
                 [[0,1],[0,2],[0,3],[1,3],[2,1],[2,2],[2,3],[3,3],[4,1],[4,2],[4,3]],
                 [[0,1],[0,3],[1,1],[1,3],[2,1],[2,2],[2,3],[3,3],[4,3]],
                 [[0,1],[0,2],[0,3],[1,1],[2,1],[2,2],[2,3],[3,3],[4,1],[4,2],[4,3]],
                 [[0,1],[0,2],[0,3],[1,1],[2,1],[2,2],[2,3],[3,1],[3,3],[4,1],[4,2],[4,3]],
                 [[0,1],[0,2],[0,3],[1,3],[2,3],[3,3],[4,3]],
                 [[0,1],[0,2],[0,3],[1,1],[1,3],[2,1],[2,2],[2,3],[3,1],[3,3],[4,1],[4,2],[4,3]],
                 [[0,1],[0,2],[0,3],[1,1],[1,3],[2,1],[2,2],[2,3],[3,3],[4,1],[4,2],[4,3]]])



def image_num(num):
    output_image_rgb = np.empty((input_image_rgb.shape[0], 4 * input_image_rgb.shape[1], input_image_rgb.shape[2]))

    for i in range(0, 5):
        line_image_rgb = np.zeros((input_image_rgb.shape[0], input_image_rgb.shape[1], input_image_rgb.shape[2]))
        for j in range(1, 4):
            mark = True;
            for point in points[num:num + 1][0]:
                # print(point)
                if (point[0] == i and point[1] == j):
                    line_image_rgb = np.concatenate((line_image_rgb, input_image_rgb), axis=1)
                    mark = False
                    break
            if (mark):
                line_image_rgb = np.concatenate((line_image_rgb, blank_image_rgb), axis=1)
        output_image_rgb = np.concatenate((output_image_rgb, line_image_rgb), axis=0)
    print(output_image_rgb.shape)
    return output_image_rgb


output_image_rgb_one = image_num(one_num)
output_image_rgb_two = image_num(two_num)
output_image_rgb = np.concatenate((output_image_rgb_one,output_image_rgb_two),axis=1)
border_bottom = np.zeros((input_image_rgb.shape[0], input_image_rgb.shape[1]*8, input_image_rgb.shape[2]))
output_image_rgb = np.concatenate((output_image_rgb, border_bottom), axis=0)
border_left = np.zeros((input_image_rgb.shape[0]*7, input_image_rgb.shape[1], input_image_rgb.shape[2]))
output_image_rgb = np.concatenate((output_image_rgb, border_left), axis=1)
output_image_path = './../static/images/yaojing1.jpg'
cv2.imwrite(output_image_path, output_image_rgb)
