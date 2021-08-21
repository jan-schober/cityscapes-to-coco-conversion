import os
import json
from os import listdir, getcwd
from os.path import join

classes = ['bicycle', 'bus', 'car', 'motorcycle', 'person', 'rider', 'traffic light', 'traffic sign', 'train', 'truck']

# box form[x,y,w,h]
def convert(size, box):
    dw = size[0]
    dh = size[1]

    w = box[2]
    h = box[3]

    x = (box[0] + 0.5 * w)/dw
    y = (box[1] + 0.5 * h)/dh

    w = w / dw
    h = h / dh
    return (x, y, w, h)


def convert_annotation():
    with open('/home/schober/cityscape_dataset/annotations/instancesonly_filtered_gtFine_train.json', 'r') as f:
        data = json.load(f)
    for item in data['images']:
        image_id = item['id']
        file_name = item['file_name']
        width = item['width']
        height = item['height']
        value = filter(lambda item1: item1['image_id'] == image_id, data['annotations'])
        subfolder_list = file_name.split('/')[:-1]
        subfolder = '/'.join(subfolder_list)
        out_folder = os.path.join('/home/schober/cityscape_dataset/annotations/darknet_labels_train/', subfolder)
        print(out_folder)
        if not os.path.exists(out_folder):
            os.makedirs(out_folder)
        outfile = open('/home/schober/cityscape_dataset/annotations/darknet_labels_train/%s.txt' % (file_name[:-4]), 'a+')
        for item2 in value:
            category_id = item2['category_id']
            value1 = list(filter(lambda item3: item3['id'] == category_id, data['categories']))
            name = value1[0]['name']
            if name == 'rider':
                name = 'person'
            class_id = classes.index(name)
            box = item2['bbox']
            bb = convert((width, height), box)
            outfile.write(str(class_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        outfile.close()


if __name__ == '__main__':
    convert_annotation()
