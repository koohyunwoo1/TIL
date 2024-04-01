-- Table 구조 확인
PRAGMA table_info('examples');

-- 1. Create a table

-- 2. Modifying table fields
-- 2.1 ADD COLUMN

-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음

-- 2.2 RENAME COLUMN

-- 2.3 RENAME TO

-- 3. Delete a table


-- sqlite는 컬럼 수정 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
