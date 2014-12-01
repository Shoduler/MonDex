import os
baseDir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(baseDir, "mon.sql")
CSRF_ENABLED = True
SECRET_KEY = "development key"