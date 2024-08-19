ALTER TABLE 
  zoo 
ADD COLUMN 
  species TEXT;

UPDATE
  zoo
SET
  species = 'Panthera leo'
WHERE
  name = 'Lion';

UPDATE
  zoo
SET
  species = 'Loxodonta africana'
WHERE
  name = 'Elephant';

UPDATE
  zoo
SET
  species = 'Giraffa camelopardalis'
WHERE
  name = 'Giraffe';

UPDATE
  zoo
SET
  species = 'Cebus capucinus'
WHERE
  name = 'Monkey';


SELECT
  *
FROM
  zoo;