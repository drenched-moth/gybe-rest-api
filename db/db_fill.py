# from flask import Flask, jsonify
from mysql.connector import connection
import json

cnx = connection.MySQLConnection(user='root',
                                 password='root',
                                 host='::1',
                                 database='concerto')
cursor = cnx.cursor()

data = dict()
with open("data/data.json", "r") as f:
    data = json.load(f)

cpt = 1
song_name_added = dict()

for key in data: # remember when iterating through dict you're really iterating through the keys
    entree = data[key]
    ven = entree["venue"]
    country = entree["country"]
    t_city, t_state, t_extr_inf, t_duration , t_notes, t_acknowledgments = "", "", "", "", "", ""
    city, state, extr_inf, duration, notes, acknowledgments = "", "", "", "", "", ""
    if entree.get("city") is not None:
        t_city = ", city"
        city = f", \"{entree.get('city')}\""
    if entree.get("state") is not None:
        t_state = ", state"
        state = f", \"{entree.get('state')}\""
    if entree.get("extra_info") is not None:
        t_extr_inf = ", extraInfo"
        extr_inf = f", \"{entree.get('extra_info')}\""
    if entree.get("note") is not None:
        t_notes = ", notes"
        note = entree.get('note').replace('"', "\\\"")
        notes = f", \"{note}\""
    if entree.get("thanks") is not None:
        t_acknowledgments = ", acknowledgments"
        thx = entree.get('thanks').replace('"', "\\\"")
        acknowledgments = f", \"{thx}\""


    query = f"insert into Concert(date_concert, country, venueName{t_city}{t_state}{t_extr_inf}{t_duration}{t_notes}{t_acknowledgments}) values(\"{key}\", \"{country}\", \"{ven}\"{city}{state}{extr_inf}{duration}{notes}{acknowledgments});"

    cursor.execute(query)

    if entree.get("setlist") is not None:
        for (idx, song) in zip(range(len(entree["setlist"])), entree["setlist"]):
            song = song.strip() # .replace("?", "\\?")
            if song not in song_name_added:
                #cursor.execute(f"insert into Songs(songID) values({cpt})")
                cursor.execute(f"insert into SongName(songName, songID) values(\"{song}\", {cpt})")
                song_name_added[song] = cpt
                cpt += 1
            cursor.execute(f"insert into SongPlayed(songID, concertID, orderSong) values({song_name_added[song]}, (select concertID from Concert where date_concert = \"{key}\"), {idx})")

cnx.commit()

with open("data/recordings.json", "r") as f:
    data = json.load(f)

cpt = 0
for elem in data:
    date_val = f"\"{elem['Date']}\""
    duration, source_info, url = "","",""
    duration_val, source_info_val, url_val = "","",""
    if "NA" not in elem["Running time"]:
        dur = int(elem['Running time'].strip("'"))
        duration = ", duration"
        duration_val = f", {dur}"
    if elem["Source Info"] is not None:
        source_info = ", sourceInfo"
        valid_source_info = elem['Source Info'].replace('"', '\\"')
        source_info_val = f", \"{valid_source_info}\""
    if elem["URL"] is not None:
        url = ", url"
        url_val = f", \"{elem['URL']}\""

    query = f"insert into Recordings(concertID{duration}{source_info}{url}) values((select concertID from Concert where date_concert = \"{elem['Date']}\"){duration_val}{source_info_val}{url_val})"
    # print(query)

    cursor.execute(query)
    cpt += 1

cursor.execute(f"insert into Concert(date_concert, venueName, city, state, country, extraInfo) values(\"2011-04-24\", \"lee's palace\", \"toronto\", \"Ontario\", \"Canada\", \"(late show) w/ total life\")");
sl = dict()
# with open("pages/page11/2011-04-24-soiree/data.json", "r") as f:
with open("data/data-2011-04-24-soir.json", "r") as f:
    sl = json.load(f)

for (idx, song) in zip(range(len(sl["songs"])), sl["songs"]) :
    cursor.execute(f"insert into SongPlayed(songID, concertID, orderSong) values((select songID from SongName where songName = \"{song}\"), (select concertID from Concert where date_concert = \"2011-04-24\" order by concertID desc limit 1), {idx})")

members = ["Efrim Menuck", "David Bryant", "Mike Moya", "Roger Tellier-Craig", "Sophie Trudeau", "Mauro Pezzente", "Thierry Amar", "Aidan Girt", "Bruce Cawdron", "Timothy Herzog", "Norsola Johnson", "Thea Pratt", "Mark Littlefair", "Fluffy Erskine", "Karl Lemieux", "Philippe Leonard", "Grayson Walker", "Peter Harry Hill"]
band_compo_requests = ["insert into BandComposition(memberID, concertID) select {}, concertID from Concert", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert < '1999-01-01' or date_concert > '2010-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1999-01-01' and date_concert < '2004-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1999-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01' and date_concert < '2012-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '2012-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01' and date_concert < '2004-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1995-01-01' and date_concert < '1998-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert < '2000-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '2000-01-01' and date_concert < '2004-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '2010-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '2015-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert > '1997-01-01' and date_concert < '1999-01-01'", "insert into BandComposition(memberID, concertID) select {}, concertID from Concert where date_concert = '1997-03-15'"]

for i in range(len(members)):
    cursor.execute(f"insert into Members(name) values(\"{members[i]}\")")
    cursor.execute(band_compo_requests[i].format(i+1))

cursor.close()
cnx.commit()
cnx.close()
