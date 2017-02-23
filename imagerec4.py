from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('images/gimp_face.png')
iar = np.asarray(i)

plt.imshow(iar) # shows image
print iar
plt.show()  # for drawing matplotlib entities