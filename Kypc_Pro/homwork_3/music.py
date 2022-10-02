import sqlite3
from flask import Flask, render_template, request
from model import Executor, Song

app = Flask(__name__)


@app.route('/', methods=['get'])
def main_music_list():
    context = {'songs': Song.select()}
    return f'Here is a list from which you may find something for yourself{render_template("music_library.html", **context)}'


@app.route('/add/music', methods=['get', 'post'])
def music_add():
    context = {'executor': Executor.select()}
    if request.method == 'POST':
        Song(
            name=request.form['name'],
            executor=request.form['executor'],
            lasting=request.form['lasting']
        ).save()

    return render_template('add_music.html', **context)


@app.route('/delete/music', methods=['get', 'post'])
def music_delete():
    context = {'songs': Song.select()}
    if request.method == 'POST':
        Song.select().where(Song.id == request.form["songs"]).delete
        return render_template('music_delete.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
