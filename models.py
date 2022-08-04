from peewee import *
from datetime import datetime

db = PostgresqlDatabase(
    'second_flask_app',
    host = 'localhost',
    port = '5432',
    user = 'saske',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    name = CharField(max_length=255, null=False)
    family = CharField(max_length=255, null=False)
    date = DateField(default=datetime.now)
    Email = CharField(max_length=55, null=False)
    password = CharField(max_length=55, null=False)

    def __repr__(self):
        return self.name

db.create_tables([Post])
# 
# Post.create(name='Atai', family='Boomer')

db.close()