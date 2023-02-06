import pathlib
from dataset_tools import *

root_dataset_path='./data/flower_dataset'
files = os.scandir(root_dataset_path)

class_file_name = 'classes.txt'
train_file_name = 'train.txt'
val_file_name = 'val.txt'
# the percent of trainset
train_percent = 0.8

# define the directory of train and val datasets
flower_dataset_train_dir = './data/flower_dataset/train'
flower_dataset_val_dir = './data/flower_dataset/val'
# create train and val directory if not exist.
if not os.path.exists(flower_dataset_train_dir):
    os.mkdir(flower_dataset_train_dir)
if not os.path.exists(flower_dataset_val_dir):
    os.mkdir(flower_dataset_val_dir)

#split_dataset_into_train_val(root_dataset_path,'daisy')
#print(count_image_file(root_dataset_path+'/daisy'))
class_name = []
train_val_lst = ['train','val']
# 创建classes.txt文件
with open(class_file_name, encoding="utf-8", mode='w') as c_file:
    for file in files:
        print(file, file.name, file.path, file.is_dir())
        # save in the list for usage
        if file.name not in train_val_lst:
            class_name.append(file.name)
            c_file.writelines(file.name + '\n')

for i,c_name in enumerate(class_name):
    split_dataset_into_train_val(root_dataset_path,flower_dataset_train_dir,
                                 flower_dataset_val_dir,c_name,i,0.8,train_file_name,val_file_name)




