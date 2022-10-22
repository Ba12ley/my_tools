import re
from pprint import pprint
import base64

user_command = 'find /usr/share/ | grep root | grep mysql | tail -n 1'

output_commands = []

def special_character_to_url_encode(command):
    url_encoding_list = [command]
    special_character = {' ': '%20', '/': '%2f', '|': '%7c', '||': '%7c%7c', '&': '%26', '&&': '%26%26'}
    character_list = special_character.keys()

    for key in character_list:
        for item in url_encoding_list:
            if key in item:
                all_iters = item.replace(key, special_character[key])
                url_encoding_list.append(all_iters)
    # pprint(url_encoding_list)
    return url_encoding_list

def base_64_encode(command):
    encoded_bytes = base64.b64encode(command.encode("utf-8"))
    encoded_string = str(encoded_bytes, "utf-8")
    return encoded_string

def brace_expansion(command):
    space_replaced = command.replace(" ", ",")
    braced_output = str('{'+space_replaced+'}')
    return braced_output

def character_insertion(command):
    pass
    # final_command = ''
    # findall_words = re.findall(r'[A-Za-z]+', command)
    # for word in findall_words:
    #     for char in len(word):
    #         print(char)
    # print(len(command))
    # print(command[0])
    # print(len(command)//2)
    # print(command.split(' '))
    #
    # print(findall_words)



if __name__ == '__main__':
    character_insertion(user_command)