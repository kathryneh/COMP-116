#Assignment 5
#Name: Katie Hawthorne
#Collaborators: Emily Bailey
#Due 9 October 2009

# Grade 100/100

import numpy as np
import pylab

# some helpers to load and save images
def load_binary_image(name):
    '''Load a binary image from a file'''
    im = pylab.imread(name)
    if im.ndim == 3:
        result = im[:,:,0] != 0
    elif im.ndim == 2:
        result = im != 0
    return result

def save_binary_image(name, value):
    '''Save a binary image to a file'''
    pylab.imsave(name, value, cmap='gray')

# load the test image we'll use below
test_image = load_binary_image('test.png')

# 1. Scroll images.

# define your functions to scroll images

def scrollLeft(img, amt):
		'''Return a new image that is the given image scrolled left by amt pixels'''
		new = np.zeros_like(img)
		# do something to fill in values in new here
		new[:, :-amt] = img[:,amt:]
		#have to figure out here how to make the values of the image ten pixels left and insert them in the array just made
		return new

# similarly define the rest of them.

def scrollRight(img, amt):
    new = np.zeros_like(img)
	#try it again here
    new[:,amt:]=img[:,:-amt]
    '''Return a new image that is the given image scrolled right by amt pixels'''
    return new

def scrollUp(img, amt):
    new=np.zeros_like(img)
    '''Return a new image that is the given image scrolled up by amt pixels'''
    new[:-amt,:]=img[amt:,:]
    return new

def scrollDown(img, amt):
	new = np.zeros_like(img)
	'''Return a new image that is the given image scrolled down by amt pixels'''
	new[amt:,:]=img[:-amt,:]
	return new

# 1A. scroll the image up by 10 pixels.
up10 = scrollUp(test_image, 10)
# and save that
save_binary_image('1A.png', up10)

#to see what it looks like here

# 1B. now scroll the result of 1A down by 10 pixels.
updown10 = scrollDown(up10, 10)
# and save that
save_binary_image('1B.png', updown10)

# 1C. Do they look the same? Why or why not?

# answer here in this comment: No they do not because the top ten pixels of the original image have been cut off, and despite that the image has been scrolled down and then scrolled back up the same amount, some of that data has been replaced with null data (or zeroes)

# 1D. Scroll the test image left by half its width
ShapeImg=test_image.shape
print 'shape of the image array=', ShapeImg
#ShapeImg=(162, 78)
leftHalf= scrollLeft(test_image, 39 )
# save it in 1D.png as above
save_binary_image('1D.png', leftHalf)
# 1E. and then scroll that result back to the right by the same amount.
rightimg=load_binary_image('1D.png')
rightback = scrollRight(rightimg, 39) 
# save in 1E.png.
save_binary_image('1E.png', rightback)
# 2. Boundary Detector

def findBoundary(img):
	LB=scrollLeft(img,1)
	LB=np.logical_and(LB, ~img)
	RB=scrollRight(img,1)
	RB=np.logical_and(RB, ~img)
	Sides=np.logical_or(LB,RB)
	TB=scrollUp(img,1)
	TB=np.logical_and(TB, ~img)
	BB=scrollDown(img,1)
	BB=np.logical_and(BB, ~img)
	Edges=np.logical_or(TB,BB)
	boundary=np.logical_or(Sides,Edges)
	return boundary
	
def findBoundary1(img):
	LI=scrollLeft(img,1)
	rightBoundary=np.logical_and(~LI, img)
	LI=scrollRight(img,1)
	leftBoundary=np.logical_and(~LI, img)
	horizBoundary=np.logical_or(leftBoundary,rightBoundary)
	LI=scrollUp(img,1)
	topBoundary=np.logical_and(~LI, img)
	LI=scrollDown(img,1)
	bottomBoundary=np.logical_and(~LI, img)
	verticalBoundary=np.logical_or(topBoundary,bottomBoundary)
	wholeBoundary=np.logical_or(horizBoundary,verticalBoundary)
	return wholeBoundary
'''Return an image that is one for boundary pixels and zero elsewhere'''
#create new image shifted left by one for every i,j has been shifted over by 1
#then, we've got two images with the same source; one is the left shifted source of the other. 
# a pixel is on the right boundary if the pixel is true and the one in LI (corresponding) is false. 
#could use logical_and use the complement of one, so if this was true and neighbor to right was false.
#LI=scrollLeft(test_image,1)
#rb=np.logical_and(test_image, ~LI)
#we also will have scroll left, scroll right, scroll up, scroll down
#how do we combine them? 
#use a function logical_or to combine them: if any pixel is true, the result should be true. 
#logical_or only takes two, so take two, then or them, and or the other two.
# compute the result of finding the boundary here
    

# show the boundary of the test image
boundary = findBoundary(test_image)
	
save_binary_image('2.png', boundary)

# 3. Dilate and Erode

def dilateImage(img):
    Add=findBoundary(img)
    dilate =np.logical_or(img, Add)
    result=dilate
    '''Return an image that is the dilation of the input img'''
    # compute the dilation here
    return result

def erodeImage(img):
    Subtract=findBoundary1(img)
    erode=np.logical_and(img, ~Subtract)
    '''Return an image that is the erosion of the input img'''
    # compute the value into result
    return erode

# 3A dilate the test image, then dilate that result, then dilate that result so you have
# three dilations. So the final result.
#for this part, use the boundary image and logical_and to find where both are true, and set both true values to zero. 
#dilation is just like the boundary except the roles of each are switched. 
D3 = dilateImage(dilateImage(dilateImage(test_image)))
save_binary_image('3A.png', D3)

E3 = erodeImage(erodeImage(erodeImage(test_image)))
save_binary_image('3B.png', E3)

E3= load_binary_image('3B.png')

E3D3 = dilateImage(dilateImage(dilateImage(E3)))
save_binary_image('3C.png', E3D3)
#for some unknown reason, this will not work. 

#E3D3=load_binary_image('test.png')
#save_binary_image('3C.png', E3D3)
#this is what it should end up looking like. 

# 3D. Find the boundary of the original image, and then dilate the boundary image.  Save the result.
Boundary=findBoundary(test_image)
DB=dilateImage(Boundary)
save_binary_image('3D.png', DB)
# save as 3D.png

# 3E. Then take the original image, dilate it once, and then find its boundary.  Save the result.
DI=dilateImage(test_image)
DIB=findBoundary(DI)
save_binary_image('3E.png',DIB)
# save as 3E.png

# 3F. Describe the difference between the two images. 

# put your description here as a comment.
#The second image is less bold than the first image; the boundary is much thinner when the boundary of the dilation is found
#and the dilated boundary is much thicker
