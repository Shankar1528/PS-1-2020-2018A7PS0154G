import numpy as np
from PIL import Image

im = np.array(Image.open('im.jpg').resize((256, 256)))

im_i = 255 - im

Image.fromarray(im_i).save('im_inverse.jpg')
