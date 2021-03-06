from flask import Flask, render_template, request, redirect, session
from config import Pages, Saves, STRATEGY_DICT
from utils import str2date

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
        strategy = req['hidden']
        params = dict(req)
        start_money = int(params['start_money_count'])
        params.pop('start_money_count')
        params.pop('hidden')
        params['start_date'] = str2date(params['start_date'])
        params['end_date'] = str2date(params['end_date'])

        redir_data = {}
        ticket = params['ticket']
        redir_data['start_money_count'] = start_money
        redir_data['ticket'] = ticket

        for k in params.keys():
            if k == 'ticket':
                continue
            if type(params[k]) is str:
                params[k] = float(params[k])

        exec_strategy = STRATEGY_DICT[strategy](**params)
        history, amount, close = exec_strategy.simulation()
        print(history)

        total_money = round(exec_strategy.count_bills(int(start_money)))
        profit = round(total_money - start_money)
        print(amount)
        value = (total_money / close) * amount  # это количество акций, номинально
        redir_data['total_money'] = total_money
        redir_data['profit'] = profit
        redir_data['value'] = value
        session['redir_data'] = redir_data

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
    if 'redir_data' in session:
        return render_template(Pages.redir, **session['redir_data'])


app.secret_key = 'Hello World'
app.config['SESSION_TYPE'] = 'filesystem'
app.run(debug=True)
