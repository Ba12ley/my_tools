from pprint import pprint

import helpers

user_command = input('Enter the command: ')
file_name = input('Enter filename: ')

if __name__ == '__main__':
    command_list = []
    url_commands = helpers.special_character_to_url_encode(user_command)
    for command in url_commands:
        command_list.append(command)

    command_list.append(helpers.brace_expansion(user_command))
    command_list.append(helpers.character_insertion(user_command))
    command_list.append(helpers.base_64_encode(user_command))
    reversing_list =[]
    base_command_list = []

    for command in command_list:
        base_all = helpers.base_64_encode(command)
        base_command_list.append(base_all)

    for command in base_command_list:
        command_list.append(command)

    for command in command_list:
        reversing_list.append(command)

    for command in reversing_list:
        rev_command = helpers.reverse_commands(command)
        command_list.append(rev_command)

    with open(f'{file_name}.txt', 'w') as f:
        for command in command_list:
            f.write(f'{command}\n')
    pprint(command_list)
