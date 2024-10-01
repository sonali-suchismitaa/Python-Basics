import cv2
import os

source = r"C:\Users\KIIT\Desktop\Machine Learning\Python\Projects\hehe.jpeg"
destination = "new.png"
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

if src is None:
    print("Error: Image not loaded. Check the file path.")
else:
    cv2.imshow("title", src)

    scale_percent = 50

    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    dsize = (width, height)

    output = cv2.resize(src, dsize)

    cv2.imwrite(destination, output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
