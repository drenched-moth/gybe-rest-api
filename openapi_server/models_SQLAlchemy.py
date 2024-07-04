from app import db

class Concert(db.Model):
    __tablename__ = 'Concert'
    concertID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_concert = db.Column(db.String(20))
    venueName = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    country = db.Column(db.String(255))
    extraInfo = db.Column(db.String(255))
    notes = db.Column(db.String(1000))
    acknowledgments = db.Column(db.String(255))
    recordings = db.relationship('Recording', backref='concert', lazy=True)
    band_compositions = db.relationship('BandComposition', backref='concert', lazy=True)

class SongName(db.Model):
    __tablename__ = 'SongName'
    nameID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    songName = db.Column(db.String(255))
    songID = db.Column(db.Integer)

class SongPlayed(db.Model):
    __tablename__ = 'SongPlayed'
    songID = db.Column(db.Integer, primary_key=True)
    concertID = db.Column(db.Integer, db.ForeignKey('Concert.concertID'), primary_key=True)
    orderSong = db.Column(db.Integer, primary_key=True)

class Recording(db.Model):
    __tablename__ = 'Recordings'
    recID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    concertID = db.Column(db.Integer, db.ForeignKey('Concert.concertID'))
    duration = db.Column(db.Integer)
    sourceInfo = db.Column(db.String(255))
    url = db.Column(db.String(255))

class Member(db.Model):
    __tablename__ = 'Members'
    memberID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))

class BandComposition(db.Model):
    __tablename__ = 'BandComposition'
    memberID = db.Column(db.Integer, db.ForeignKey('Members.memberID'), primary_key=True)
    concertID = db.Column(db.Integer, db.ForeignKey('Concert.concertID'), primary_key=True)
