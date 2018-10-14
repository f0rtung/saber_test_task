import os
import io
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .decorators import check_post_method
from .responses import ErrorResponse, SuccessResponse

LOG_NAME = 'jsonl_log.jsonl'
LOG_PATH = os.path.join(settings.BASE_DIR, LOG_NAME)
MAX_READ_LINES = 20


def get_file_total_size(path_to_file):
    file_stat = os.stat(path_to_file)
    return file_stat.st_size


@csrf_exempt
@check_post_method
def read_log(request):
    try:
        offset = int(request.POST['offset'])
        file_total_size = get_file_total_size(LOG_PATH)

        if offset < 0 or offset > file_total_size:
            raise IndexError("Invalid offset param ({})".format(offset))

        if offset == file_total_size:
            response = SuccessResponse(file_total_size, file_total_size, [])
        else:
            with io.open(LOG_PATH, 'rt', encoding='utf-8') as log_file:
                log_file.seek(offset)
                lines = []
                for _ in xrange(MAX_READ_LINES):
                    line = log_file.readline()
                    if not line:
                        break
                    lines.append(json.loads(line))
                new_offset = log_file.tell()
                response = SuccessResponse(new_offset, file_total_size, lines)

    except KeyError as error:
        response = ErrorResponse("Key {} does not exist!".format(str(error)))

    except Exception as error:
        response = ErrorResponse(str(error))

    return response.create_http_response()
