def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return print(file_contents)

def get_num_words(path_to_file):
    with open(path_to_file) as f:
        count = 0
        file_contents = f.read()
        split = file_contents.split()
        for i in split:
            count += 1
    return count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return print(file_contents)

def get_number_letters(path_to_file):
    new = {}
    with open(path_to_file) as f:
        file_contents = f.read().lower()
        split = file_contents.split()
        for i in split:
            for x in i:
                if x not in new:
                    new[x] = 1
                else:
                    new[x] += 1
    return new

def sort(item):
    return item["num"]

def report(path_to_file):
    new_list = []
    for i in get_number_letters(path_to_file):
        new_list.append({"char": i, "num": get_number_letters(path_to_file)[i]})
    new_list.sort(reverse=True, key=sort)
    return new_list