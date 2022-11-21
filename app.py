from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'raphael20221118'


@app.route("/")
def root():
    """ 主页 :return: Index.html """
    return render_template('Index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')