from PIL import Image, ImageDraw
import colorsys
import os


def main():
    IMG_NAME = 'guard'
    BACKGROUND_IM = 'bigcity'

    im = Image.open(IMG_NAME + '.jpg')
    ct = Image.open(BACKGROUND_IM + '.jpg')

    print("im.size: ", im.size)
    print("ct.size: ", ct.size)

    # now get the pixels
    pixels = im.load()  # create the pixel map
    bg_pixels = ct.load()  # create the pixel map

    bg = pixels[0,0]    # get corner pixel value
    #newbg = (57, 233, 155)
    newbg = (255, 255, 0)       # yellow

    # Appply Tolerance to the RGB values
    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            px = pixels[i, j]
            if px[0] < 131 and px[1] < 131 and px[2] > 131:  # good good
                pixels[i, j] = newbg

    # Apply further Tolerance to the RBG values
    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            px = pixels[i, j]
            #if px[0] < 60 and px[1] < 60 and px[2] > 60:  # good  another for highlighted
            if px[0] < 50 and px[1] < 54 and px[2] > 54:
                pixels[i, j] = newbg

    #im.show()

    # fill in background
    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            px = pixels[i, j]
            if px == newbg:
                pixels[i, j] = bg_pixels[i, j]

    im.show()

    # save my image data from memory to a file with a different name
    im.save('highlight_' + IMG_NAME + '.jpg', 'JPEG')

# end of def main():

if __name__ == "__main__":
    main()
