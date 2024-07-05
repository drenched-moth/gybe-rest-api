from typing import Optional
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey
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
    #recordings = db.relationship('Recording', backref='concert', lazy=True)
    #band_compositions = db.relationship('BandComposition', backref='concert', lazy=True)

class Recording(Base):
    __tablename__ = 'Recordings'

    recID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    concertID: Mapped[int] = mapped_column(ForeignKey("Concert.concertID"))
    duration: Mapped[Optional[int]]
    sourceInfo: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))

class Member(Base):
    __tablename__ = 'Member'

    memberID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))

class BandComposition(Base):
    __tablename__ = 'BandComposition'

    memberID: Mapped[int] = mapped_column(ForeignKey("Member.memberID"), primary_key=True)
    concertID: Mapped[int] = mapped_column(ForeignKey("Concert.concertID"), primary_key=True)

class SongName(Base):
    __tablename__ = 'SongName'

    nameID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    songName: Mapped[str]
    songID: Mapped[int]

class SongPlayed(Base):
    __tablename__ = 'SongPlayed'

    songID: Mapped[int] = mapped_column(primary_key=True)
    concertID: Mapped[int] = mapped_column(ForeignKey("Concert.concertID"), primary_key=True)
    orderSong: Mapped[int] = mapped_column(primary_key=True)

with app.app_context():
    db.create_all()


import json

with open("data/data.json", "r") as f:
    data = json.load(f)

cpt = 1 # cpt pour SongName
cpt_concert = 1
song_name_added = dict()

for key in data: # remember when iterating through dict you're really iterating through the keys
    # key = date_concert = venue
    entree = data[key]
    ven = entree["venue"]
    country = entree["country"]

    note = entree.get('note').replace('"', "\\\"")
    thx = entree.get('thanks').replace('"', "\\\"")

    new_concert = Concert(date_concert=key,
                          venueName=entree.get("venue")
                          country=entree.get("country"),
                          city=entree.get("city"),
                          state=entree.get("state"),
                          extraInfo=entree.get("extra_info"),
                          notes=note,
                          acknowledgments=thx)

    # add new_concert
    db.session.add(new_concert)
    db.session.commit()

    if entree.get("setlist") is not None:
        for (idx, song) in zip(range(len(entree["setlist"])), entree["setlist"]):
            song = song.strip() # .replace("?", "\\?")
            if song not in song_name_added:
                #cursor.execute(f"insert into SongName(songName, songID) values(\"{song}\", {cpt})")
                new_song_name = SongName(songName=song, songID=cpt)
                db.session.add(new_song_name)
                song_name_added[song] = cpt
                cpt += 1
            new_song_played = SongPlayed(songID=song_name_added[song], concertID=new_concert.concertID, orderSong=idx)
            db.session.add(new_song_played)
            #cursor.execute(f"insert into SongPlayed(songID, concertID, orderSong) values({song_name_added[song]}, (select concertID from Concert where date_concert = \"{key}\"), {idx})")
        db.session.commit()

double_day_concert = Concert(date_concert="2011-04-24",
                             venueName="lee's palace",
                             city="toronto",
                             state="Ontario",
                             country="Canada",
                             extraInfo="(late show) w/ total life")
db.session.add(double_day_concert)

with open("data/recordings.json", "r") as f:
    data = json.load(f)

cpt = 0
for elem in data:
    if "NA" not in elem["Running time"]:
        dur = int(elem['Running time'].strip("'"))
    else:
        dur = None

    new_recording = Recording(concertID=db.session.execute(db.select(Concert.concertID).where(Concert.date_concert == elem["Date"])).scalar_one(),
                              duration=dur,
                              sourceInfo=elem['Source Info'].replace('"', '\\"'),
                              url=elem.get("URL"))

    db.session.add(new_recording)

db.session.commit()

sl = dict()
with open("data/data-2011-04-24-soir.json", "r") as f:
    sl = json.load(f)

for (idx, song) in zip(range(len(sl["songs"])), sl["songs"]) :
    songID = db.session.execute(db.select(SongName.songID).where(SongName.songName == song)).scalar_one()
    concertID = double_day_concert.concertID
    db.session.add(SongPlayed(songID=songID,
                              concertID=concertID,
                              orderSong=idx))

members = ["Efrim Menuck", "David Bryant", "Mike Moya", "Roger Tellier-Craig", "Sophie Trudeau", "Mauro Pezzente", "Thierry Amar", "Aidan Girt", "Bruce Cawdron", "Timothy Herzog", "Norsola Johnson", "Thea Pratt", "Mark Littlefair", "Fluffy Erskine", "Karl Lemieux", "Philippe Leonard", "Grayson Walker", "Peter Harry Hill"]
band_compo_requests = ["insert into BandComposition(memberID, concertID) select {}, concertID from Concert",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert < '1999-01-01' or date_concert > '2010-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1999-01-01' and date_concert < '2004-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1999-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01' and date_concert < '2012-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '2012-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01' and date_concert < '2004-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1995-01-01' and date_concert < '1998-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert < '2000-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '2000-01-01' and date_concert < '2004-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '2010-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '2015-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01' and date_concert < '1999-01-01'",
                       "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert = '1997-03-15'"]

# TODO: finish the ORM inserting for data regarding members and band composition

# chatgpt generated code below
# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     db.init_app(app)

#     # Import blueprints or routes
#     with app.app_context():
#         from . import routes  # Import routes from the generated code
#         db.create_all()  # Create tables

#     return app
