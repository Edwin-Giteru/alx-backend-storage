-- a script that create an index on the first name and score of a table

CREATE INDEX idx_name_first_score
ON names(name(1), score);
