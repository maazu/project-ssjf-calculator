import os
from django.conf import settings
from datetime import datetime


def handle_fileupload(payload):
    TIMESTAMP = datetime.now().strftime("%Y-%m-%d-%I-%M-%S-%p")
    uploaded_file = payload.FILES['file']
    cal_function = payload.data['calFunction']
    path = os.path.join(settings.MEDIA_ROOT,
                        str(TIMESTAMP) + '-' + cal_function + '-' + uploaded_file.name)

    with open(path, 'w') as infile:
        str_repr = uploaded_file.read().decode()
        infile.write(str_repr)

    return path
