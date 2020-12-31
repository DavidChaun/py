"""
design by wayne
"""
import xlrd
import requests
import os


def get_pic(source_url_path, head=0, target_path_dir='D:/image'):
    if not os.path.exists(target_path_dir):
        os.makedirs(target_path_dir)

    book = xlrd.open_workbook(source_url_path)
    names = book.sheet_names()
    print(names)

    sheet = book.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols

    print("共%d行，共%d列" % (rows, cols))

    # 根据行遍历数据

    for i in range(head, rows):
        try:
            data_list = sheet.row_values(i, 0, 2)
            print(data_list)

            image = requests.get(data_list[1])

            image_name = str(data_list[0]).replace(":", "：")
            # 文件的打开模式：w for write，b for binary
            f = open('%s/%s.jpg' % (target_path_dir, image_name), 'wb')
            f.write(image.content)
            f.close()
        except:
            pass


get_pic('D:/竖版(1).xlsx')
