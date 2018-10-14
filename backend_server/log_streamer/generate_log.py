import json
import codecs
from random import choice

LOG_LEVELS = ['DEBUG',
              'INFO',
              'WARN',
              'ERROR']
LOG_MESSAGES = ['Blah blah blah',
                'Everything is fine!',
                'Hmmm, wait...',
                'Holly $@#t!']


def generate_log(log_path, row_count):
    with codecs.open(log_path, 'wt', encoding='utf-8') as log_file:
        for _ in xrange(row_count):
            log_data = {
                'level': choice(LOG_LEVELS),
                'message': choice(LOG_MESSAGES)
            }
            json.dump(log_data, log_file)
            log_file.write('\n')


if __name__ == "__main__":
    generate_log('../jsonl_log.jsonl', 10000)
    print("Finish")
