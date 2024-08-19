CREATE TABLE songs (
  id INTEGER PRIMARY KEY,
  title TEXT,
  artist TEXT,
  album TEXT,
  genre TEXT,
  duration INTEGER
)


INSERT INTO songs (title, artist, album, genre, duration) VALUES
  ('Song 1', 'Artist 1', 'Album 1', 'Pop', 200),
  ('Song 2', 'Artist 2', 'Album 2', 'Rock', 300),
  ('Song 3', 'Artist 3', 'Album 3', 'Hip Hop', 250),
  ('Song 4', 'Artist 4', 'Album 4', 'Electronic', 180),
  ('Song 5', 'Artist 5', 'Album 5', 'R&B', 320);


UPDATE 
  songs
SET 
  title = 'New Title'
WHERE 
  id = 1;


SELECT
  *
FROM 
  songs;