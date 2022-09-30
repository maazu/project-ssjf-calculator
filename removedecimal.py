import argparse


def remove_decimal(content):
    return content.replace('.', '')


def save_data_file(path, data_content):
    try:
        with open(path, 'w') as a:
            a.write(data_content)
        print('Result file has been written successfully')
    except Exception as e:
        print('Error', str(e))


def read_file_content(path):
    try:
        with open(path) as f:
            
            data = f.read()
            return data

    except Exception as e:
        print('File reading error occurred', str(e))
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Execute Step 3 of the program.')

    parser.add_argument('--file', type=str,
                        help='Enter a file name')

    parser.add_argument('--savepath', type=str,
                        help='Enter file save path')

    args = parser.parse_args()

    file = args.file
    path = args.savepath

    content = read_file_content(file)
    content = remove_decimal(content)
    save_data_file(path, content)
