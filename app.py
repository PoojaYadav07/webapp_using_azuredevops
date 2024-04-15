from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure Task Status</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .message {
                font-size: 48px;
                color: #0078D4; /* Azure's official color */
            }
        </style>
    </head>
    <body>
        <div class="message">AZURE TASK COMPLETED</div>
    </body>
    </html>
    '''
    return render_template_string(html)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
