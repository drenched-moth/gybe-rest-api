from typing import Optional
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql:///:memory:"

db = SQLAlchemy(model_class=Base)

db.init_app(app)

class Concert(Base):
    __tablename__ = 'Concert'

    concertID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date_concert: Mapped[str] = mapped_column(String(20))
    venueName: Mapped[str] = mapped_column(String(255))
    city: Mapped[str] = mapped_column(String(255))
    state: Mapped[Optional[str]] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(255))
    extraInfo: Mapped[Optional[str]] = mapped_column(String(255))
    notes: Mapped[Optional[str]] = mapped_column(String(1000))
    acknowledgments: Mapped[Optional[str]] = mapped_column(String(255))
    # still need to understand how to declare the following 'foreign keys' or wtv
    recordings = db.relationship('Recording', backref='concert', lazy=True)
    band_compositions = db.relationship('BandComposition', backref='concert', lazy=True)


# chatgpt generated code below
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Import blueprints or routes
    with app.app_context():
        from . import routes  # Import routes from the generated code
        db.create_all()  # Create tables

    return app
