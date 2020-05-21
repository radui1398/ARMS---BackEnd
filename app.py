from datetime import datetime, timedelta

from flask import Flask, escape, request, jsonify, Response
from flask_cors import CORS

from scrapper import load_tweets

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def default():
    try:
        d = int(request.args.get('d'))
        m = int(request.args.get('m'))
        y = int(request.args.get('y'))
        country = request.args.get('country')

        tweets = load_tweets(d, m, y, country)

        if len(tweets) == 0:
            return Response({'Nothing found.'}, status=404, mimetype='application/json')

        data = {'count': len(tweets), 'data': tweets}

        return data
    except Exception as e:
        print(e)
        return Response("Invalid request.", status=400, mimetype='application/json')

@app.route('/today', methods=['GET'])
def today():
    try:
        now = datetime.now() - timedelta(days=1)
        country = request.args.get('country')
        limit = request.args.get('limit')

        if limit:
            tweets = load_tweets(now.day, now.month, now.year, country, int(limit))
        else:
            tweets = load_tweets(now.day, now.month, now.year, country)

        if len(tweets) == 0:
            return Response({'Nothing found.'}, status=404, mimetype='application/json')

        data = {'count': len(tweets), 'data': tweets}

        return data
    except Exception as e:
        print(e)
        return Response("Invalid request.", status=400, mimetype='application/json')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)