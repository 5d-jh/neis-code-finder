import re
import requests
from bs4 import BeautifulSoup

def get(school):
    uri = 'https://www.schoolinfo.go.kr/ei/ss/Pneiss_f01_l0.do'
    form = {
        "SEARCH_GS_HANGMOK_CD": "",
        "SEARCH_GS_HANGMOK_NM": "",
        "SEARCH_SCHUL_NM": school.encode('EUC-KR'),
        "SEARCH_GS_BURYU_CD": "",
        "SEARCH_KEYWORD": school.encode('EUC-KR')
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.post(uri, data=form, headers=headers)

    soup = BeautifulSoup(r.text)
    school_infos = soup.find_all(class_="SchoolList")

    reg_code = r'searchSchul\(\'([A-Za-z0-9_]+)\'\)'
    results_code = [re.findall(reg_code, str(info.a))[0] for info in school_infos]

    results_name = [info.a.string for info in school_infos]
    
    reg_addr = r'<\/span>(.*)<\/li>'
    results_address = [str(info.find_all('li')[1]) for info in school_infos]
    results_address = [re.findall(reg_addr, addr)[0] for addr in results_address]

    school_types = {
        '초': 'elementary',
        '중': 'middle',
        '고': 'high'
    }
    results_type = [info.find_all(class_="mapD_Class")[0].string for info in school_infos]
    results_type = [school_types[sch_type] for sch_type in results_type]

    iters_num = len(results_code)
    results = []
    for i in range(iters_num):
        results.append({
            'code': results_code[i],
            'address': results_address[i],
            'name': results_name[i],
            'type': results_type[i]
        })

    return results