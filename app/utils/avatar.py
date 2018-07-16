#!/usr/bin/env python
# coding=utf-8


from PIL import Image, ImageDraw
from random import randint
from hashlib import md5


GRID_SIZE = 9
BORDER = 10
LENGTH = 110

class GenerateImage(object):

    """生成avatar图像"""

    def __init__(self, _str, _bg_color="#fff"):
        w, h = LENGTH, LENGTH
        # 用作hash的字符串
        self.has_code_str = _str
        self.image = Image.new('RGB', (w, h), _bg_color)
        self.draw = ImageDraw.Draw(self.image)
        self.hash = int(md5(_str.encode('utf-8')).hexdigest(), 16)
    
    def image_grid_color(self):
        return (self.hash>>8 & 0xff, self.hash>>16&0xff, self.hash>>24&0xff)

    def image_data(self):
        """生成那些位置图有颜色, 那些位置没有"""
        color = self.image_grid_color()
        print (color)
        self.hash >> 16
        x, y=0, 0
        for index_x in range(int((GRID_SIZE*BORDER)/2)):
            if self.hash & 1:
                index_x = BORDER+(x*BORDER)
                index_y = BORDER+(y*BORDER)
                self.draw.rectangle(
                        [index_x, index_y, index_x+BORDER, index_y+BORDER], fill=color)
                # 对称的位置
                index_x = LENGTH-index_x-BORDER
                self.draw.rectangle(
                        [index_x, index_y, index_x+BORDER, index_y+BORDER], fill=color)
            self.hash >>= 1
            y += 1
            if y == GRID_SIZE:
                y = 0
                x+=1
    
    def get_image(self):
        self.image_data()
        with open('./images/{}.png'.format(self.has_code_str), 'wb') as fp:
            self.image.save(fp, 'PNG')


if __name__ == '__main__':
    for index in range(2, 4):
        image = GenerateImage('1504052{}'.format(index))
        image.get_image()

