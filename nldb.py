
import collections
import os
import sqlite3

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
