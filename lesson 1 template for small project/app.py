from flask import Flask 
app = Flask(__name__)

print(app)
print(__name__)

@app.route('/')
def index(): 
    return "welcom !"

if  __name__ == '__main__':
    app.run(debug=True)