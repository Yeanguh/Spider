import glob
import os
import threading
import time

from PIL import Image


def create_image(oold_filename):
    im = Image.open("./pic/" + oold_filename)
    filename = oold_filename.split('.')[0]
    im.save("./webp/" + str(filename) + ".webp", "WEBP")

# def pic_webp(picpath):
#     imagePath = picpath.split(".")[0] #文件名称
#     outputPath = imagePath + ".webp" #输出文件名称
#     im = Image.open(imagePath) #读入文件
#     im.save(outputPath) #保存


def start():
    for (dirpath, dirname, dirfile) in os.walk("./pic/"):
        print(dirpath, dirname, dirfile)
        for i in dirfile:
            create_image(i)
        # t = threading.Thread(target=create_image, args=(infile, index,))
        # t.start()
        # t.join()
        # index += 1


if __name__ == "__main__":

    start_time = time.time()
    start()
    end_time = time.time()
    final_time = end_time - start_time
    print(final_time)
