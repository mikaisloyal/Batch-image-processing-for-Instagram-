#import mandatory libraries/modules
from PIL import Image
import os

#set the dimensions to which you want to crop the image
d=(40,40,1080,1080)

#initialize the path to the watermark image and the pics folder/directory
water=Image.open(r"C:\Users\zhasm\Downloads\PL drafts\watermark.png")
folder = r"C:\Users\zhasm\Downloads\PL drafts\PIL"

#iterate through images in a folder/directory
for img in os.listdir(folder):

    #condition to choose only image files in a folder
    if (img.endswith(".png") or img.endswith(".jpg") or img.endswith(".jpeg")):

        #open image, crop, convert it to black-white and paste a watermark image
        x=Image.open(img)
        y=x.crop(d)
        z=y.convert("L")
        z.paste(water, (825 ,700))

        #save an ediited image in the initial folder with addition of "editted_" to the name of a file
        z.save(str("editted_")+img)
        x.close()



