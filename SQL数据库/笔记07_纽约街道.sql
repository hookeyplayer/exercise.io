CREATE TABLE new_york_addresses (
	longitude numeric(9,6),
    latitude numeric(9,6),
    street_number varchar(10),
    street varchar(32),
    unit varchar(7),
    postcode varchar(5),
    id integer CONSTRAINT new_york_key PRIMARY KEY
);

COPY new_york_addresses
FROM '/Users/xiaofan/Downloads/practical-sql-master/Chapter_07/city_of_new_york.csv'
WITH (FORMAT CSV, HEADER);


-- Benchmark queries for index performance

EXPLAIN ANALYZE SELECT * FROM new_york_addresses
WHERE street = 'BROADWAY';

-- Listing 7-13: Creating a B-Tree index on the new_york_addresses table

CREATE INDEX street_idx ON new_york_addresses (street);
