from flask import Flask, render_template, request, jsonify
import get_code

app = Flask(__name__)

@app.route('/')
def get_page():
    query = request.args.get('q')
    page = request.args.get('page')
    return render_template(
        'index.html',
        school_infos = query and get_code.get(query, page),
            #query변수의 값이 있을 경우 get_code.get()함수 호출     
        query = query or '',
            #query변수의 값이 없을 경우 비어 있는 문자열을 넘겨줌
        page = int(page) if page else 1
    )

@app.route('/api')
def get_json():
    query = request.args.get('q')
    page = request.args.get('page')
    return jsonify(school_infos=get_code.get(query, page) if query else [])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)