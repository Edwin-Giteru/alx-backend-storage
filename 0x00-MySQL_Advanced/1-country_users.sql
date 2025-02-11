-- a script that creates table users
-- the table contains the following attributes: id email name country

CREATE TABLE IF NOT EXISTS users(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM("US", "CO", "TN") NOT NULL DEFAULT "US"
	);

