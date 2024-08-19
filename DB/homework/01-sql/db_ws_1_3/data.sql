SELECT
  *
FROM
  users
WHERE
  first_name
LIKE
  '하%'


SELECT
  *
FROM
  users
WHERE
  phone
LIKE 
  '%555'


SELECT
  *
FROM
  users
WHERE
  country
LIKE
  '경상%'


SELECT
  *
FROM
  users
WHERE
  country
LIKE
  '경_남%'
  OR
  country
LIKE
  '충_남%';


