from PIL import Image, ImageDraw
import colorsys
import os


def main():

    #IMG_NAME = 'tinyrose'   #tiny rose
    #IMG_NAME = 'littleJack'
    IMG_NAME = 'highlighted_guard'

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
            if px[0] < 45 and px[1] < 45 and px[2] > 75:
            #if px[0] < 131 and px[1] < 131 and px[2] > 131:  # good
                # change to blue
                #pixels[i, j] = (57, 233, 155)
                pixels[i, j] = newbg


    im.show()

    # save my image data from memory to a file with a different name
    im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')

# end of def main():

if __name__ == "__main__":
    main()
