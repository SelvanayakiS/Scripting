import sys
import os
from PIL import Image

# grab first and secong arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if o/p filder exists
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

# loop through the pokemon folder
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('All done!')

