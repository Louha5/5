CREATE TABLE IF NOT EXISTS user_info(
    vk_id INTEGER PRIMARY KEY,
    sentence TEXT
);
CREATE TABLE IF NOT EXISTS user_social_network(
    vk_id INTEGER PRIMARY KEY,
    social TEXT,
    link TEXT
);
CREATE TABLE IF NOT EXISTS user_Monday(
    vk_id INTEGER,
    time TEXT UNIQUE,
    name_lesson TEXT,
    office INTEGER
);
CREATE TABLE IF NOT EXISTS user_Tuesday(
    vk_id INTEGER,
    time TEXT UNIQUE,
    name_lesson TEXT,
    office INTEGER
);
CREATE TABLE IF NOT EXISTS user_Wednesday(
    vk_id INTEGER,
    time TEXT UNIQUE,
    name_lesson TEXT,
    office INTEGER
);
CREATE TABLE IF NOT EXISTS user_Thursday(
    vk_id INTEGER,
    time TEXT UNIQUE,
    name_lesson TEXT,
    office INTEGER
);
CREATE TABLE IF NOT EXISTS user_Friday(
    vk_id INTEGER,
    time TEXT UNIQUE,
    name_lesson TEXT,
    office INTEGER
);
CREATE TABLE IF NOT EXISTS user_Saturday(
    vk_id INTEGER,
    time TEXT UNIQUE,
    name_lesson TEXT,
    office INTEGER
);
CREATE TABLE IF NOT EXISTS user_Sunday(
    vk_id INTEGER,
    time TEXT UNIQUE,
    name_lesson TEXT,
    office INTEGER
)