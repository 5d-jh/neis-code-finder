# neis_code_finder
## api
### 요청
`http://127.0.0.1:8000/api/?q=[학교 이름]`

### 응답
```json
{
    "school_infos": [
        {
            "code": "X123456789",
            "address": "서울시..."
        }, {
            "code": "X987654321",
            "address": "부산시..."
        }
    ]
}
```
