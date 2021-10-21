from flask import Flask, jsonify, request
import csv
allmovies = []

with open('movies.csv',encoding ='utf8' )as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

likedmovies = []
dislikedmovies = []
notwatched = []

app = Flask(__name__)

@app.route('/get-movie')
def getmovie():
    return jsonify({ 'data':allmovies[0], 'status':'success'})

@app.route('/liked-movie', methods = ['POST'])
def likedmovies():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    likedmovies.append(movie)
    return jsonify({ 'status':'success'})

@app.route('/disliked-movie', methods = ['POST'])
def dislikedmovies():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    dislikedmovies.append(movie)
    return jsonify({ 'status':'success'}) 

@app.route('/notwatched-movie', methods = ['POST'])
def notwatched():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    notwatched.append(movie)
    return jsonify({ 'status':'success'})    










if __name__ == '__main__':
    app.run()