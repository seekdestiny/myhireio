from django.http import HttpResponse
from django.shortcuts import render

from account import models

import json

def talents(request):
    return render(
        request,
        'desktop/talents/talent_list.html',
        {
            'tab': 'talents',
        }
    )

def load_more_talents(request):
    talent_objects = models.Talent.objects.order_by('last_active')

    if not talent_objects:
        return HttpResponse(json.dumps([]), content_type="application/json")

    start = int(request.GET.get('index', 0))
    end = start + 10
    if end > talent_objects.count():
        end = talent_objects.count()
    last_ten_talents = talent_objects[start:end]

    talents = []
    for talent in last_ten_talents:
        serialized_item = talent.serialize()
        talents.append(serialized_item)

    return HttpResponse(json.dumps(talents), content_type="application/json")

