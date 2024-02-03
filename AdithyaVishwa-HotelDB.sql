drop database if exists Hotel;

create database Hotel;

use Hotel;

create table RoomType (
    RoomTypeID TINYINT PRIMARY KEY auto_increment,
	RoomType VARCHAR(50) NOT NULL
);
create table Room (
    RoomNumber INT PRIMARY KEY auto_increment NOT NULL,
    isAccessible BOOL,
    StandardOccupancy TINYINT,
    MaximumOccupancy TINYINT NOT NULL,
    BasePrice DEC(6,2) NOT NULL,
    ExtraPerson DEC(6,2), 
    RoomTypeID TINYINT,
    FOREIGN KEY fk_Room_RoomType (RoomTypeID)
		REFERENCES RoomType (RoomTypeID)
);

create table Reservation (
	Full_Name VARCHAR(50),
    Res_ID INT PRIMARY KEY auto_increment,
	Adults tinyint,
    Children tinyint,
    Access_Date DATE NOT NULL,
    Vacate_Date  DATE NOT NULL,
    reservation_Cost DEC(10,2)
);
create table RoomReservation (
	RoomNumber INT auto_increment NOT NULL,
    Res_ID INT,
    PRIMARY KEY (RoomNumber, Res_ID),
    FOREIGN KEY fk_RoomReservation_Room (RoomNumber)
		REFERENCES Room (RoomNumber),
    FOREIGN KEY fk_RoomReservation_Reservation (Res_ID)
		REFERENCES Reservation (Res_ID)	
);

# Foreign key [fk_ThisTable_TargetTable (TargetTableField)
# References TargetTable (TargetTableField)
#ALTER TABLE ThisTable
#	ADD CONSTRAINT fk_ThisTable_TargetTableField FOREIGN KEY (TargetTableField) 
#		REFERENCES TargetTable(TargetField) ON DELETE NO ACTION,
create table Guest (
    Guest_ID INT PRIMARY KEY AUTO_INCREMENT,
    Full_Name VARCHAR(50) NOT NULL,
    Address VARCHAR(50) NOT NULL,
	City VARCHAR(50) NOT NULL,
	State VARCHAR(50) NOT NULL,
    ZIP VARCHAR(7) NOT NULL,
	Phone VARCHAR(15) NOT NULL
);
create table GuestReservation (
    Guest_ID INT,
    Res_ID INT,
    PRIMARY KEY (Guest_ID, Res_ID),
    FOREIGN KEY fk_GuestReservation_Guest (Guest_ID)
		REFERENCES Guest (Guest_ID),
    FOREIGN KEY fk_GuestReservation_Reservation (Res_ID)
		REFERENCES Reservation (Res_ID)   
);
create table Amenities (
    Amenity_ID INT PRIMARY KEY AUTO_INCREMENT,
    Amenity VARCHAR(50) NOT NULL
);
create table RoomAmenities (
    RoomNumber INT NOT NULL,
    Amenity_ID INT,
    PRIMARY KEY (RoomNumber, Amenity_ID),
    FOREIGN KEY fk_RoomAmenities_Room (RoomNumber)
		REFERENCES Room (RoomNumber),
    FOREIGN KEY fk_RoomAmenities_Amenities (Amenity_ID)
		REFERENCES Amenities (Amenity_ID)	
);


