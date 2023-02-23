from flask import Flask, request ,render_template , jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/math', methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        elif ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        elif ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        elif ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
        return render_template('results.html' , result = result)



"""
body > raw > json
{ "operation": "add", "num1": 1, "num2": 2 }
"""
@app.route('/postman_action', methods=['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        elif ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        elif ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        elif ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
        return jsonify(result)


@app.route('/details')
def get_details():
    name = request.args.get('n1')
    print(name)
    result = f'Hi this is {name}'
    return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
