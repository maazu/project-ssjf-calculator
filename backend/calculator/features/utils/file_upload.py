import os
import sys
from urllib import request
from django.conf import settings
from datetime import datetime


def handle_fileupload(payload, file_name):
    TIMESTAMP = datetime.now().strftime("%Y-%m-%d-%I-%M-%S-%p")
    print(payload)
    uploaded_file = payload[file_name]
    cal_function = payload['calFunction']
    path = os.path.join(settings.MEDIA_ROOT,
                        str(TIMESTAMP) + '-' + cal_function + '-' + uploaded_file.name)

    with open(path, 'w') as infile:
        str_repr = uploaded_file.read().decode()
        infile.write(str_repr)

    return path


def initialise_file_content(file_path):
    # Open a file
    file = os.open(file_path, os.O_RDWR)

    # Reading text
    file_content = os.read(file, 100000000000)
    file_content = file_content.decode()

    os.close(file)

    return file_content


def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater
