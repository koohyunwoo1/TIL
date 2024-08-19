CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);


INSERT INTO zoo (name, eat, weight, height, age) VALUES ('Lion', 'Meat', 200, 120, 5);
INSERT INTO zoo (name, eat, weight, height, age) VALUES ('Elephant', 'Plants', 5000, 300, 15);
INSERT INTO zoo (name, eat, weight, height, age) VALUES ('Giraffe', 'Leaves', 1500, 550, 10);
INSERT INTO zoo (name, eat, weight, height, age) VALUES ('Monkey', 'Fruits', 50, 60, 8);

SELECT 
  *
FROM
  zoo