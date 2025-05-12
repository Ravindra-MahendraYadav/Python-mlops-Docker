from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML templates
form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome App</title>
</head>
<body>
    <h2>Enter your name</h2>
    <form method="post">
        <input type="text" name="username" placeholder="Your Name" required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

welcome_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h2>Welcome, {{ name }}!</h2>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        return render_template_string(welcome_html, name=username)
    return form_html

if __name__ == '__main__':
    app.run(debug=True, port=5000)
