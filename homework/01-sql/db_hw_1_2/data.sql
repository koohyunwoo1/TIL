-- 1
SELECT 
  *
FROM 
  tracks;

-- 2
SELECT
  Name, Milliseconds, UnitPrice
FROM
  tracks;

-- 3
SELECT 
  *
FROM 
  tracks
WHERE
  GenreId = 1;

-- 4
SELECT
  *
FROM
  tracks
GROUP BY
  Name;

-- 5
SELECT
  *
FROM
  tracks
LIMIT
  10;