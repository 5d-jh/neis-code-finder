import logging

import azure.functions as func
from jinja2 import Template
from ..school_info import get_data

def main(req: func.HttpRequest) -> func.HttpResponse:
    query = req.params.get('q') or ''
    page = int(req.params.get('page') or 1)

    data = get_data(query)

    f = open("app/index.html", "r")
    html = f.read()

    tm = Template(html)
    rendered = tm.render(
        query=query,
        page=page,
        school_infos=data[0],
        is_all=data[1]
    )

    f.close()
    
    return func.HttpResponse(body=rendered, headers={"Content-Type": "text/html;"})
