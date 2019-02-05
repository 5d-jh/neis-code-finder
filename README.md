# neis_code_finder
## api
### 요청 URI
`https://code.schoolmenukr.ml/api/?q=[학교 이름]`

### 응답 예시
```json
{
    "school_infos": [
        {
            "code": "X123456789",
            "address": "서울시...",
            "name": "OO학교",
            "type": "elementary || middle || high"
        }, {
            "code": "X987654321",
            "address": "부산시...",
            "name": "XX학교",
            "type": "elementary || middle || high"
        }
    ]
}
```
