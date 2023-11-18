#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print('hello')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    nums=str()
    for i in range(0,parameter):
        nums += f'{i}\n'
    return nums

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    output = str()
    match operation:
        case '+':
            output = num1+num2
            
        case '-':
            output = num1-num2   
                   
        case 'div':
            try:
                output = num1 / num2
            except ZeroDivisionError:
                return("Error: num2 cannot be equal to 0")  
                  
        case '*':
            output = num1*num2
        
        case '%':
            try:
                output = num1 % num2
            except ZeroDivisionError:
                return("Error: num2 cannot be equal to 0")
            
        case _:
            return "Invalid Operation"

            
    return f"{output}"
    
                
            
    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
