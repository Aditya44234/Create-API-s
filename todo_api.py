
from flask import Flask, jsonify, request, Response


app = Flask(__name__)
@app.route("/")
def home():

    return jsonify({
        "name":"Aditya Joshi",
        "role":"Software Engineer",
        "message": "Welcome to your first flask API!",
        "id": 4561
    })


# Another route with GET
@app.route("/greet/<name>")
def greet(name):
    return jsonify({
        "greeting":f"Hello , {name} ! "
    })

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    result=a+b

    return jsonify({
           "num1":a,
           "num2":b,
           "result": result
    })


@app.route("/calculate/<operation>/<int:a>/<int:b>")
def calculate(operation,a,b):
    if(operation == "add"):
        result = a + b
    elif(operation == "sub"):
        result = a-b
    elif(operation == "mul"):
        result = a*b
    elif(operation == "div"):
        if b==0:
            return Response("Division by zero is not allowed", status=400)
        result = a / b
    else:
        return Response("Invalid operation", status=400)
    return jsonify({
        "operation": operation,
        "num1": a,
        "num2": b,
        "result": result
    })


@app.route("/api/calculate")
def calculate_query():
    op=request.args.get('op')
    a=request.args.get('a', type=int)
    b=request.args.get('b', type=int)


    


    if op not in ['add', 'sub', 'mul', 'div']:
        return jsonify({
            "error":"Invalid operation. Supported operations are: add, sub, mul, div"
        }),400
    
    if a is None or b is None:
        return jsonify({
            "error":"Both 'a' and 'b' parameters are required"
        }), 400
   

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        if b == 0:
            return Response("Division by zero is not allowed", status=400)
        result = a / b
    else:
        return Response("Invalid operation", status=400)

    return jsonify({
        "operation": op,
        "num1": a,
        "num2": b,
        "result": result
    })
    

if __name__ == '__main__':

    app.run(debug=True)