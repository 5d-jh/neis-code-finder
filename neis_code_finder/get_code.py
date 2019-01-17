import re
import requests

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

    # print(r.text)

    results_code = re.findall(r'searchSchul\(\'([A-Za-z0-9_]+)\'\)', r.text)
    results_code = results_code[::2]

    results_address = re.findall(r'학교주소<\/span>(.*)<\/li>', r.text)
    if len(results_address) != 0:
        results_address.pop()

    iters_num = len(results_code)
    results = []
    for i in range(iters_num):
        results.append({
            'code': results_code[i],
            'address': results_address[i]
        })
        
    return results