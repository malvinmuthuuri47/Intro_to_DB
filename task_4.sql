-- This script prints the full description of a table from the database
-- without using the DESCRIBE or EXPLAIN keywords

SELECT
	TABLE_NAME,
	COLUMN_NAME,
	COLUMN_TYPE,
	IS_NULLABLE,
	COLUMN_KEY,
	COLUMN_DEFAULT,
	EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
AND TABLE_NAME = 'books';
