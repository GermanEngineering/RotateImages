# Rotate Images
This program will help you to automatically rotate your images into horizontal orientation.

## Downloads:
Clone or download the [Git Repository](https://github.com/GermanEngineering/RotateImages) or from my website:
For Windows:
	[20190130 - RotateImages.exe](https://trustmeimanengineer.de/wp-content/uploads/2019/01/RotateImagesWindows.7z)
For Linux / MAC:
	[20190130 - RotateImages.py](https://trustmeimanengineer.de/wp-content/uploads/2019/01/RotateImagesPython.7z)

## Application:
1. Unzip downloaded files.
1. Execute RotateImages.exe.
1. Specify the input folder in which your images are located.
	(all subdirectories will be processed as well)
1. Specify the output folder for the results.
1. Check the output folder for the results.

The application of the program is very simple and explained in [this YouTube video](https://youtu.be/A-gYWGp0qLk).
![Rotate Images](https://trustmeimanengineer.de/wp-content/uploads/2019/01/RotateImages.jpg)

## Function:
The program will go through all pictures in the specified input folder, including subfolders.
Only .jpg, .jpeg and .png files will be processed, while all others will be copied without any change.
Next, the program will try to get the orientation from the image exif data.
Every image containing this information will then be loaded and rotated into horizontal orientation.
The rotated images will be saved into the specified output folder.

I’ve already tested it successfully with LG and Samsung (Android Phone), Apple (iPhone), a Sony Camera, Android WhatsApp and GoPro images.

***

I'm frequently using this program in combination with another one helping you to unify picture names.
You can find more about the project on this site: [Unify Picture Names](https://trustmeimanengineer.de/en/unify-picture-names/).
