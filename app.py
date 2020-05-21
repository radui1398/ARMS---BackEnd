from flask import Flask, escape, request, jsonify, Response

from scrapper import load_tweets

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    try:
        d = int(request.args.get('d'))
        m = int(request.args.get('m'))
        y = int(request.args.get('y'))
        country = request.args.get('country')

        tweets = load_tweets(d, m, y, country)

        if len(tweets) == 0:
            return Response({'Nothing found.'}, status=404, mimetype='application/json')

        data = {'data': tweets}

        return data
    except Exception as e:
        print(e)
        return Response("Invalid request.", status=400, mimetype='application/json')


app.run()
