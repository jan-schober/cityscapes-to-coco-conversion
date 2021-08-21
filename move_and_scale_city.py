import glob
from PIL import Image



source_folder = glob.glob('/storage/Cityscapes/cityscape_dataset/leftImg8bit/train/*/*.png')
target_folder = '/home/schober/cityscape_dataset/annotations/darknet_labels_train/images/'

for file in source_folder:
    img = Image.open(file)
    img = img.resize((512,256))

    file_name = file.split('/')[-1]
    output_dst = target_folder + file_name
    img.save(output_dst)

