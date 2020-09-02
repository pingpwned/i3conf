import os
import sys
from PIL import Image as pil
from scipy.ndimage import gaussian_filter
import imageio

infilename = sys.argv[1]

image = pil.open(infilename)

res = gaussian_filter(image, sigma=2)

imageio.imwrite(infilename, res)

