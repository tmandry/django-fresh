from django.template.response import TemplateResponse
from django.http import HttpResponse

import json

from .models import LastChange


def home(request):
    return TemplateResponse(request, 'core/home.html', None)


def refresher(request):
    changes = LastChange.objects.filter(refreshed=False)
    if changes:
        for change in changes:
            print change
            change.refreshed = True
            change.save()
        refresh = True
    else:
        refresh = False

    return HttpResponse(json.dumps({'refresh': refresh}), mimetype='application/json')
