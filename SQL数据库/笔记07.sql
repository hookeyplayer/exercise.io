CREATE TABLE pls_fy2014_pupld14a ( 
	stabr varchar(2) NOT NULL,
	fscskey varchar(6) CONSTRAINT fscskey2014_key PRIMARY KEY,
	libid varchar(20) NOT NULL,
	libname varchar(100) NOT NULL,
	obereg varchar(2) NOT NULL,
	rstatus integer NOT NULL, 
	statstru varchar(2) NOT NULL, 
	statname varchar(2) NOT NULL, 
	stataddr varchar(2) NOT NULL,
	wifisess integer NOT NULL,
	yr_sub integer NOT NULL
      );