import os


def rename(param, **Type):
    Img = 0
    File = 0
    Other = 0
    for parent_item in os.listdir(param):
        child_dir = os.path.join(param, parent_item)
        '''判断是否存在子目录
           不存在
        '''
        if not os.path.isdir(child_dir):
            file_type = os.path.splitext(parent_item)[1]
            if file_type in Type[list(Type)[0]]:
                Img = Img + 1
                new_name = 'Image_{0}{1}'.format(Img, file_type)
            elif file_type in Type[list(Type)[1]]:
                File = File + 1
                new_name = 'File_{0}{1}'.format(File, file_type)
            else:
                Other = Other + 1
                new_name = '_{0}{1}'.format(Other, file_type)
            os.rename(child_dir, os.path.join(param, new_name))
        # 存在
        else:
            new_dir = os.listdir(os.path.join(param, parent_item))
            for child_item in new_dir:
                reg = os.path.join(os.path.join(param, parent_item),
                                   child_item)
                if os.path.isdir(reg):
                    # 向下递归遍历
                    rename(reg)
                else:
                    # 向上遍历
                    file_type = os.path.splitext(child_item)[1]
                    if file_type in Type[list(Type)[0]]:
                        Img = Img + 1
                        new_name = 'Image_{0}{1}'.format(Img, file_type)
                    elif file_type in Type[list(Type)[1]]:
                        File = File + 1
                        new_name = 'File_{0}{1}'.format(File, file_type)
                    else:
                        Other = Other + 1
                        new_name = '_{0}{1}'.format(Other, file_type)
                    os.rename(os.path.join(child_dir, child_item),
                              os.path.join(child_dir, new_name))


if __name__ == "__main__":
    while 1:
        # D:\一级目录
        # D:\一级目录\二级目录
        file_type = {
            "Img": [".jpg", ".png", ".gif", ".webp", ".bmp", ".tif"],
            "txt": [".txt", ".ini", ".log", ".json", ".reg"]
        }
        path = str(input("请输入需要重命名的磁盘路径地址："))
        rename(path, **file_type)
