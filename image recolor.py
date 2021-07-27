import os
import time
import pathlib
import pathlib
import sys
from PIL import Image
import random

def recolor(image,r ,g ,b,filen):

    outputname = "output_"+str(filen)+".jpg"
    bg_img = Image.open(image)
    bg_img = bg_img.convert('RGBA') 
    width, height = bg_img.size 
    foregr_img  = Image.new( mode = "RGBA", size = (width, height) , color = (r, g, b, 127))
    #foregr_img.save("greensample.png")
    newimg = Image.blend(bg_img, foregr_img, alpha=0.5)
    newimg = newimg.convert("RGB")
    newimg = newimg.save(outputname)
    print("Recolored " + str(image))


images = 0 
filepaths = []
dir_path = os.path.dirname(os.path.realpath(__file__))

filelist = os.listdir(dir_path)
for filename in filelist:
    fext = filename.split('.')[-1]
    if fext.lower() in ['png', 'jpg', 'jpeg']:
        images = images + 1
        filepath = os.getcwd() + "\\" + str(filename)
        filepaths.append(filepath)



if(images != 0):
    print("Found " + str(images) + " recolorable images:" )
    for x in range(len(filepaths)):
        print(str(filepaths[x]))

    print("Choose prefered mode:")
    print("1 - recolor to set green value")
    print("2 - recolor each image to a random green sheen")
    print("3 - recolor to set RGB values")
    print("quit - close the program")
    while True:
        j = input("Pick preffered option:")
        if(str(j) == "1"):

            while True:
                green = input("Input a green value between 0 - 255 :")
                try:
                    int(green)
                    if(int(green) > 255 or int(green) < 0):
                        print("Invalid value, please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid value, please try again.")
            
            print("\nContinuing will recolor all files listed above to set rgb values. No files will be replaced or lost. Are you sure you want to proceed?")
            input("Press Enter to continue... (or close the program to stop)")
            for x in range(len(filepaths)):
                recolor(str(filepaths[x]), 0 , int(green) , 0, x)
        elif(str(j) == "2"):
            print("\nContinuing will recolor all files listed above to set rgb values. No files will be replaced or lost. Are you sure you want to proceed?")
            input("Press Enter to continue... (or close the program to stop)")
            for x in range(len(filepaths)):
                recolor(str(filepaths[x]), 0 , random.randrange(90,220), 0, x)
        elif(str(j) == "3"):
            while True:
                red = input("Input a red value between 0 - 255 :")
                try:
                    int(red)
                    if(int(red) > 255 or int(red) < 0):
                        print("Invalid value, please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid value, please try again.")

            while True:
                green = input("Input a green value between 0 - 255 :")
                try:
                    int(green)
                    if(int(green) > 255 or int(green) < 0):
                        print("Invalid value, please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid value, please try again.")

            while True:
                blue = input("Input a blue value between 0 - 255 :")
                try:
                    int(blue)
                    if(int(blue) > 255 or int(blue) < 0):
                        print("Invalid value, please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid value, please try again.")

            print("\nContinuing will recolor all files listed above to set rgb values. No files will be replaced or lost. Are you sure you want to proceed?")
            input("Press Enter to continue... (or close the program to stop)")
            for x in range(len(filepaths)):
                recolor(str(filepaths[x]), int(red) , int(green) , int(blue), x)

        elif(str(j).lower()=="quit"):
            print("Closing...")
            time.sleep(2)
            sys.exit()
        else:
            print("\'" + str(j)+"\' is not a available option, please try agian.")
else:
    print("No images suitable for recolor found. Acceptable formats are .png , .jpg and .jpeg . The program will close in 5 seconds.")
    time.sleep(5)
    sys.exit()



