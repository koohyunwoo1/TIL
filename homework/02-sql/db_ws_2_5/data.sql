-- transactions 테이블 생성
CREATE TABLE transactions (
    id INT PRIMARY KEY,
    user_id INT NOT NULL,
    amount INT NOT NULL,
    transaction_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- transactions 데이터 삽입
INSERT INTO 
  transactions (id, user_id, amount, transaction_date) VALUES (1, 1, 500, '2024-03-15');
INSERT INTO 
  transactions (id, user_id, amount, transaction_date) VALUES (2, 2, 700, '2024-03-16');
INSERT INTO 
  transactions (id, user_id, amount, transaction_date) VALUES (3, 1, 200, '2024-03-17');
INSERT INTO 
  transactions (id, user_id, amount, transaction_date) VALUES (4, 3, 1000, '2024-03-18');

-- 사용자와 거래 조인하여 사용자의 이름, 거래 금액, 거래 일자를 출력
SELECT 
  u.first_name, u.last_name, t.amount, t.transaction_date
FROM 
  users u
JOIN 
  transactions t 
ON 
  u.id = t.user_id;

-- 사용자와 거래 조인하여 사용자의 이름, 거래 금액, 거래 일자를 출력하되 거래 일자가 '2024-03-16' 이후인 것만 선택
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

-- 사용자와 거래 조인하여 사용자의 이름, 전체 거래 금액을 출력
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
