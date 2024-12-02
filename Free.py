def read_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def fillter_keyword(keyword):
    while True:
        line = (yield)
        if keyword in line:
            yield line

def to_uppercase(filtered_lines):
    for line in filtered_lines:
        yield line.upper()

def process_file(filename, keyword):
    line_generator = read_lines(filename)
    filter_coroutine = fillter_keyword(keyword)

    next(filter_coroutine)

    for line in line_generator:
        filter_line = filter_line(line)
        if filter_line:
            for upper_line in to_uppercase(filter_line):
                print(upper_line)

if __name__ == "__main__":
    process_file("example.txt", "pypthon")