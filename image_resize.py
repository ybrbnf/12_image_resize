import os
import argparse
from PIL import Image


def resize_image(path_to_original, path_to_result):
    img = Image.open(args.filename)
    width, height = img.size
    file_format = img.format
    if args.scale:
        width = int(width * args.scale)
        height = int(height * args.scale)
    elif args.width and args.height:
        if width/height != args.width/args.height:
            print ('Обработаное избражение будет с нарушением пропорций')
        width, height = (args.width, args.height)
    elif args.width:
        ratio = int(args.width / width)
        width, height = (args.width, height * ratio)
    elif args.height:
        ratio = int(args.height / height)
        width, height = (width * ratio, args.height)
    if args.output:
        file_name = os.path.basename(args.filename)
        file_path = os.path.dirname(args.output)
        result = '{}/{}'.format(file_path, file_name)
    else:
        file_name = os.path.splitext(args.filename)[0]
        file_path = os.path.dirname(args.filename)
        if not file_path:
            file_path = os.getcwd()
        result = '{}/{}__{}x{}.{}'.format(
                                          file_path,
                                          file_name,
                                          width,
                                          height,
                                          file_format
                                          )
    return img, width, height, result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help', action='help',
                        help='show this message and exit')
    parser.add_argument('-f', '--filename', type=str,
                        help='Файл исходного изображения')
    parser.add_argument('-s', '--scale', type=float,
                        help='Изменение размеров изображения в scale раз')
    parser.add_argument('-w', '--width', type=int,
                        help='Изменение ширины изображения')
    parser.add_argument('-h', '--height', type=int,
                        help='Изменение высоты изображения')
    parser.add_argument('-o', '--output', type=str,
                        help='Путь для сохранения обработанного изображения')
    args = parser.parse_args()
    if not args.filename:
        print ('Необходимо указать исходный файл')
    else:
        if args.scale and (args.width or args.height):
            print ('Используйте либо ключ scale, либо ключи width/height')
        else:
            img_res = resize_image(args.filename, args.output)
            img = img_res[0].resize((img_res[1], img_res[2]), Image.ANTIALIAS)
            img.save(img_res[3], mode='RGBA')
