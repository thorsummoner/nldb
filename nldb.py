
import collections
import os
import sqlite3

class Video(object):
    def __init__(self, youtube_id):
        super(Video, self).__init__()
        self.youtube_id = youtube_id

    @property
    def youtube_url(self):
        return 'https://www.youtube.com/watch?v=' + self.youtube_id


class NlDatabase(object):
    DATABASE_FILE = './nl.db'
    SCHEEMA = {
        'videos': collections.OrderedDict([
            ('youtube_id',           'TEXT PRIMARY KEY'),
            ('release_date_ISO8601', 'TEXT'),
            ('runtime_seconds',      'NUMERIC'),
            ('thumbnail_url',        'TEXT'),
            ('title',                'TEXT'),
        ]),
        'videos_nl': collections.OrderedDict([
            ('youtube_id',      'TEXT PRIMARY KEY'),
            ('enjoyment_score', 'NUMERIC'),
            ('insanity_score',  'NUMERIC'),
            ('power_score',     'NUMERIC'),
        ]),
        'videos_caption': collections.OrderedDict([
            ('youtube_id',      'TEXT PRIMARY KEY'),
            ('nocaption',       'BOOL'),
            ('ttml',            'TEXT'),
            ('plaintext',       'TEXT'),
        ]),
        'word_rank': collections.OrderedDict([
            ('word',            'TEXT PRIMARY KEY'),
            ('occurances',      'NUMERIC'),
        ]),
    }

    def __init__(self, auto_commit=False):
        super(NlDatabase, self).__init__()

        self.auto_commit = auto_commit

    def __enter__(self):
        self.connection = sqlite3.connect(self.DATABASE_FILE)
        self.cursor = self.connection.cursor()

        return self.cursor

    def __exit__(self, *_):
        if self.auto_commit:
            self.connection.commit()
        self.connection.close()

    def init_scheema(self):
        with self as cursor:
            for table, columns in self.SCHEEMA.iteritems():
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS `{table}` ({columns})'.format(
                        table=table,
                        columns=', '.join([
                            '`{}` {}'.format(k, v)
                            for k, v in columns.iteritems()
                        ]),
                    )
                )
            self.connection.commit()

    def init_scheema_once(self):
        if not os.path.isfile(self.DATABASE_FILE):
            self.init_scheema()


    def insert_dict(self, table, data):
        with self as cursor:
            cursor.execute(
                (
                    'INSERT OR REPLACE '
                    'INTO `{table}` ({columns}) '
                    'VALUES ({values}) '
                ).format(
                    table=table,
                    columns=', '.join([
                        '`{}`'.format(key) for key in data.keys()
                    ]),
                    values=', '.join(['?'] * len(data)),
                ),
                data.values()
            )
