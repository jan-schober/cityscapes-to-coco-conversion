import cv2


img = cv2.imread('test.png')

t_l_x = 1731
t_l_y = 397
width = 312
height = 269

top_left = (t_l_x, t_l_y)
bot_right = (t_l_x+width, t_l_y+height)

img_rec = cv2.rectangle(img, top_left, bot_right, color = (0, 255, 0), thickness = 2)

cv2.imshow('test', img_rec)
cv2.waitKey(0)
