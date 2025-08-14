CREATE DATABASE IF NOT EXISTS art_gallery;
USE art_gallery;

CREATE TABLE Artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE,
    nationality VARCHAR(50)
);

CREATE TABLE Artwork (
    artwork_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    year INT,
    type VARCHAR(50),
    price DECIMAL(10,2),
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
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
    FOREIGN KEY (artwork_id) REFERENCES Artwork(artwork_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
