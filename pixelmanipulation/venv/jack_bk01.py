from PIL import Image, ImageDraw
import colorsys
import os


def main():
    IMG_NAME = 'littlejack'

    with Image.open(IMG_NAME + '.jpg') as im:
        width = int(im.size[0])
        height = int(im.size[1])

        pixels = im.load()  # get the pixels

        bg = pixels[0, 0]  # grab pixel value of corner
        print("bg: ", bg)

        newbg = (56, 133, 255)  # set new background color (blue)


        for i in range(im.size[0]):  # for every pixel:
            for j in range(im.size[1]):
                px = pixels[i, j]
                if px == bg:
                    pixels[i, j] = newbg

        # for i in range(im.size[0]):  # for every pixel:
        #     for j in range(im.size[1]):
        #         px = pixels[i, j]
        #         r, g, b = bg
        #         if px[0]
        #         if px == bg:
        #             pixels[i, j] = newbg



    im.show()

    # save my image data from memory to a file with a different name
    #im.save('highlight_' + IMG_NAME + '.jpg', 'JPEG')


# end of def main():

if __name__ == "__main__":
    main()
