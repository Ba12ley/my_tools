from qr_generator import generate_qr_codes
import pyfiglet

ascii_banner = pyfiglet.figlet_format('Enter your\n Areas')

def get_user_list():
    end_list_entry = False
    area_list = []
    while not end_list_entry:
        area_list.append(input('Enter Area Name: '))
        print(f'{area_list}')
        add_more = input('Add another? y/n')
        if add_more == 'n':
            end_list_entry = True
            print(area_list)
    return area_list


def generate_from_area_list(area_list):
    for area in area_list:
        for i in range(1, 6):
            generate_qr_codes(area + str(i))


if __name__ == '__main__':
    print(ascii_banner)
    generate_from_area_list(get_user_list())
