from PIL import Image, ImageDraw
import colorsys
import os


def main():

    #IMG_NAME = 'tinyrose'   #tiny rose
    #IMG_NAME = 'littleJack'
    IMG_NAME = 'highlight_guard'
    #IMG_NAME = 'guard'

    im = Image.open(IMG_NAME + '.jpg')
    #im = Image.open(IMG_NAME + '.png')
    pixels = im.load()  # create the pixel map
    bg = pixels[0,0]
    newbg = (57, 233, 155)


    print("pixels[0,0]: ", pixels[50,50])
    print("bg: ", bg)
    print("bg[2]: ", bg[2])

    for i in range(im.size[0]):  # for every pixel:
        for j in range(im.size[1]):
            px = pixels[i, j]
            #if px[0] > 100 and px[1] > 100 and px[2] > 100:
            #if px[0] < 100 and px[1] < 130 and px[2] < 250:
            #if px[0] < 65 and px[1] < 80 and px[2] > 190:

            #if px[0] < 40 and px[1] < 40 and px[2] > 70:
            #if px[0] < 40 and px[1] < 40 and px[2] > 75:  #maybe for highlighted

            if px[0] < 60 and px[1] < 60 and px[2] > 60:


            #if px[0] < 60 and px[1] < 60 and px[2] > 60:  # good  another for highlighted
            #if px[0] < 131 and px[1] < 131 and px[2] > 131:  # good good
                # change to blue
                #pixels[i, j] = (57, 233, 155)
                pixels[i, j] = newbg


    im.show()

    # save my image data from memory to a file with a different name
    im.save('highlight_' + IMG_NAME + '.jpg', 'JPEG')

# end of def main():

if __name__ == "__main__":
    main()
