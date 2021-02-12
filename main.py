from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>This is my home page</h1>
    <h2 style='color:red'>Another one</h2>
    '''

@app.route('/page1')
def page1():
    return 'page 1 output'

@app.route('/page1/<variable>')
def page1plus(variable):
    permitted = ['tom', 'sean', 'moroni']
    if variable in permitted:
        return f'The url input was: {variable}'
    else:
        return f'{variable} was not recognised'

@app.route('/control', methods = ['POST', 'GET'])
def control():
    if request.method == 'POST':
        print(request.form)
    else: 
        pass
    return render_template('control.html')

if __name__ == '__main__':
    app.run(
        host = '127.0.0.1',
        port = '8000',
        debug = True,
    )
