import json
from abc import abstractmethod, ABCMeta
from django.shortcuts import HttpResponse


class BaseResponse:
    __metaclass__ = ABCMeta

    @abstractmethod
    def as_dict(self):
        pass

    def create_http_response(self):
        dict_response = self.as_dict()
        return HttpResponse(json.dumps(self.as_dict()), status=200)


class ErrorResponse(BaseResponse):
    def __init__(self, error_message):
        self.error_message = error_message

    def as_dict(self):
        return {
            'ok': False,
            'reason': self.error_message
        }


class SuccessResponse(BaseResponse):
    def __init__(self, next_offset, total_size, messages):
        self.next_offset = next_offset
        self.total_size = total_size
        self.messages = messages

    def as_dict(self):
        return {
            'ok': True,
            'next_offset': self.next_offset,
            'total_size': self.total_size,
            'messages': self.messages
        }