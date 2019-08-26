from app import app
from flask import jsonify
from billboard import ChartData


@app.route('/')
@app.route('/index')
def index():
    return ''

@app.route('/api/retrieve', methods=['GET'])
def retrieve():

    chart = ChartData('hot-100')

    if chart == []:
        return jsonify({ 'Error': {
        'empty': chart }})

    clist = []

    #iterating through the list of songs
    for c in chart:
        blist = {
        'title': c.title,
        'artist': c.artist
        }
        clist.append(blist)
    return jsonify({ 'Success': {
    'data': clist
    }})

    # except:
    #     return jsonify({ 'Error': 'Could not grab data.'})
