import os
import argparse
from PIL import Image


def open_image(path_to_original):
    image = Image.open(args.filename)
    return image


def resize_image(image, scale, width, height):
    if scale:
        new_width = int(image.width * scale)
        new_height = int(image.height * scale)
    elif width and height:
        new_width, new_height = (width, height)
    elif width:
        ratio = (width / image.width)
        new_width, new_height = (width, int(image.height * ratio))
    elif height:
        ratio = (height / image.height)
        new_width, new_height = (int(image.width * ratio), height)
    return new_width, new_height


def get_name_of_new_image(size, path_to_original, path_to_result):
    if args.output:
        file_name = os.path.basename(args.filename)
        file_path = os.path.dirname(args.output)
    else:
        file_name = os.path.splitext(args.filename)[0]
        file_ext = os.path.splitext(args.filename)[1]
        file_path = os.path.dirname(args.filename)
        file_name = '{}__{}x{}{}'.format(file_name, size[0], size[1], file_ext)
    return os.path.join(file_path, file_name)


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
    elif not (args.scale or args.width or args.height):
        print ('Размер изображения не изменяется')
    else:
        image = open_image(args.filename)
        if args.scale and (args.width or args.height):
            print ('Используйте либо ключ scale, либо ключи width/height')
        elif args.width and args.height:
            if input_image.width/input_image.height != args.width/args.height:
                print ('Обработаное избражение будет с нарушением пропорций')
        new_size = resize_image(image, args.scale, args.width, args.height)
        path_to_save = get_name_of_new_image(new_size, args.filename, args.output)
        output_image = image.resize(new_size, Image.ANTIALIAS)
        output_image.save(path_to_save, mode='RGBA')
