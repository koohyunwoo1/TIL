SELECT
  genre, COUNT(*) as count
FROM
  songs
GROUP BY
  genre;



SELECT
  genre, COUNT(*) as count ,
  AVG(duration) as average_duration
FROM
  songs
GROUP BY
  genre;