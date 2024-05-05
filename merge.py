#Importing libraries
from PIL import Image
import math

while True:
    if input("Do you want to merge the files? y/n ") == "y":

#Selecting pictures to merge, number of columns user wants, and the name of the output file 
        pictures=[]
        while True:
            i = input("The name of the picture without file extension (or hit double enter to finish) ")
            if i != "":
                pictures.append(i)
            else:
                break
        output=input("Please entere the name of the merged picture: ")
        columns = int(input("How many pictures should be there horizontally? "))

#Adding file extension to the file
        pictures = [x + ".png" for x in pictures]

#Merging pictures based on https://stackoverflow.com/questions/72723928/how-to-combine-several-images-to-one-image-in-a-grid-structure-in-python
        for image in pictures:
            rows = math.ceil(len(pictures) / columns)
            width_max = max([Image.open(image).width for image in pictures])
            height_max = max([Image.open(image).height for image in pictures])
            background = Image.new('RGBA', (columns*(width_max+1), rows*(height_max+1)), (255, 255, 255, 255))
            x = 0
            y = 0
            for i, image in enumerate(pictures):
                img = Image.open(image)
                x_offset = int((width_max-img.width)/2)
                y_offset = int((height_max-img.height)/2)
                background.paste(img, (x+x_offset, y+y_offset))
                x += width_max 
                if (i+1) % columns == 0:
                    y += height_max
                    x = 0
            background.save(output+".png")
    
    else:
        break