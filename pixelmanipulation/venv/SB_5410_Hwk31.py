from PIL import Image, ImageDraw
from SortFunctions import selectionSort
from SortFunctions import quickSortRecursive, quickSortIterative
from SearchFunctions import binarySearchSub
from PixelFunctions import *


def main():
    #IMG_NAME = 'tinyrose'   #Tiny
    #IMG_NAME = 'bigrose'   #Medium
    #IMG_NAME = 'abq'        #Large 500x300
    #IMG_NAME = 'abq_huge'   #Huge 1500x1300
    IMG_NAME = 'jack'
    #IMG_NAME = 'guard'

    # open image
    # read each pixel into memory as the image object im
    with Image.open(IMG_NAME + '.jpg') as im:
        pixels = storePixels(im)
        print("stored")

        ### sort copy of pixels ###
        sorted_pixels = pixels.copy()
        #selectionSort(sorted_pixels, comparePixels)
        quickSortIterative(sorted_pixels, 0, len(sorted_pixels)-1, comparePixels)
        print("sorted")
        sorted_im = pixelsToImage(im, sorted_pixels)
        sorted_im.save('sorted_'+ IMG_NAME + '.jpg', 'JPEG')

        # grayscale pixels in place
        #grayScale(im, pixels)

        while(True): #do whileloop in Python does not exist
            command = input("Type a value for red threshold or Q to quit:")
            if(command in ('q', 'Q')):
                save = input("Save File? (Y|y) or press any other key to Quit")
                if (save in ('y', 'Y')):
                    format = input("which format?  enter '1' for 'JPEG';  '2' for 'PNG'")
                    if (format == '1'):
                        print("Saved as JPEG")
                        im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')
                    elif (format == '2'):
                        print(" Saved as PNG")
                        im.save('highlighted_' + IMG_NAME + '.png', 'PNG')
                    else:
                        print("Invalid option - file was not saved")
                break   #leave loop

            #might want to test that command is a number or convert it
            threshold = int(command)

            # grayscale pixels in place
            grayScale(im, pixels)

            #search copy for r
            # use a comprehension to find the sorted r values
            # sorted_r_values = [r[0][0] for r in sorted_pixels}
            subi = binarySearchSub([r[0][0] for r in sorted_pixels],
                                   0, len(sorted_pixels)-1, threshold)
            #print("Sublist of resds starts at: ", subi)

            # restore found r
            # uses list slice notation to remove any item before subi
            pixelsToPoints(im, sorted_pixels[subi:])
            #pixelsToPoints(im, sorted_pixels[0:subi])
            im.show()
        #end while(True)

    # end with Image.open(IMG_NAME + '.jpg') as im:

    # save my image data from memory to a file with a different name
    im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')

    # opens with your external preiview program, shows memory representaion
    #im.show()
# end of def main():

if __name__ == "__main__":
    main()
