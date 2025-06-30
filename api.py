
from flask import Flask, jsonify, request, Response
from datetime import datetime
import csv

calculation_history = []

app = Flask(__name__)
@app.route("/")
def home():

    return jsonify({
        "name":"Aditya Joshi",
        "role":"Software Engineer",
        "message": "Welcome to your first flask API!",
        "id": 4561
    })


@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    result=a+b

    # For keeping track of the calculation history
    
    return jsonify({
           "num1":a,
           "num2":b,
           "result": result
    })


# Route to perform basic arithmetic operations
# This route takes an operation (add, sub, mul, div) and two integers (
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
    

    # For keeping track of the calculation history
    calculation_history.append({
        "operation": operation,
        "num1": a,
        "num2": b,
        "result": result
    })
    # Keep track of the calculation history only last 10 calculations
    if(len(calculation_history) > 10):
        calculation_history.pop(0)

    return jsonify({
        "operation": operation,
        "num1": a,
        "num2": b,
        "result": result
    })



# Route to perform basic arithmetic operations using query parameters
@app.route("/api/calculate")
def calculate_query():
    op=request.args.get('op')
    a=request.args.get('a', type=int)
    b=request.args.get('b', type=int)
    # Validate the operation


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

@app.route("/api")
def api():
    return jsonify({
        "API":"Application Programming Interface",
        "Description":"Basically an API is a way to communicate between diffrent sites where diffrent sites can communicate using some http methods such as GET,POST,DELETE,PUT etc."
    })


# Route with for calculation history
@app.route("/history")
def get_history():
    if not calculation_history:
        return jsonify({
            "message": "No calculations have been performed yet."
        }), 404
    
    return jsonify({
        "history": calculation_history
    })

# Route to clear the calculation history
# This will reset the calculation_history list to an empty list
@app.route("/history/clear")
def clear_history():
   
    global calculation_history

    if len(calculation_history) == 0:
        return jsonify({
            "message": "Calculation history is already empty."
        }), 404
    
    calculation_history = []
    return jsonify({
        "message": "Calculation history cleared."
    })



# Route to greet a user by name
# This route takes a name as a URL parameter and returns a greeting message
@app.route("/greet/<name>")
def greet(name):
    return jsonify({
        "greeting":f"Hello , {name} ! "
    })


# Route to submit user data
# This route accepts user data via query parameters and stores it in a list
user_data = []
@app.route("/submit")
def submit_user():
    
    name=request.args.get('name')
    role=request.args.get('role')
    message=request.args.get('message')
    id=request.args.get('id')


    if not all([name,role,message,id]):
        return jsonify({
            "error":"All fields are required: name, role, message, id"
        }), 400
    
    timestamp =datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
    entry={
        "id":id,
        "name":name,
        "role":role,
        "message":message,
        "timestamp":timestamp
    }

    user_data.append(entry)
    
    return jsonify( {
        "message": "Data submitted successfully",
        "data": entry
    })


# Route to retrieve user history
# This route returns the list of user data submitted via the /submit route
@app.route("/user_history")
def user_history():
    if not user_data:
        return jsonify({
            "message": "No user data available."
        }), 404
    
    return jsonify({
        "user_data": user_data[::-1]
    })


# Export route to export the pdf

@app.route("/export")
def export_csv():
    def generate():
        yield 'id,name,role,timestamp,message\n'
        for entry in user_data:
            line=f"{entry['id']},{entry['name']},{entry['role']},{entry['timestamp']},{entry['message']}\n"
            yield line
    return Response(generate(),mimetype='text/csv',
                    headers={
                            "Content-Disposition":"attachment;filename=user_data.csv"
                            }
                        
                        )



    

if __name__ == '__main__':

    app.run(debug=True)