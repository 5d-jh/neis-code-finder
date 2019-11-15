# NEIS code finder API 가이드
## 요청
GET `https://www.schoolcodekr.ml/api`

### 요청 예시
```python
import requests
import json
url = 'https://www.schoolcodekr.ml/api?q=한국학교'
response = requests.get(url)
school_infos = json.loads(response.text)
print(school_infos)
```

### 쿼리 파라미터
|이름|필수 여부|값(자료형)|
|:--:|:--:|:--:|
|`q`|필수|학교 이름(문자열)|

페이지 당 최대 20개의 정보를 불러옵니다.

## 응답
Content-Type: `application/json`

### 응답 예시
```json
{
    "school_infos": [
        {
            "code": "X123456789",
            "address": "서울시...",
            "name": "OO학교",
            "type": "elementary"
        }, {
            "code": "X987654321",
            "address": "부산시...",
            "name": "XX학교",
            "type": "middle"
        }
    ],
    "server_message": {
        "all_loaded": true
    }
}
```

### 응답 정의
|아이템|설명|데이터 설명|
|:--:|:--:|:--:|
|`school_infos.type`|학교 종류|`elementary`, `middle`, `high`, `special` 중 하나인 문자열입니다.|
|`school_infos.code`|NEIS 코드|첫 자리가 알파벳이고 나머지가 숫자인 열 자리 문자열입니다.|
|`school_infos.address`|학교 주소|학교의 소재지입니다.|
|`school_infos.name`|학교 이름|학교의 이름입니다.|
|`server_message.all_loaded`|전부 다 불러왔는지 여부|학교 정보가 `school_infos`에 있는 것이 전부라면 `true`, 아니면 `false` 입니다.|

elementary는 초등학교, middle은 중학교, high는 고등학교, special은 특수학교 입니다.
