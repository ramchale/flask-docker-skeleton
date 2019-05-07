from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def default_route():
    return 'This is just returning a string'


@app.route('/test')
def test():
    return render_template('test.html')


# If the app is started with UWSGI this will get skipped
if __name__ == '__main__':
    # TODO - Explain this
    app.run(debug=True, port=80, host='0.0.0.0')
