from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

if __name__ == '__main__':
    # 這裡的 port 設定能確保你在本地測試時正常運作
    app.run(host='0.0.0.0', port=5000, debug=True)
