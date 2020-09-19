CREATE TABLE `daily-results` (
	`date` DATE NOT NULL,
	`co1` VARCHAR NOT NULL,
	`co2` VARCHAR NOT NULL,
	`r` FLOAT NOT NULL,
	`r2` INT,
	`sd` FLOAT NOT NULL,
	PRIMARY KEY (`date`,`co1`,`co2`)
);

SELECT * FROM daily-results;

INSERT INTO daily-results
VALUES (value1, value2, value3, ...);
