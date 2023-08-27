-- MCCT

DROP SCHEMA IF EXISTS mcct;
CREATE SCHEMA mcct;
USE mcct;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- Create ENUM Type
CREATE TYPE user_type AS ENUM ("admin", "manager", "reader");
CREATE TYPE post_type AS ENUM ("news", "event", "ad");

-- Create Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY AUTO_INCREMENT = 10000,
    username VARCHAR(255) UNIQUE NOT NULL,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(255) UNIQUE NOT NULL,
    address VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL, -- hashed password
    avatar VARCHAR(255),
    role user_type NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

-- Create Table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY AUTO_INCREMENT = 10000,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT
);

-- Create Table
CREATE TABLE posts (
    id SERIAL PRIMARY KEY AUTO_INCREMENT = 10000,
    is_sticky TINYINT(1) NOT NULL DEFAULT 0,
    thumbnail_url VARCHAR(255),
    title VARCHAR(255) NOT NULL,
    subtitle TEXT,
    content TEXT,
    access_level user_type DEFAULT "reader",
    type post_type NOT NULL,
    address VARCHAR(255),
    phone_number VARCHAR(20),
    category_id INT REFERENCES categories(id),
    created_by INT REFERENCES users(id),
    visible_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    visible_end TIMESTAMP DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Comment Table
CREATE TABLE comments (
    id SERIAL PRIMARY KEY AUTO_INCREMENT = 10000,
    content TEXT NOT NULL,
    reply_to INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SET FOREIGN_KEY_CHECKS = 1;

-- Insert mock data into users table
INSERT INTO users (username, firstname, lastname, phone_number, email, address, password, avatar, role)
VALUES
    ("adminuser", "Admin", "User", "1234567890", "admin@example.com", "123 Admin St", "hashed_password", "avatar_url", "admin"),
    ("manageruser", "Manager", "User", "9876543210", "manager@example.com", "456 Manager Ave", "hashed_password", "avatar_url", "manager"),
    ("readeruser", "Reader", "User", "5555555555", "reader@example.com", "789 Reader Rd", "hashed_password", "avatar_url", "reader"),
    ("user1", "John", "Doe", "1111111111", "user1@example.com", "123 Main St", "hashed_password", "avatar_url", "reader"),
    ("user2", "Jane", "Smith", "2222222222", "user2@example.com", "456 Elm Ave", "hashed_password", "avatar_url", "reader"),
    ("user3", "Michael", "Johnson", "3333333333", "user3@example.com", "789 Oak Rd", "hashed_password", "avatar_url", "reader"),
    ("user4", "Emily", "Williams", "4444444444", "user4@example.com", "567 Pine St", "hashed_password", "avatar_url", "reader"),
    ("user5", "David", "Brown", "5555555555", "user5@example.com", "890 Maple Ave", "hashed_password", "avatar_url", "reader"),
    ("user6", "Sarah", "Davis", "6666666666", "user6@example.com", "234 Cedar Rd", "hashed_password", "avatar_url", "reader"),
    ("user7", "Jessica", "Miller", "7777777777", "user7@example.com", "678 Birch St", "hashed_password", "avatar_url", "reader"),
    ("user8", "Kevin", "Wilson", "8888888888", "user8@example.com", "123 Pine Ave", "hashed_password", "avatar_url", "reader"),
    ("user9", "Amanda", "Martinez", "9999999999", "user9@example.com", "456 Oak St", "hashed_password", "avatar_url", "reader"),
    ("user10", "Daniel", "Garcia", "1010101010", "user10@example.com", "789 Elm Ave", "hashed_password", "avatar_url", "reader");

-- Insert mock data into categories table
INSERT INTO categories (name, description)
VALUES
    ("News", "Latest news and updates"),
    ("Events", "Upcoming events and activities"),
    ("Ads", "Advertisements and promotions");

-- Insert mock data into posts table
INSERT INTO posts (is_sticky, thumbnail_url, title, subtitle, content, access_level, type, address, phone_number, category_id, created_by, visible_start, visible_end)
VALUES
    (1, "thumbnail_url_1", "Important News", "Breaking news!", "This is an important news article.", "admin", "news", "123 News St", "1112223333", 10001, 10001, NOW()),
    (0, "thumbnail_url_2", "Upcoming Event", "Join us for an exciting event!", "Get ready for a fantastic event.", "manager", "event", "456 Event Ave", "4445556666", 10002, 10002, NOW() + INTERVAL 1 DAY),
    (0, "thumbnail_url_3", "Special Promotion", "Limited-time offer!", "Check out our amazing deals.", "reader", "ad", "789 Promo Rd", "7778889999", 10003, 10003, NOW() + INTERVAL 2 DAYS),
    (0, "thumbnail_url_4", "Weekly Recap", "A summary of the week", "Catch up on what happened this week.", "reader", "news", "123 Recap St", "1112223333", 10001, 10003, NOW() - INTERVAL 5 DAYS),
    (0, "thumbnail_url_5", "Art Exhibition", "Celebrate creativity", "Join us for an art exhibition showcasing local talents.", "manager", "event", "456 Art Ave", "4445556666", 10002, 10002, NOW() + INTERVAL 3 DAYS),
    (0, "thumbnail_url_6", "New Product Launch", "Introducing our latest product", "Discover our innovative new product designed to enhance your life.", "reader", "ad", "789 Product Rd", "7778889999", 10003, 10001, NOW() + INTERVAL 2 DAYS),
    (0, "thumbnail_url_7", "Sports Tournament", "Cheer for your favorite team", "Join us for an exciting sports tournament with teams from around the region.", "manager", "event", "234 Sports St", "3334445555", 10002, 10002, NOW() - INTERVAL 5 DAYS, NOW() + INTERVAL 6 DAYS),
    (0, "thumbnail_url_8", "Limited-time Sale", "Huge discounts for a limited time", "Don\'t miss out on our special sale offering big discounts on selected items.", "reader", "ad", "567 Sale Ave", "6667778888", 10003, 10003, NOW() + INTERVAL 7 DAYS),
    (0, "thumbnail_url_9", "Health Workshop", "Learn about healthy living", "Join us for a workshop where experts will share tips for a healthier lifestyle.", "manager", "event", "890 Health Rd", "9990001111", 10002, 10001, NOW() + INTERVAL 10 DAYS),
    (0, "thumbnail_url_10", "Book Launch", "Discover a new literary masterpiece", "Be the first to experience the launch of a highly anticipated novel.", "reader", "event", "123 Book St", "2223334444", 10002, 10002, NOW() + INTERVAL 12 DAYS),
    (0, "thumbnail_url_11", "Tech Conference", "Explore the latest tech trends", "Tech enthusiasts can\'t afford to miss this conference featuring cutting-edge innovations.", "manager", "event", "456 Tech Ave", "5556667777", 10002, 10003, NOW() + INTERVAL 15 DAYS),
    (0, "thumbnail_url_12", "Summer Sale", "Beat the heat with hot deals", "Stay cool and enjoy summer savings on a wide range of products.", "reader", "ad", "789 Summer Rd", "8889990000", 10003, 10001, NOW() + INTERVAL 18 DAYS),
    (0, "thumbnail_url_13", "Charity Run", "Run for a cause", "Participate in a charity run to support a noble cause and make a difference.", "manager", "event", "234 Charity St", "1112223333", 10002, 10002, NOW() + INTERVAL 20 DAYS),
    ;

-- Insert mock data into comments table
INSERT INTO comments (content, reply_to)
VALUES
    ("Great news!", NULL),
    ("Looking forward to it!", NULL),
    ("I can\'t wait!", NULL),
    ("Will there be food?", 10001),
    ("Yes, there will be snacks.", 10004),
    ("Awesome!", NULL);