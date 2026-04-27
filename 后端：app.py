from flask import Flask, render_template_string, request, jsonify
import requests
import json

app = Flask(__name__)

# 前端页面
@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

# Pinterest 无翻墙搜索 API（GitHub开源公共接口）
@app.route('/api/pinterest')
def search_pinterest():
    keyword = request.args.get('q', 'design')
    url = f"https://pinterest-api.vercel.app/search?keyword={keyword}"
    
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        return jsonify(data)
    except:
        return jsonify({"code": 500, "data": []})

# Behance 无翻墙搜索 API
@app.route('/api/behance')
def search_behance():
    keyword = request.args.get('q', 'design')
    url = f"https://behance-api.vercel.app/search?q={keyword}"
    
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        return jsonify(data)
    except:
        return jsonify({"code": 500, "data": []})

if __name__ == '__main__':
    print("✅ 网站已启动！打开浏览器访问：http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
