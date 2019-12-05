import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse


class ResponseMessage:
    result = False
    code = 200
    message = None
    content = None

    def __init__(self, result=False, code=200, message=None, content=None):
        self.result = result
        self.code = code
        self.message = message
        self.content = content
def render_json(obj):
    if isinstance(obj, (list, dict, tuple)):
        return HttpResponse(json.dumps(obj, cls=DjangoJSONEncoder, ensure_ascii=False),
                            content_type='application/json')
    else:
        return HttpResponse(json.dumps(obj.__dict__, cls=DjangoJSONEncoder, ensure_ascii=False),
                            content_type='application/json')