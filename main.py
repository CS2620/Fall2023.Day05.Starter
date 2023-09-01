# The program requires pillow
# python -m pip install pillow
print("Start")

# import Image from PIL
# use Image.open to open the file and assign it to a variable
# load the image with <reference>.load and store the pixel buffer
# Get the width and height by getting the first and second array entries of <reference>.size
# loop over y and x
# get the pixel at <buffer>[x,y]
# get the rgb of <pixel> by accessing array values 0,1,2
# create a new list of (r,g,b)
# update <buffer>[x,y] with the new list
# save <reference> with <reference>.save("filename.ext", "ext"
