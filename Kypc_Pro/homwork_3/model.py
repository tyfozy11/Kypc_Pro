import peewee

db = peewee.SqliteDatabase('peewee_music_library.sqlite3')


class Executor(peewee.Model):
    name = peewee.CharField()
    genre = peewee.CharField()

    class Meta:
        database = db


class Song(peewee.Model):
    name = peewee.CharField()
    lasting = peewee.IntegerField()
    executor = peewee.ForeignKeyField(Executor)

    class Meta:
        database = db


if __name__ == '__main__':
    db.create_tables([Executor, Song])
