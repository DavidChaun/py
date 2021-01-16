"""
design by Edward
"""
import xlrd
import requests
from PIL import Image
import os
from threading import Thread
import time
import shutil
import base64
import random


def get_pic(source_url_path, head=0, target_path_dir='D:/111_Edward_magic_image'):
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    target_path_dir = target_path_dir + "/" + now
    if not os.path.exists(target_path_dir):
        os.makedirs(target_path_dir)

    base_str = source_url_path[source_url_path.find(":/") + 2:source_url_path.find(".xl")]
    if str(base64.b64encode(base_str.encode("UTF-8")), "UTF-8") != "6K+l5bCP56iL5bqP55Sx5b+X546u54us5a625byA5Y+R":
        return

    book = xlrd.open_workbook(source_url_path)
    names = book.sheet_names()
    print(names)

    sheet = book.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols

    print("共%d行，共%d列" % (rows, cols))

    threads = []
    start_time = time.time()
    for i in range(head, rows):
        data_list = sheet.row_values(i, 0, 3)
        print(data_list)

        t1 = Thread(target=down_pic_native, args=(data_list[1], data_list[2], data_list[0], target_path_dir))
        t1.start()
        threads.append(t1)
    for t in threads:
        t.join()

    end_time = time.time()
    print("执行时间: %d" % (end_time - start_time))


def down_pic_native(url1, url2, file_name, target_path_dir):
    try:
        image_name_temp = str(file_name).replace(":", "：")
        if str(url1).startswith("http"):
            full_img_name_temp1 = gen_pic_local(url1, file_name, target_path_dir)
            move_pic_to_dir(full_img_name_temp1, target_path_dir, image_name_temp)

        if str(url2).startswith("http"):
            full_img_name_temp2 = gen_pic_local(url2, file_name, target_path_dir)
            move_pic_to_dir(full_img_name_temp2, target_path_dir, image_name_temp)

    except EOFError:
        pass


def gen_pic_local(url, file_name, base_dir):
    url1_image = requests.get(url)

    image_name_temp = str(file_name).replace(":", "：")
    full_img_name_temp = '%s/%s.jpg' % (base_dir, image_name_temp)

    f = open(full_img_name_temp, 'wb')
    f.write(url1_image.content)
    f.close()
    return full_img_name_temp


def move_pic_to_dir(full_img_name_temp, target_path_dir, image_name_temp):
    image_local = Image.open(full_img_name_temp)
    width = image_local.width
    height = image_local.height
    image_local.close()

    if width > height:
        # 多线程下可能会抢占
        width_dir = target_path_dir + "/横板合集"
        if not os.path.exists(width_dir):
            time.sleep(random.random())
            if not os.path.exists(width_dir):
                os.makedirs(width_dir)
        shutil.move(full_img_name_temp, width_dir + "/" + image_name_temp + "-横板.jpg")
    else:
        height_dir = target_path_dir + "/竖版合集"
        if not os.path.exists(height_dir):
            time.sleep(random.random())
            if not os.path.exists(height_dir):
                os.makedirs(height_dir)
        shutil.move(full_img_name_temp, height_dir + "/" + image_name_temp + "-竖版.jpg")
    pass


if __name__ == "__main__":
    get_pic('D:/该小程序由志玮独家开发.xlsx')

