import qrcode
from pathlib import Path


def generate_qr_codes(area_name):
    # area_name = input("Area Name: ")

    img = qrcode.make(area_name)

    path_to_file = f'{area_name}.png'
    path = Path(path_to_file)

    if path.is_file():
        overwrite = input(f'File {area_name}.png already exists, overwrite? y/n')
        if overwrite == 'y':
            img.save(f'{area_name}.png')
        elif overwrite == 'n':
            print('Exiting')
    else:
        img.save(f'{area_name}.png')
