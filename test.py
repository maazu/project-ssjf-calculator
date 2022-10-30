def read_file_content(path):

    try:
        with open(path) as f:
            print('reading file........')
            data = f.read()
            data = data.replace('.', '')
            print('finished reading file........')
            return data

    except Exception as e:
        print('File reading error occurred', str(e))
        return False


TESTNUMBER = read_file_content('./data/billion-long/1-bill.txt')

MOD_NUMER = 36

MOD_LIMITS_LIST = []
