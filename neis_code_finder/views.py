from django.shortcuts import render
from django.http import JsonResponse
from . import get_code

def get_page(req):
    template_data = {}
    if 'q' in req.GET:
        template_data['school_infos'] = get_code.get(req.GET['q'])
        template_data['query'] = req.GET['q']

    return render(req, 'neis_code_finder/main.html', template_data)

def get_data(req):
    json_data = {}
    if 'q' in req.GET:
        json_data['school_infos'] = get_code.get(req.GET['q'])
    else:
        json_data['school_infos'] = []
    
    return JsonResponse(json_data)