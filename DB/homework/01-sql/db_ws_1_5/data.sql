SELECT
  *
FROM
  users
WHERE
  age >= 30 and balance >= 1000;


SELECT
  *
FROM 
  users
WHERE
  balance <= 1000 and age <= 20;


SELECT
  *
FROM
  users
WHERE
  first_name
LIKE
  '현%' AND country = '제주특별자치도' 
ORDER BY
  age DESC
LIMIT
  1;


SELECT
  *
FROM 
  users
WHERE
  last_name
LIKE
  '%박' AND age >= 25
ORDER BY
  age
LIMIT
  1;


SELECT
  *
FROM
  users
WHERE
  first_name
IN
  ('재은', '영일')
ORDER BY
  balance DESC
LIMIT
  1;


SELECT
  first_name,
  last_name, 
  age, 
  phone, 
  country, 
  MAX(balance) 
AS 
  max_balance 
FROM 
  users 
GROUP BY 
  country 
ORDER BY 
  max_balance DESC;


SELECT
 * 
FROM 
  users 
WHERE 
  age >= 30 
AND balance > (
    SELECT AVG(balance) 
    FROM users 
    WHERE age >= 30
);
