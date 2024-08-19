-- 01. Querying data
-- SELECT 필드명 FROM 테이블명
SELECT
  LastName
FROM 
  employees;

-- 테이블 employees에서 LastName, FirstName 필드의 모든 데이터를 조회
SELECT 
  LastName, FirstName
FROM
  employees;

-- 테이블 employees에서 모든 필드 데이터를 조회
SELECT 
  *
FROM
  employees;

-- 조회 시 'FirstName'이 아닌 '이름'으로 출력
SELECT 
  FirstName AS '이름'
FROM
  employees;

-- 테이블 track에서 Name, Milliseconds 필드의 모든 데이터 조회
-- (단, Milliseconds 필드는 60000으로 나눠 분 단위 값으로 출력)
SELECT 
  Name,
  Milliseconds / 60000 AS '재생시간(분)'
FROM
  tracks;


-- 02. Sorting data
-- 테이블 employees에서 FirstName 필드의 모든 데이터를 오름차순으로 조회
SELECT
  FirstName
FROM 
  employees
ORDER BY
  FirstName;

-- 테이블 employees에서 FirstName 필드의 모든 데이터를 내림차순으로 조회
SELECT
  FirstName
FROM 
  employees
ORDER BY
  FirstName DESC;

-- 테이블 customers에서 Country 필드의 기준으로 내림차순 정렬한 다음 
-- City 필드 기준으로 오름차순 정렬하여 조회
SELECT
  Country, City
FROM 
  customers
ORDER BY
  Country DESC,
  City ASC;

-- 테이블 tracks에서 Milliseconds 필드를 기준으로 내림차순 정렬한 다음 
-- Name, Milliseconds 필드의 모든 데이터를 조회
-- 단, Miliseconds 필드는 60,000으로 나눠 단위 값으로 출력
SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM 
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시
-- NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력

SELECT
  ReportsTo
FROM 
  employees
ORDER BY
  ReportsTo;

-- SELECT statement 실행 순서
-- FROM -> SELECT -> ORDER BY
-- 1. 테이블에서 (FROM) 2. 조회하여 (SELECT) 3. 정렬(ORDER BY)

-- 03. Filtering data



-- DISTINCT statement
-- 조회 결과에서 중복된 레코드를 제거

-- 테이블 customers에서 Country 필드의 모든 데이터를 오름차순 조회
SELECT
  Country
FROM
  customers
ORDER BY
  Country;

-- 테이블 customers에서 Country 필드의 모든 데이터를 중복없이 오름차순 조회
SELECT DISTINCT
  Country
FROM 
  customers
ORDER BY
  Country;

-- WHERE statement
-- 조회 시 특정 검색 조건을 지정

-- 테이블 customers에서 City 필드 값이, 'Prague'인 데이터의
-- LastName, FirstName, City 조회
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

-- 테이블 customers에서 City 필드 값이, 'Prague'가 아닌 데이터의
-- LastName, FirstName, City 조회
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

-- 테이블 customers에서 Company 필드 값이 NULL이고, 
-- Country 필드 값이 'USA'인 데이터의
-- LastName, FirstName, Company, Country 조회
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

-- 테이블 customers에서 Company 필드 값이 NULL이거나, 
-- Country 필드 값이 'USA'인 데이터의
-- LastName, FirstName, Company, Country 
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';

-- 테이블 tracks에서 Bytes 필드 값이, 10,000 이상 500,000 이하인
-- 데이터의 Name, Bytes 조회
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000;

-- 테이블 tracks에서 Bytes 필드 값이, 10,000 이상 500,000 이하인
-- 데이터의 Name, Bytes를 Bytes 기준으로 오름차순 조회
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

-- 테이블 customers에서 Country 필드 값이, 
-- 'Canada' 또는 'Germany' 또는 'France'인 데이터의
--  LastName, FirstName, Country 조회
SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada','Germany','France');

-- 테이블 customers에서 Country 필드 값이, 
-- 'Canada' 또는 'Germany' 또는 'France'가 아닌 데이터의
--  LastName, FirstName, Country 조회
SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada','Germany','France');

-- 테이블 customers에서 LastName 필드 값이, 
-- 'son'으로 끝나는 데이터의 LastName, FirstName 조회
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

-- 테이블 customers에서 FirstName 필드 값이 4자리면서, 
-- 'a'으로 끝나는 데이터의 LastName, FirstName 조회
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';

-- Wildcard Characters

-- '%' : 0개 이상의 문자열과 일치 하는지 확인
-- '_' : 단일 문자와 일치하는지 확인


-- LIMIT 활용 1
-- 테이블 track에서 Trackid, Name, Bytes 필드 데이터를
-- Bytes 기준 내림차순으로 7개만 조회

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY Bytes DESC
LIMIT 7;


-- LIMIT 활용 2
-- 테이블 track에서 Trackid, Name, Bytes 필드 데이터를
-- Bytes 기준 내림차순으로 4번째부터 7개만 조회

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY 
  Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;



-- 04. Grouping data


-- GROUP BY syntax
-- FROM 및 WHERE 절 뒤에 배치
-- GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성

-- Country 필드를 그룹화
SELECT
  Country
FROM
  customers
GROUP BY
  Country;


-- COUNT 함수가 각 그룹에 대한 집계된 값을 계산
SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

-- 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한
-- Bytes의 평균 값을 내림차순 조회

SELECT
  Composer,
  AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;


SELECT
  Composer,
  AVG(Bytes) AS avgOfBytes
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  avgOfBytes DESC;


-- 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한
-- Milliseconds의 평균 값이 10 미만인 데이터 조회
-- (단, Milliseconds필드는 60,000으로 나눠 분 단위 값의 평균으로 계산)

-- 에러 발생

SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
WHERE
  avgOfMinute < 10
GROUP BY
  Composer;

-- 에러 발생




SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOfMinute < 10;


-- SELECT statement 실행 순서
-- 테이블에서 (FROM)
-- 특정 조건에 맞추어 (WHERE)
-- 그룹화 하고 (GROUP BY)
-- 만약 그룹화 조건이 있다면 맞추고 (HAVING)
-- 조회하여 (SELECT)
-- 정렬하고 (ORDER BY)
-- 특정 위치의 값을 가져옴 (LIMIT)




