-- Ceci est une ébauche TEMPORAIRE
-- faut check ça aussi : https://docs.sqlalchemy.org/en/20/core/pooling.html
create database if not exists concerto character set utf8;
use concerto;

create table Concert (
  concertID int auto_increment primary key,
  date_concert varchar(20),
  venueName varchar(255),
  city varchar(255),
  state varchar(255),
  country varchar(255),
  extraInfo varchar(255),
  notes varchar(1000),
  acknowledgments varchar(255)
);
-- faut check ça :
-- https://www.w3schools.com/sql/sql_primarykey.asp

create table SongName (
  nameID int auto_increment primary key,
  songName varchar(255),
  songID int -- attention au nom trompeur, il ne s'agit pas d'un vrai ID, plusieurs noms peuvent designer le meme morceau
);

create table SongPlayed (
  songID int,
  concertID int,
  orderSong int,
  primary key (songID, concertID, orderSong), -- primary key (songID, date_concert), <-- on ne peut pas faire ca car il y a des doublons sur une seule date, morceau inconnu (?) ou bien improvisation
  foreign key (concertID) references Concert(concertID)
);

create table Recordings (
  recID int auto_increment primary key,
  concertID int,
  duration int, -- in minutes
  sourceInfo varchar(255),
  url varchar(255),
  foreign key (concertID) references Concert(concertID)
);

create table Members (
  memberID int auto_increment primary key,
  name varchar(100)
);

create table BandComposition (
  memberID int,
  concertID int,
  primary key (memberID, concertID),
  foreign key (concertID) references Concert(concertID),
  foreign key (memberID) references Members(memberID)
);

create view band_composition_with_name as
  select name, memberID, concertID
  from
    BandComposition
      inner join
    Members using(memberID);

create view songs_played_named as
  select concertID, orderSong, songName, songID
    from
      SongName
        inner join
      SongPlayed using(songID);

create view songs_played_named_ordered as
  select *
  from songs_played_named
  order by
    concertID asc,
    orderSong asc;

create view songs_played_occurence as
  select songID, count(songID) as occurence
  from SongPlayed
  group by songID;

create view songs_played_named_occurence as
  select songID, songName, count(songID) as occurence
  from songs_played_named
  group by songName;

create view nbr_song_played_at_concert as
  select concertID, count(concertID)
  from songs_played_named
  group by concertID;

create view recorded_concerts_distinct_ids as
  select distinct concertID from Recordings;

create view recorded_concerts as
  select *
  from
    recorded_concerts_distinct_ids
      inner join
    Concert using(concertID);

create view recordings_with_concert_info as
  select *
  from
    Recordings
      inner join
    Concert using(concertID);

create view songs_recorded_occurence as
  select songID, count(songID) as occurence
  from
    recorded_concerts_distinct_ids
      inner join
    SongPlayed using(concertID)
  group by songID;

create view songs_recorded_occurence_named as
  select songID, songName, occurence
  from
    songs_recorded_occurence
      inner join
    SongName using(songID);

create view songs_positional_occurence as
  select songID, orderSong, count(*) as timesPlayed
  from SongPlayed
  group by songID, orderSong;

create view songs_max_positional_occurence as
  select songID, max(timesPlayed) as maxPlayed
  from songs_positional_occurence
  group by songID;

create view songs_min_positional_occurence as
  select songID, min(timesPlayed) as minPlayed
  from songs_positional_occurence
  group by songID;

create view most_played_position as
  select a.songID, orderSong, timesPlayed
  from
    songs_positional_occurence as a
      inner join
    songs_max_positional_occurence as b on a.songID = b.songID and a.timesPlayed = b.maxPlayed;

create view least_played_position as
  select a.songID, orderSong, timesPlayed
  from
    songs_positional_occurence as a
      inner join
    songs_min_positional_occurence as b on a.songID = b.songID and a.timesPlayed = b.minPlayed;

create view songs_played_by_concert as
  select concertID, date_concert, songID
  from
    SongPlayed
      inner join
    Concert using(concertID);

create view songs_played_by_recording as
  select concertID, date_concert, songID
  from
    songs_played_by_concert
      inner join
    Recordings using(concertID);

create view last_time_song_was_played as
  select *
  from songs_played_by_concert
  order by date_concert desc;

create view first_time_song_was_played as
  select *
  from songs_played_by_concert
  order by date_concert asc;

create view following_songs as
  select a.concertID, a.songID, b.songID as followingSong
  from
    SongPlayed as a
      inner join
    SongPlayed as b on a.concertID = b.concertID and b.orderSong = (a.orderSong+1);

create view preceding_songs as
  select a.concertID, a.songID, b.songID as precedingSong
    from
      SongPlayed as a
        inner join
      SongPlayed as b on a.concertID = b.concertID and b.orderSong = (a.orderSong-1);

create view count_following_songs as
  select songID, followingSong, count(followingSong) as nbrFollowed
  from following_songs
  group by songID, followingSong;

create view count_preceding_songs as
  select songID, precedingSong, count(precedingSong) as nbrPreceded
  from preceding_songs
  group by songID, precedingSong;
