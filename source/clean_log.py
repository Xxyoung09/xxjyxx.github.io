import os

def delete_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

# 删除当前目录下的image1文件
image1_file_path = "image_compare_log"
if os.path.isfile(image1_file_path):
    os.remove(image1_file_path)

# 删除当前目录下的test_image文件夹下的所有文件
test_image_dir_path = "test_image"
if os.path.isdir(test_image_dir_path):
    delete_files(test_image_dir_path)