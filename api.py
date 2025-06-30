

from flask import Flask,jsonify,request,Response


app = Flask(__name__)

@app.route("/")

def home():
    return jsonify(
        {
        "message": "Welcome to your first flask API!",
        "id":4561

        }
    )


# Another route with GET
@app.route('/greet/<name>')

def greet(name):
    return jsonify({
        "greeting":f"Hello , {name} ! "
    })


@app.route('/add',methods=['POST'])

def add_nums():
    data=request.get_json()
    a=data.get('a',0)
    b=data.get('b',0)
    
    return jsonify({
        "result":a+b
    })



if __name__=='__main__':
    app.run(debug=True)

