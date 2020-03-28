import os


def reName(dirname):
    for category in os.listdir(dirname):
        filename = os.path.splitext(category)[0]
        filetype = os.path.splitext(category)[1]
        odir = dirname + "\\" + category
        if filename.startswith('000'):
            filename = str.replace(filename, "000", '')
            if int(filename) < 10:
                filename = '0' + filename
            fullname = "\\" + filename + filetype
            ndir = dirname + fullname
            os.rename(odir, ndir)
        else:
            if int(filename) < 10:
                filename = '0' + filename
            fullname = "\\" + filename + filetype
            ndir = dirname + fullname
            os.rename(odir, ndir)


if __name__ == '__main__':
    while 1:
        dirname = str(input('请输入地址'))
        if dirname == 'quit':
            break
        else:
            reName(dirname)
