"""
https://avmoo.cyou/cn/genre/6387ceb8946b83c3
把封面图爬下来
"""
import requests
import re
from time import sleep
import os

PIC_PATTERN = re.compile(r'<div class="photo-frame">\s*<img src="(.*?)" title="(.*?)">\s*</div>')


def decode_page(page_bytes, charsets):
    """通过指定的字符集对页面进行解码"""
    for charset in charsets:
        try:
            return page_bytes.decode(charset)
        except UnicodeDecodeError:
            pass


def show_content(num: int) -> str:
    url = "https://avmoo.cyou/cn/genre/6387ceb8946b83c3/page/%d" % num
    resp = requests.get(url)
    if resp.status_code == 200:
        """
        解析这段东西
        <div class="item">
            <a class="movie-box" href="https://avmoo.cyou/cn/movie/9e695e374c89b2ca">
                <div class="photo-frame">
                    <img src="https://jp.netcdn.space/digital/video/ebod00808/ebod00808ps.jpg" title="夏目藍果">
                </div>
                <div class="photo-info">
                   <span>夏目藍果 <br><date>EBOD-808</date> / <date>2021-03-13</date></span>
                </div>
            </a>
        </div>
        """
        return decode_page(resp.content, charsets={"utf-8", "gbk"})


def get_pic_url(c: str):
    return PIC_PATTERN.findall(c)


def pic_url_to_local(pic_set: tuple, page_num=1, target_dir='D:/1scratch_pic'):
    if not pic_set or len(pic_set) != 2:
        pass
    page_target_dir = f'{target_dir}/{page_num}'
    if not os.path.exists(page_target_dir):
        os.makedirs(page_target_dir)

    resp = requests.get(pic_set[0])
    if resp.status_code == 200:
        image_name_temp = str(pic_set[1]).replace(":", "：").replace("\\", " ").replace("/", " ")\
                            .replace("*", " ").replace("?", "？").replace('"', "“")\
                            .replace("<", "《").replace(">", "》").replace("|", "l")
        if len(image_name_temp) > 200:
            image_name_temp = image_name_temp[0:200]
        full_img_name = f'{page_target_dir}/{image_name_temp}.jpg'

        '''判断是否存在该文件，存在跳过'''
        if not os.path.exists(full_img_name):
            f = open(full_img_name, "wb")
            f.write(resp.content)
            f.close()


if __name__ == "__main__":
    page = 2
    while page < 10:
        content = show_content(page)
        if content and content != '':
            pic_list = get_pic_url(content)
            for pic in pic_list:
                '''dict类型'''
                print(pic)
                pic_url_to_local(pic, page)
        page += 1



