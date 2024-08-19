1.
SELECT
  *
FROM
  artists;

2.
SELECT
  COUNT(*)
FROM
  artists;

3.
SELECT
  *
FROM
  artists
WHERE
  Name = 'AC/DC';

4.
SELECT
  ArtistId, Name
FROM
  artists;

5.
SELECT
  *
FROM
  artists
WHERE
  Name = 'Gilberto Gil'
  OR
  Name = 'Ed Motta';


6.
SELECT
  *
FROM
  artists
ORDER BY
  Name DESC;


7.
SELECT
  *
FROM
  artists
WHERE
  Name
LIKE
  'Vinícius%' 
LIMIT 2;


8.
SELECT
 ArtistId
FROM 
  artists 
LIMIT 
  21 
OFFSET 
  49;