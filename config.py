import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Flask application config
    ------------------------
    """
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning
    # set size limit for upload files
    MAX_CONTENT_LENGTH = 3 * 1000 * 1000
    # Upload paths
    UPLOAD_PATH = os.path.join('app/static/images')