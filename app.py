from flask import Flask, request, render_template_string

app = Flask(__name__)

# 根目錄：做一個簡單的導覽頁面，方便教授批改點擊
@app.route('/')
def index():
    return '''
    <h1>Flask Exercises (43 - 48)</h1>
    <ul>
        <li><a href="/ex43">Exercise 43: Index Page</a></li>
        <li><a href="/ex44">Exercise 44: Hello Flask</a></li>
        <li><a href="/ex45">Exercise 45: HTTP Methods (Login)</a></li>
        <li><a href="/ex46/home">Exercise 46: Load HTML (Home)</a></li>
        <li><a href="/ex46/Apple">Exercise 46: Load HTML (Apple)</a></li>
        <li><a href="/ex47/Kevin">Exercise 47: Rendering Templates (Hello Name)</a></li>
        <li><a href="/ex48">Exercise 48: Compute Double</a></li>
    </ul>
    '''

# ==========================================
# Exercise 43: Flask Online (Index Page)
# ==========================================
@app.route('/ex43')
def ex43_index():
    return 'Index Page'

# ==========================================
# Exercise 44: Hello Flask (對應截圖 2)
# ==========================================
@app.route('/ex44')
def ex44_hello():
    return 'Hello, World!'

# ==========================================
# Exercise 45: HTTP Methods
# ==========================================
@app.route('/ex45', methods=['GET', 'POST'])
def ex45_login():
    if request.method == 'POST':
        username = request.form.get('username', 'Guest')
        return f'Logged in as {username} (POST)'
    
    html_form = '''
    <form method="post">
        Username: <input type="text" name="username">
        <input type="submit" value="Login">
    </form>
    '''
    return render_template_string(html_form)

# ==========================================
# Exercise 46: Flask Load HTML (對應截圖 1)
# ==========================================
@app.route('/ex46/home')
def ex46_home():
    # 呈現文字與表格
    html_content = '''
    <h1>My Website Text</h1>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr><td>Text Text Text</td><td>Text Text Text</td><td>Text Text Text</td></tr>
        <tr><td>Text Text Text</td><td>Text Text Text</td><td>Text Text Text</td></tr>
        <tr><td>Text Text Text</td><td>Text Text Text</td><td>Text Text Text</td></tr>
    </table>
    '''
    return render_template_string(html_content)

@app.route('/ex46/Apple')
def ex46_apple():
    # 呈現蘋果圖片 (直接使用網路圖片網址，避免 static 資料夾找不到圖片的問題)
    html_content = '''
    <img src="https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg" alt="Apple" width="300">
    '''
    return render_template_string(html_content)

# ==========================================
# Exercise 47: Rendering Templates (Variable Rules)
# ==========================================
@app.route('/ex47/')
@app.route('/ex47/<name>')
def ex47_hello(name="World"):
    return f'<h1>Hello, {name}!</h1>'

# ==========================================
# Exercise 48: Show double of inputted number (對應截圖 3)
# ==========================================
# 共用的 HTML 模板
ex48_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Simple Flask Form (Compute the double)</title>
</head>
<body>
    <h2>Input a number</h2>
    <form action="/ex48/predict" method="post">
        <input type="number" name="x" required>
        <button type="submit">Submit</button>
    </form>
    
    {% if result is not none %}
        <h3>Double Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
'''

@app.route('/ex48')
def ex48_index():
    # 初始頁面，不顯示結果
    return render_template_string(ex48_template, result=None)

@app.route('/ex48/predict', methods=['POST'])
def ex48_predict():
    # 接收表單資料並計算兩倍
    x = int(request.form['x'])
    result = x * 2
    return render_template_string(ex48_template, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
