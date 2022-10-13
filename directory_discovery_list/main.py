
base_dir = '/var/www/html/'
dirs_to_append = []
created_list = []

def create_dir_list():
    with open('directory-list-1.0.txt', 'r') as f:
        for line in f:
            dirs_to_append.append(line)
        for word in dirs_to_append:
            print(word)
            with open('createdlist.txt', 'a+') as fc:
                fc.write(f'{base_dir}{word}')





if __name__ == "__main__":

    create_dir_list()





