SELECT
  AVG(age) as average_age
FROM  
  users


SELECT
  country, COUNT(*) as user_count
FROM
  users
GROUP BY
  country


SELECT
  *
FROM
  users
ORDER BY
  balance DESC
LIMIT
  1;


SELECT
  country, AVG(balance) as avg_balance
FROM
  users
GROUP BY
  country



SELECT 
  MAX(balance) - MIN(balance) as balance_difference
FROM
  users

