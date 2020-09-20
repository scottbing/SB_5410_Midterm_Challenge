from PIL import Image, ImageDraw
import colorsys
import os


def main():

    IMG_NAME = 'guard'
    BACKGROUND_IM = city

    im = Image.open(IMG_NAME + '.jpg')

    pixels = im.load()  # create the pixel map
    bg = pixels[0,0]    # get corner pixel value
    #newbg = (57, 233, 155)
    newbg = (255, 255, 0)

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            px = pixels[i, j]
            #if px[0] < 60 and px[1] < 60 and px[2] > 60:  # good  another for highlighted
            if px[0] < 131 and px[1] < 131 and px[2] > 131:  # good good
                pixels[i, j] = newbg

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            px = pixels[i, j]
            if px[0] < 60 and px[1] < 60 and px[2] > 60:  # good  another for highlighted
            #if px[0] < 131 and px[1] < 131 and px[2] > 131:  # good good
                pixels[i, j] = newbg


    im.show()

    # save my image data from memory to a file with a different name
    im.save('highlight_' + IMG_NAME + '.jpg', 'JPEG')

# end of def main():

if __name__ == "__main__":
    main()
