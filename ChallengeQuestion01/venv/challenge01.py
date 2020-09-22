from PIL import Image, ImageDraw
import colorsys
import os


def main():
    IMG_NAME = 'jack'
    BACKGROUND_IM = 'citystreet'

    with Image.open(IMG_NAME + '.jpg') as im:
        # width = int(im.size[0])
        # height = int(im.size[1])

        #open background image
        ct = Image.open(BACKGROUND_IM + '.jpg')
        bg_pixels = ct.load()  # create the pixel map

        #confirm  that both images are the same size
        print("jack size: ", im.size)
        print("city size: ", im.size)

        pixels = im.load()  # get the pixels

        #bg = pixels[0, 0]  # grab pixel value of NW corner - pixel[0,0]
        bg = (4, 255, 0)
        print("bg pixeel[0,0]: ", bg)

        #set background to new color - from green to blue
        newbg = (56, 133, 255)  # set new background color (blue)

        #  First pass
        # set all pixel values = pixel[0,0]
        for i in range(im.size[0]):  # for every pixel:
            for j in range(im.size[1]):
                px = pixels[i, j]
                if px == bg:
                    pixels[i, j] = newbg

        # threshold setting for rgb values
        threshold = 150

        for i in range(im.size[0]):  # for every pixel:
            for j in range(im.size[1]):
                px = pixels[i, j]
                r, g, b = bg
                if px[0] < threshold and px[1] > threshold and px[2] < threshold:
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
    im.save('final_' + IMG_NAME + '.jpg', 'JPEG')


# end of def main():

if __name__ == "__main__":
    main()
