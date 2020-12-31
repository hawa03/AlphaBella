from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    name = 'Hawa Jalloh'
    username = 'hawa03'
    return render_template('index.html', data=name, data2 = username)

    
if __name__ == '__main__':
    app.run()
    
    
