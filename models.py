"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://i.pinimg.com/1200x/9f/dd/8f/9fdd8ff262a58cfc71f660792a974c44.jpg"

class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """Connect this database to provided Flask app.
    """

    db.app = app
    db.init_app(app)

