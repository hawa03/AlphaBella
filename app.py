from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = 'Hawa Jalloh'
    
    return render_template('index.html', data=name)
    
if __name__ == '__main__':
    app.run()
    
    
