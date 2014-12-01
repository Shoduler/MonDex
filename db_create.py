from config import SQLALCHEMY_DATABASE_URI
from app import db, models

db.create_all()

db.session.add(models.Mon(id = 1,
    name = "Bulbasaur",
    desc = "The seed on its back is filled with nutrients. The seed grows steadily larger as its body grows.",
    type = "GRASS"))

db.session.add(models.Mon(id = 4,
    name = "Charmander",
    desc = "The flame on its tail shows the strength of its life force. If it is weak, the flame also burns weakly.",
    type = "FIRE"))

db.session.add(models.Mon(id = 7,
    name = "Squirtle",
    desc = "The shell is soft when it is born. It soon becomes so resilient, prodding fingers will bounce off it.",
    type = "WATER"))

db.session.commit()