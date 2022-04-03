from flask import Flask, render_template, request, redirect
from config import Pages, Saves, STRATEGY_DICT

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        print('Ебать')
        req = request.form
        strategy = req['strategy']
        req.pop('strategy')
        params = list(req.values())

        exec_strategy = STRATEGY_DICT[strategy](*params)
        exec_strategy.simulation()
        out = exec_strategy.history
        return redirect('/redir')
    else:
        return render_template('index.html')


@app.route('/index.html', methods=('GET', 'POST'))
def indexh():
    if request.method == 'POST':
        print('Ебать')
        req = request.form
        print(req)
        # strategy = req['strategy']
        # req.pop('strategy')
        # params = list(req.values())
        #
        # exec_strategy = STRATEGY_DICT[strategy](*params)
        # exec_strategy.simulation()
        # out = exec_strategy.history
        return redirect('/redir')
    else:
        return render_template('index.html')
#
# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/redir')
def redir():
    stock_img_path = 'static/img/ContentFon.png'
    return render_template(Pages.redir,)


app.run(debug=True)
