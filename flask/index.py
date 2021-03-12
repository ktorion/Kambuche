from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('home.html')

def about():
    return render_template ('sobremi.html')
def portfolio():
    return render_template ('portafolio.html')

def skills():
    return render_template ('skills')

if __name__ == '__main__':
    app.run(debug=True)


