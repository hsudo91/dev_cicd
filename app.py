from flask import Flask
# test
app = Flask(__name__)

@app.route('/')
def hello():
    return 'CI/CD hsudo!!'
    
if __name__ == '__main__':
    app.run()
