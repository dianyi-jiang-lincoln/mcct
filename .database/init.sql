-- MCCT

DROP SCHEMA IF EXISTS mcct;
CREATE SCHEMA mcct;
USE mcct;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- Create Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY AUTO_INCREMENT,
    role ENUM ("admin", "manager", "user") DEFAULT "user",
    username VARCHAR(255) UNIQUE NOT NULL,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(255) UNIQUE NOT NULL,
    address VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL, -- hashed password
    avatar VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

ALTER TABLE users AUTO_INCREMENT = 10000;

-- Create Table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT
);

ALTER TABLE categories AUTO_INCREMENT = 10000;

-- Create Table
CREATE TABLE posts (
    id SERIAL PRIMARY KEY AUTO_INCREMENT,
    is_sticky TINYINT(1) NOT NULL DEFAULT 0,
    thumbnail_url VARCHAR(255),
    title VARCHAR(255) NOT NULL,
    type ENUM ("news", "event", "ad"),
    preview TEXT,
    content TEXT, -- HTML
    address VARCHAR(255),
    phone_number VARCHAR(20),
    category_id INT REFERENCES categories(id),
    created_by INT REFERENCES users(id),
    visible_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    visible_end TIMESTAMP DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT NULL
);

ALTER TABLE posts AUTO_INCREMENT = 10000;

-- Create Comment Table
CREATE TABLE comments (
    id SERIAL PRIMARY KEY AUTO_INCREMENT,
    content TEXT NOT NULL,
    post_id INT REFERENCES posts(id),
    reply_to INT, -- comment id
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT NULL
);

ALTER TABLE comments AUTO_INCREMENT = 10000;

SET FOREIGN_KEY_CHECKS = 1;

-- Insert mock data into categories table
INSERT INTO categories (name, description)
VALUES
    ("Technology", "Stay updated with the latest tech trends."),
    ("Food", "Explore mouthwatering culinary delights."),
    ("Travel", "Discover amazing destinations around the world."),
    ("Health", "Tips for maintaining a healthy lifestyle."),
    ("Entertainment", "Entertainment news and updates.");

-- Insert mock data into users table
INSERT INTO users (role, username, firstname, lastname, phone_number, email, address, password, avatar, last_login)
VALUES
    ("admin", "adminuser", "Admin", "User", "1234567890", "admin@example.com", "123 Admin St", "hashed_password", "avatar_url", NOW()),
    ("manager", "manageruser", "Manager", "User", "9876543210", "manager@example.com", "456 Manager Ave", "hashed_password", "avatar_url", NOW()),
    ("user", "readeruser", "Reader", "User", "5555555555", "reader@example.com", "789 Reader Rd", "hashed_password", "avatar_url", NOW()),
    ("user", "user1", "John", "Doe", "1111111111", "user1@example.com", "123 Main St", "hashed_password", "avatar_url", NOW()),
    ("user", "user2", "Jane", "Smith", "2222222222", "user2@example.com", "456 Elm Ave", "hashed_password", "avatar_url", NOW()),
    ("user", "user3", "Michael", "Johnson", "3333333333", "user3@example.com", "789 Oak Rd", "hashed_password", "avatar_url", NOW()),
    ("user", "user4", "Emily", "Williams", "4444444444", "user4@example.com", "567 Pine St", "hashed_password", "avatar_url", NOW()),
    ("user", "user5", "David", "Brown", "5555555555", "user5@example.com", "890 Maple Ave", "hashed_password", "avatar_url", NOW()),
    ("user", "user6", "Sarah", "Davis", "6666666666", "user6@example.com", "234 Cedar Rd", "hashed_password", "avatar_url", NOW()),
    ("user", "user7", "Jessica", "Miller", "7777777777", "user7@example.com", "678 Birch St", "hashed_password", "avatar_url", NOW());

-- Insert mock data into posts table
INSERT INTO posts (is_sticky, thumbnail_url, title, type, preview, content, address, phone_number, category_id, created_by, visible_start)
VALUES
    (1, "https://images.pexels.com/photos/257540/pexels-photo-257540.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200", "Tech News", "news", "Stay updated with the latest tech news.", "Read about the latest innovations in the tech industry.", "123 Tech St", "1112223333", 10001, 10001, NOW()),
    (0, "https://images.pexels.com/photos/3173554/pexels-photo-3173554.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200", "Food Festival", "event", "Experience a culinary extravaganza!", "Indulge in a variety of delicious dishes at the food festival.", "456 Food Ave", "4445556666", 10002, 10002, NOW() - INTERVAL 2 DAY),
    (0, "https://images.pexels.com/photos/458533/pexels-photo-458533.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200", "Travel Guide", "news", "Plan your next adventure with our travel guide.", "Explore breathtaking destinations and travel tips.", "789 Travel Rd", "7778889999", 10003, 10001, NOW() - INTERVAL 4 DAY),
    (0, 'https://images.pexels.com/photos/5412276/pexels-photo-5412276.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200', 'Gaming Tournament', 'event', 'Join the ultimate gaming competition!', 'Compete against the best gamers in town and win exciting prizes.', '123 Game St', '1112223333', 10005, 10005, NOW() + INTERVAL 1 DAY),
    (0, 'https://images.pexels.com/photos/1640774/pexels-photo-1640774.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200', 'Healthy Recipes', 'news', 'Discover delicious and nutritious recipes.', 'Learn how to prepare healthy meals for you and your family.', '456 Kitchen Ave', '4445556666', 10002, 10006, NOW() + INTERVAL 3 DAY),
    (0, 'https://images.pexels.com/photos/4172951/pexels-photo-4172951.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200', 'New Movie Release', 'news', 'Get ready for an amazing cinematic experience!', 'Check out the latest blockbuster hitting theaters near you.', '789 Cinema Rd', '7778889999', 10005, 10005, NOW() - INTERVAL 2 DAY),
    (0, 'https://images.pexels.com/photos/5212349/pexels-photo-5212349.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200', 'Fitness Workshop', 'event', 'Achieve your fitness goals with expert guidance.', 'Join our fitness workshop to learn effective workout routines.', '234 Gym St', '3334445555', 10004, 10004, NOW() + INTERVAL 5 DAY),
    (0, 'https://images.pexels.com/photos/3860099/pexels-photo-3860099.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200', 'Local Art Exhibition', 'event', 'Celebrate local artists and their incredible work.', 'Explore a diverse collection of artworks from talented local artists.', '567 Art Center', '6667778888', 10001, 10001, NOW() + INTERVAL 7 DAY),
    (0, 'https://images.pexels.com/photos/4860146/pexels-photo-4860146.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200', 'Home Decor Tips', 'news', 'Transform your living space with these decor ideas.', 'Learn how to create a stylish and cozy home environment.', '890 Home Rd', '8889990000', 10002, 10002, NOW() + INTERVAL 9 DAY),
    (0, 'https://images.pexels.com/photos/2416522/pexels-photo-2416522.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200', 'Music Concert', 'event', 'Get ready for a night of unforgettable music!', 'Experience live performances by your favorite artists at our music concert.', '123 Concert St', '2223334444', 10005, 10005, NOW() + INTERVAL 11 DAY),
    (0, 'https://images.pexels.com/photos/3319905/pexels-photo-3319905.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200', 'Cooking Class', 'event', 'Enhance your culinary skills with our cooking class.', 'Learn how to prepare exquisite dishes from professional chefs.', '789 Culinary Rd', '9990001111', 10002, 10002, NOW() + INTERVAL 15 DAY),
    (0, 'https://images.pexels.com/photos/2599384/pexels-photo-2599384.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=200&w=200', 'Pet Adoption Drive', 'event', 'Find a furry friend to bring home!', 'Join our pet adoption event and give a loving home to a shelter animal.', '234 Pet Shelter', '1112223333', 10004, 10004, NOW() + INTERVAL 17 DAY);

-- Insert mock data into comments table
INSERT INTO comments (content, post_id)
VALUES
    ("Great article!", 10001),
    ("Looking forward to it!", 10002),
    ("I can\'t wait to travel!", 10003),
    ("Are there any travel discounts?", 10003),
    ("Yes, there are special offers for our readers.", 10001);
