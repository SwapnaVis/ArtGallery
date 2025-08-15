CREATE DATABASE IF NOT EXISTS art_gallery;
USE art_gallery;

DROP TABLE IF EXISTS Sale;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Artwork;
DROP TABLE IF EXISTS Artist;

CREATE TABLE Artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_date DATE,
    nationality VARCHAR(50)
);

CREATE TABLE  IF NOT EXISTS artworks (
    artwork_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    year INT,
    type VARCHAR(50),
    price DECIMAL(10,2),
    rating DECIMAL(2,1) DEFAULT NULL,
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
       ON DELETE SET NULL
       ON UPDATE CASCADE
 
    );

CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE Sale (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    artwork_id INT UNIQUE,
    customer_id INT,
    date_of_sale DATE,
    price_sold DECIMAL(10,2),
    FOREIGN KEY (artwork_id) REFERENCES Artwork(artwork_id)
      ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
      ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO Artist (name, birth_date, nationality) VALUES
('Leonardo da Vinci', '1452-04-15', 'Italian'),
('Pablo Picasso', '1881-10-25', 'Spanish'),
('Vincent van Gogh', '1853-03-30', 'Dutch');

-- Insert sample artworks
INSERT INTO Artwork (title, year, type, price, rating, artist_id) VALUES
('Mona Lisa', 1503, 'Portrait', 780000000.00, 5.0, 1),
('The Weeping Woman', 1937, 'Cubism', 100000000.00, 4.8, 2),
('Starry Night', 1889, 'Post-Impressionism', 82000000.00, 4.9, 3);

-- Insert sample customers
INSERT INTO Customer (name, email, phone) VALUES
('John Doe', 'john@example.com', '1234567890'),
('Jane Smith', 'jane@example.com', '0987654321');

-- Insert sample sales
INSERT INTO Sale (artwork_id, customer_id, date_of_sale, price_sold) VALUES
(1, 1, '2023-06-15', 780000000.00),
(2, 2, '2024-02-20', 100000000.00);