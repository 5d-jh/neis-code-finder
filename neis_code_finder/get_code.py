import requests
import json

def get(school, page_num=1):
    uri = "https://www.schoolinfo.go.kr/ei/ss/Pneiss_f01_l0.do"
    form = {
        "SEARCH_SCHUL_NM": school,
        "pageNumber": page_num,
        "callbackMode": "json",
        "schulCrseScCode": "",
        "hsKndScCode": "",
        "fondScCode": ""
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    r = requests.post(uri, data=form, headers=headers)

    response_json = json.loads(r.text)

    result = []

    for school_info in response_json:
        result.append({
            "code": school_info["SCHUL_CODE"],
            "name": school_info["SCHUL_NM"],
            "type": {
                "02": "elementary",
                "03": "middle",
                "04": "high",
                "05": ""
            }[school_info["SCHUL_CRSE_SC_CODE"]],
            "address": school_info["ADDRESS"]
        })

    return result