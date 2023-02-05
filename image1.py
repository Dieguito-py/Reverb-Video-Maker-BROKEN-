from PIL import Image, ImageDraw, ImageColor
import scipy
import scipy.misc
import scipy.cluster
import binascii
import numpy as np
import os, random
import input



random_file=random.choice(os.listdir(r'C:\Users\User\Documents\code\vmsv\banco de imagens'))
print (random_file)


NUM_CLUSTERS = 5
print('reading image')
im = Image.open('C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+random_file)
im = im.resize((150, 150))      
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

print('finding clusters')
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
print('cluster centres:\n', codes)

vecs, dist = scipy.cluster.vq.vq(ar, codes)         
counts, bins = scipy.histogram(vecs, len(codes))    

index_max = scipy.argmax(counts)                    
peak = codes[index_max]
colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
print(colour)

hex = "#"+colour
aa = ImageColor.getcolor(hex, "RGB")
im = Image.new('RGB', (1920, 1080), aa)
draw = ImageDraw.Draw(im)

im.save('C:\\Users\\User\\Documents\\code\\vmsv\\gradients\\'+input.msc+'.png', quality=95)