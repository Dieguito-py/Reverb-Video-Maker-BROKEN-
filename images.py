from sys import prefix
from wand.image import GRAVITY_TYPES, Image
# from gradient_generator import generate_gradient
from wand import image
from wand.drawing import Drawing
from wand.color import Color
import os
import random
import input
import shutil
import letras
import image1

# image = generate_gradient(1920, 1080)
# with open(input.msc+'.png', 'wb') as f:
# 	f.write(image.getbuffer())
# source = 'C:\\Users\\User\\Documents\\code\\vmsv\\'+input.msc+'.png'
# destination = 'C:\\Users\\User\\Documents\\code\\vmsv\\gradients\\'+input.msc+'.png'
# shutil.move(source,destination) 

def ma():
    nya = Image(filename ='C:\\Users\\user\\Documents\\code\\vmsv\\banco de imagens\\'+image1.random_file)
    na = Image(filename ='C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+image1.random_file)
    nya.transform(resize='x531')
    na.blur(sigma = 10)
    na.brightness_contrast(int(-15), int(-10), 'composite_channels')
    na.resize(886,531)
    na.composite(nya, gravity='center')
    na.save(filename='C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+'new'+image1.random_file)
    os.remove('C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+image1.random_file)
    source = 'C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+'new'+image1.random_file
    destination = 'C:\\Users\\User\\Documents\\code\\vmsv\\imagenseditadas\\'+'new'+image1.random_file
    shutil.move(source,destination) 
def ra():
    na = Image(filename ='C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+image1.random_file)
    na.resize(886,531)
    na.save(filename='C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+'new'+image1.random_file)
    os.remove('C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+image1.random_file)
    source = 'C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+'new'+image1.random_file
    destination = 'C:\\Users\\User\\Documents\\code\\vmsv\\imagenseditadas\\'+'new'+image1.random_file
    shutil.move(source,destination) 

ny = Image(filename ='C:\\Users\\User\\Documents\\code\\vmsv\\banco de imagens\\'+image1.random_file)
print(ny.height, ny.width)
if ny.height>ny.width:
    ma()
elif ny.height==ny.width:
    ma()
elif    ny.height<ny.width:
    ra()

ply = Image(filename=r"C:\Users\User\Documents\code\vmsv\imagenseditadas\loop.png")
img = Image(filename='C:\\Users\\User\\Documents\\code\\vmsv\\imagenseditadas\\'+'new'+image1.random_file)
with Image(filename ='C:\\Users\\User\\Documents\\code\\vmsv\\gradients\\'+input.msc+'.png') as canvas:
    with Drawing() as context:
        context.font = r"C:\Users\User\Documents\fonts\Louis George Cafe.ttf"
        context.fill_color = Color('black')
        context.stroke_color = Color('black')
        context.font_style = 'italic'
        context.font_size = 104
        context.text(x=517,y=699,body=letras.title)
        context(canvas)
        context.font = r"C:\Users\User\Documents\fonts\Louis George Cafe Light.ttf"
        context.fill_color = Color('black')
        context.stroke_color = Color('black')
        context.font_style = 'italic'
        context.font_size = 70
        context.text(x=517,y=799,body=letras.slug)
        context(canvas)
        canvas.format = "png"
        canvas .composite(img, left=517, top=53)
        canvas .composite(ply, left=594, top=873)
    canvas.save(filename='C:\\Users\\User\\Documents\\code\\vmsv\\imagemvideo\\'+input.msc+'new.png')