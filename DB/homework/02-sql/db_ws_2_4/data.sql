-- transactions 테이블 생성
CREATE TABLE transactions (
    id INT PRIMARY KEY,
    user_id INT NOT NULL,
    amount INT NOT NULL,
    transaction_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- ttransactions 데이터 삽입
INSERT INTO transactions (id, user_id, amount, transaction_date) VALUES (1, 1, 500, '2024-03-15');
INSERT INTO transactions (id, user_id, amount, transaction_date) VALUES (2, 2, 700, '2024-03-16');
INSERT INTO transactions (id, user_id, amount, transaction_date) VALUES (3, 1, 200, '2024-03-17');
INSERT INTO transactions (id, user_id, amount, transaction_date) VALUES (4, 3, 1000, '2024-03-18');

SELECT 
  u.first_name, u.last_name, t.amount, t.transaction_date
FROM 
  users u
JOIN 
  transactions t 
ON 
  u.id = t.user_id;


SELECT 
  u.first_name, u.last_name, t.amount, t.transaction_date
FROM 
  users u
JOIN 
  transactions t 
ON 
  u.id = t.user_id
WHERE 
  t.transaction_date > '2024-03-16';

SELECT 
  u.first_name, u.last_name, SUM(t.amount) AS total_amount
FROM 
  users u
JOIN 
  transactions t 
ON 
  u.id = t.user_id
GROUP BY 
  u.id;