import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT'in i]
#print(events)

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        points.append((x,y))

        if len(points)>=2:
            cv2.line(img, points[-2], points[-1], (255,0,0), 2)

        cv2.imshow('img', img)

#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512,512,3], np.uint8)
cv2.imshow('img', img)
points = []
cv2.setMouseCallback('img', click_event) #****

cv2.waitKey(0)
cv2.destroyAllWindows()