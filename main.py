from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list/<prof>')
def list_prof(list):
    prof = ('инженер-исследователь', 'пилот', 'строитель',
            'экзобиолог', 'врач', 'инженер по терраформированию',
            'климатолог', 'специалист по радиационной защите',
            'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
            'метеоролог', 'оператор марсохода', 'киберинженер',
            'штурман', 'пилот дронов')
    return render_template('list_prof.html', list=list, prof=prof)


if __name__ == '__main__':
    app.run()
