import io
import scipy.stats as stats
import matplotlib.pyplot as graph

from flask import Flask, render_template, make_response


app = Flask(__name__)
graph.style.use('fivethirtyeight')


@app.route('/simple.png')
def simple_image():
    # Generate data
    x = stats.norm(0, 1).rvs(25)
    y = x + stats.norm(0, 1).rvs(len(x))

    # Generate graph
    graph.plot(x, y, 'o')
    buffer = io.BytesIO()
    graph.savefig(buffer, format='png')
    buffer.seek(0)
    graph.close()

    # Create response for the web
    response = make_response(buffer.getvalue())
    response.mimetype = 'image/png'

    return response


@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Flask and Matplotlib'
    )


if __name__ == '__main__':
    import sys

    app.run(debug='d' in sys.argv[-1])