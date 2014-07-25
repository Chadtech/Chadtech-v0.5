import os
import PIL
from PIL import Image

numberOfImages = 0
for fileItem in os.listdir(os.getcwd()):
	print 'FILEITEM',fileItem
	if fileItem.endswith('.PNG') and fileItem.startswith('w'):
		numberOfImages+=1

print 'NUMBER OF IMAGES',numberOfImages
spriteSheet = Image.new('RGB',(12*numberOfImages,16),(0,0,0))

for imageFile in range(numberOfImages):
	print imageFile
	spriteSheet.paste(Image.open('w'+str(imageFile).zfill(4)+'.PNG'),(12*imageFile,0))

spriteSheet.save('spriteSheet.PNG','png')