from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

# threshold function
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x+y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)

# load some images
i = Image.open('images/gimp_face.png', 'r')
iar = np.array(i)

i2 = Image.open('images/gimp_face_muted.png', 'r')
iar2 = np.array(i2)

# reference the figure
fig = plt.figure()
