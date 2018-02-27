from flask import Flask, render_template, request
app= Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == "__main__":
    app.run(debug = True)