-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);


-- 1. Insert data into table
INSERT INTO 
  articles (title, content, createdAt)
VALUES
  ('hello', 'world', '2000-01-01');


INSERT INTO 
  articles (title, content, createdAt)
VALUES
  ('hello', 'DB', '2024-04-02');


INSERT INTO 
  articles (title, content, createdAt)
VALUES
  ('python', 'clear', '2024-01-20'),
  ('algorithm', 'clear', '2024-03-16'),
  ('django', 'in progress', '2024-04-01'),
  ('hello', 'DB', '2024-04-02');

SELECT * FROM articles;


-- 2. Update data in table
-- articles 테이블 1번 레코드의 title 필드 값을 'update Title'로 변경
UPDATE
  articles
SET
  title = 'update title'
WHERE
  id = 1;

SELECT * FROM articles;


-- articles 테이블 2번 레코드의 title, content 필드 값을 
-- 'update Title', 'update Content'로 변경
UPDATE
  articles
SET
  title = 'update title',
  content = 'update Content'
WHERE
  id = 2;

SELECT * FROM articles;

-- title이 hellor 였던 것들을 JavaScript로 바꿔줌
UPDATE
  articles
SET
  title = 'JavaScript',
  content = 'not started'
WHERE
  title = 'hello';

SELECT * FROM articles;





-- 3. Delete data from table

-- 마지막 테이블의 레코드 삭제하자
DELETE FROM
  articles
WHERE
  id = 6;


-- 새로운 데이터를 삽입하면
-- 그 전에 삭제한 id 6번은 사라지고
-- 7번부터 생성이 된다.AlbumId
INSERT INTO
  articles(title, content, createdAt)
VALUES
  ('new_title', 'new_content', '2000-01-01');


SELECT * FROM articles;


-- articles 테이블에서 작성일이
-- 오래된 순으로 레코드 2개 삭제

DELETE FROM
  articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAt 
  LIMIT 2
);


SELECT * FROM articles;
-- DELETE FROM
--   articles
-- WHERE id IN (

-- )