-- a script that creates an indexing the first letter of a name in a table

CREATE INDEX idx_name_first
ON names(name(1));
