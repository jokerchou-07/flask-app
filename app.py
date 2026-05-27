from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# ==========================================
# Exercise 43: Flask Online (首頁)
# 路由: /
# ==========================================
@app.route('/')
def ex43_index():
    return 'Index Page'

# ==========================================
# Exercise 44: Routing & Variable Rules (動態路由)
# 路由: /user/<username>  (例如: /user/Kevin)
# ==========================================
@app.route('/user/<username>')
def ex44_show_user_profile(username):
    return f'User: {username}'

# ==========================================
# Exercise 45: HTTP Methods (GET/POST 表單處理)
# 路由: /login
# ==========================================
@app.route('/login', methods=['GET', 'POST'])
def ex45_login():
    if request.method == 'POST':
        username = request.form.get('username', 'Guest')
        return f'Logged in as {username} (POST)'
    
    # GET 請求時，返回一個簡單的 HTML 表單供測試
    html_form = '''
    <form method="post">
        Username: <input type="text" name="username">
        <input type="submit" value="Login">
    </form>
    '''
    return render_template_string(html_form)

# ==========================================
# Exercise 46: Static Files (靜態檔案路由說明)
# 路由: /static_demo
# ==========================================
@app.route('/static_demo')
def ex46_static():
    return 'Static files are served from /static folder. Example: /static/style.css'

# ==========================================
# Exercise 47: Rendering Templates (樣式渲染)
# 路由: /hello/ 或 /hello/<name>
# ==========================================
@app.route('/hello/')
@app.route('/hello/<name>')
def ex47_hello(name=None):
    html_template = '''
    <!doctype html>
    <html>
    <head><title>Hello Page</title></head>
    <body>
        {% if name %}
          <h1>Hello {name}!</h1>
        {% else %}
          <h1>Hello, World!</h1>
        {% endif %}
    </body>
    </html>
    '''
    res_html = html_template.replace('{name}', name if name else 'World')
    return render_template_string(res_html)

# ==========================================
# Exercise 48: About JSON (返回 JSON 資料)
# 路由: /api/data
# ==========================================
@app.route('/api/data')
def ex48_json():
    return jsonify({
        "status": "success",
        "message": "This is Exercise 48 JSON response",
        "data": {
            "course": "Web Application Development",
            "date": "2026-05-27"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
