from app import app, db
from flask import jsonify, request, redirect, url_for
from billboard import ChartData #issue with this module
import requests
from bs4 import BeautifulSoup
from app.models import User
import time
import jwt

@app.route('/')
@app.route('/index')
def index():
    return ''


@app.route('/api/retrieve', methods=['GET'])
def retrieve():

    try:
        page = requests.get('https://www.billboard.com/charts/hot-100')

        soup = BeautifulSoup(page.content, 'html.parser')


        names = soup.find_all('div', attrs={"chart-list-item__artist"})
        titles = soup.find_all('span', attrs={"chart-list-item__title-text"})
        ranks = soup.find_all('div', attrs={"chart-list-item__rank"})
        div_tags = soup.find_all('div', attrs={"chart-list-item__image-wrapper"})

        names_list = []
        titles_list = []
        ranks_list = []
        image_list =[]
        song_elements =[]

        for tag in div_tags:
            img_tag = tag.find_all('img', attrs={"chart-list-item__image"})
            for tag in img_tag:
                try:
                    image_list.append(tag['data-src'])
                except:
                    image_list.append('https://assets.billboard.com/assets/1565881383/images/charts/bb-placeholder-new.jpg?f5cede3a841850a742ad')

        for title in titles:
            titles_list.append(title.get_text().strip())


        for name in names:
            names_list.append(name.get_text().strip())

        for rank in ranks:
             ranks_list.append(rank.get_text().strip())

        for rank, name, title, image in zip(ranks_list, names_list, titles_list, image_list):
            song_elements.append({'rank': rank, 'artist': name, 'title': title, 'image': image})

        print(song_elements)

        return jsonify({ 'Success': song_elements })
    except:
        return jsonify({ 'Error': 'There is an issue that needs to be solved. '})



@app.route('/api/login')
def login():
    try:
        token = request.headers.get('token')

        print(token)

        # decode the token back to a dictionary
        data = jwt.decode(
            token,
            app.config['SECRET_KEY'],
            algorithm=['HS256']
        )

        print(data)

        # query db to get user and check pass
        user = User.query.filter_by(email=data['email']).first()

        # if user doesn't exist or password incorrect, send fail msg
        if user is None or not user.check_password(data['password']):
            return jsonify({ 'message': 'Error #002: Invalid credentials' })

        # create a token and return it
        return jsonify({ 'message': 'success', 'token': user.get_token() })
    except:
        return jsonify({ 'message': 'Error #003: Failure to login' })


@app.route('/api/register')
def register():

    try:

        token = request.headers.get('token')


        data = jwt.decode(
            token,
            app.config['SECRET_KEY'],
            algorithm=['HS256']
        )

        user = User(email=data['email'])
        user.set_password(data['password'])

        db.session.add(user)
        db.session.commit()


        return jsonify({ 'message': 'success'})
    except:
        return jsonify({ 'Error': 'Error #004: Failure to register' })
        #****** route for Billboard.py package *******
    # try:
    # chart = ChartData('hot-100')
    #
    # if chart == []:
    #     return jsonify({ 'Error': {
    #     'empty': chart }})
    #
    # clist = []
    #
    # #iterating through the list of songs
    # for c in chart:
    #     blist = {
    #     'title': c.title,
    #     'artist': c.artist
    #     }
    #     clist.append(blist)
    # return jsonify({ 'Success': {
    # 'data': clist
    # }})

    # except:
    #     return jsonify({ 'Error': 'Could not grab data.'})
