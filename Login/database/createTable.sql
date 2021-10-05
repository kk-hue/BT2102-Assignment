CREATE TABLE Customer(
	id			VARCHAR(20)		NOT NULL,
    fname		VARCHAR(50)		NOT NULL,
    phone		VARCHAR(8)		NOT NULL,
    email 		VARCHAR(30) 	NOT NULL,
    address 	VARCHAR(30)		NOT NULL,
    cpassword	VARCHAR(50)		NOT NULL,
    gender		enum('Male', 'Female')		NOT NULL,
    
    primary key (id))
