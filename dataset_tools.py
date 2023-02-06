import os
import shutil


def split_dataset_into_train_val(dataset_path, des_dir_train_path, des_dir_val_path,c_name,c_index,train_percent=0.8,tf_name='train.txt',vf_name='val.txt'):
    # des_dir_train_path为data/flower_dataset/train
    # des_dir_val_path为data/flower_dataset/val
    # dataset_path为data/flower_dataset
    # 计算训练集和测试集的大小

    # dataset_path_clsname 典型数据为data/flower_dataset/daisy
    dataset_path_clsname=os.path.join(dataset_path,c_name)
    # des_dir_train_path_clsname 典型数据为data/flower_dataset/train/daisy
    des_dir_train_path_clsname=os.path.join(des_dir_train_path,c_name)
    # des_dir_val_path_clsname 典型数据为data/flower_dataset/train/daisy
    des_dir_val_path_clsname = os.path.join(des_dir_val_path, c_name)

    #目录不存在，则创建
    if not os.path.exists(des_dir_train_path_clsname):
        os.mkdir(des_dir_train_path_clsname)
    if not os.path.exists(des_dir_val_path_clsname):
        os.mkdir(des_dir_val_path_clsname)

    # 计算对应目录下的图片数量
    image_count,image_file_list = count_image_file(dataset_path_clsname)
    train_len = int(image_count*train_percent)

    #写入信息到train.txt文件当中
    with open(tf_name,encoding='utf-8',mode='a') as f:
        # 将数据整理到训练目录中的类目录当中
        for i in range(train_len):
            orgin_image_file_path = os.path.join(dataset_path_clsname,image_file_list[i])
            des_image_file_path = os.path.join(des_dir_train_path_clsname,image_file_list[i])
            shutil.copy(orgin_image_file_path,des_image_file_path)
            f.writelines(c_name+'/'+image_file_list[i]+' '+str(c_index)+'\n')

    with open(vf_name, encoding='utf-8', mode='a') as f:
        # 将数据整理到验证集val目录
        for i in range(train_len,image_count):
            orgin_image_file_path = os.path.join(dataset_path_clsname,image_file_list[i])
            des_image_file_path = os.path.join(des_dir_val_path_clsname,image_file_list[i])
            shutil.copy(orgin_image_file_path,des_image_file_path)
            f.writelines(c_name + '/' + image_file_list[i] + ' ' + str(c_index) + '\n')



def count_image_file(dataset_path):
    image_count = 0
    image_file_list=[]
    for file in os.listdir(dataset_path):
        if file.endswith('.jpg'):
            image_count = image_count + 1
            image_file_list.append(file)
    print('image_count:',image_count)
    print('image_file_list:',image_file_list)
    return image_count,image_file_list
