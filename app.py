from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Exercise 43: Flask Online
@app.route('/')
def ex43_index():
    return 'Index Page'

# Exercise 44: Routing & Variable Rules
@app.route('/user/<username>')
def ex44_show_user_profile(username):
    return f'User: {username}'

# Exercise 45: HTTP Methods
@app.route('/login', methods=['GET', 'POST'])
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

# Exercise 46: Static Files
@app.route('/static_demo')
def ex46_static():
    return 'Static files are served from /static folder. Example: /static/style.css'

# Exercise 47: Rendering Templates
@app.route('/hello/')
@app.route('/hello/<name>')
def ex47_hello(name=None):
    html_template = '''
    <!doctype html>
    <html>
    <head><title>Hello Page</title></head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>
    '''
    if name:
        html_template = html_template.replace('World', name)
    return render_template_string(html_template)

# Exercise 48: About JSON
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
