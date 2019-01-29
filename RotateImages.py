import os
from datetime import datetime
import logging
import Progress
from PIL import Image
import piexif
from shutil import copy2
 
def RotateImages(inputFolder, outputFolder):
    processedFiles = 0
    # iterate through all files including subdirectories
    for path, subDirectories, files in os.walk(inputFolder):
        # create output path
        if not os.path.exists(path.replace(inputFolder, outputFolder)):
            os.makedirs(path.replace(inputFolder, outputFolder))

        for file in files:
            filePath = os.path.join(path, file)

            # get exif data
            exifDictionary = piexif.load(filePath)
            orientation = exifDictionary["0th"][piexif.ImageIFD.Orientation]

            if orientation == 1 and inputFolder != outputFolder:
                copy2(filePath, filePath.replace(inputFolder, outputFolder))

            elif orientation > 1:
                # set orientation to 1 and delete thumbnail data
                exifDictionary["0th"][piexif.ImageIFD.Orientation] = 1             
                exifDictionary.pop("thumbnail")

                # load image
                image = Image.open(filePath)

                # rotate image
                if orientation == 2:
                    image = image.transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 3:
                    image = image.rotate(180)
                elif orientation == 4:
                    image = image.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 5:
                    image = image.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 6:
                    image = image.rotate(-90, expand=True)
                elif orientation == 7:
                    image = image.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 8:
                    image = image.rotate(90, expand=True)

                # save image with updated exif data
                image.save(filePath.replace(inputFolder, outputFolder), "JPEG", quality=95, exif=piexif.dump(exifDictionary))

            # show progress
            processedFiles = processedFiles + 1
            Progress.PrintProgress(processedFiles)

def GetFormattedDatetimeNow():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

try:
    logging.basicConfig(filename="RotateImages.log", level=logging.INFO)
    logging.info("{0} - ##### Program Start #####".format(GetFormattedDatetimeNow()))

    inputFolder = input("Please specify the relative input folder name.\nJust press Enter to use the default value \"output\".\n")
    if not inputFolder:
        inputFolder = "output"
    outputFolder = input("Please specify the relative output folder name.\nJust press Enter to use the default value \"output\".\n")
    if not outputFolder:
        outputFolder = "output"

    RotateImages(inputFolder, outputFolder)

    logging.info("{0} - ##### Execution Finished #####\n".format(GetFormattedDatetimeNow()))

except Exception as e:
    logging.exception("{0} - {1}".format(GetFormattedDatetimeNow(), e))
