-- @block
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);

--@block
INSERT INTO Users (email, bio, country)
VALUES
(
    "hello22@world.com",
    "I Love 222 !",
    "US"
),
(
    "hello323@world.com",
    "I 333trangers !",
    "IN"
),
(
    "hello42@world.com",
    "I Love 44444gers !",
    "MH"
);

-- @block
SELECT * FROM Users

-- @block
CREATE INDEX email_index ON Users(email);

-- @block

CREATE TABLE Rooms(
    id INT AUTO_INCREMENT,
    street VARCHAR(255),
    owner_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (owner_id) REFERENCES Users(id)
)

--@block
INSERT INTO Rooms (owner_id, street)
VALUES 
(1,'san diego sailboat'),
    (1, 'nantucket cottage'),
    (1, 'vail cabin'),
    (1, "sf cardboard box");

-- @block

SELECT * FROM users
LEFT JOIN Rooms ON Rooms.owner_id = users.id


-- @block
CREATE TABLE Bookings(
    id INT AUTO_INCREMENT,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (guest_id) REFERENCES Users(id),
    FOREIGN KEY (room_id) REFERENCES Rooms(id)
);

-- @block Rooms a user has booked
SELECT 
    guest_id,
    street,
    check_in
FROM bookings
INNER JOIN rooms ON rooms.owner_id = guest_id;

--@block
DROP DATABASE airbnb