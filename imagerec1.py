from PIL import Image
import numpy as np

i = Image.open('images/gimp_face.png', 'r')
iar = np.asarray(i) #array makes a copy, asarray only makes a copy when necessary.

print iar

