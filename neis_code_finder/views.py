from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import get_code
import os

def get_page(req):
    template_data = {}
    if 'q' in req.GET:
        page =  req.GET['page'] if 'page' in req.GET else None
        template_data['school_infos'] = get_code.get(req.GET['q'], page)
        template_data['query'] = req.GET['q']

    return render(req, 'neis_code_finder/main.html', template_data)

def get_data(req):
    json_data = {}
    if 'q' in req.GET:
        page =  req.GET['page'] if 'page' in req.GET else None
        json_data['school_infos'] = get_code.get(req.GET['q'], page)
    else:
        json_data['school_infos'] = []
    
    return JsonResponse(json_data)

def get_fav(req):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    return HttpResponse(
        open(dir_path+'/favicon.png', 'rb').read(),
        content_type='image/png'
    )