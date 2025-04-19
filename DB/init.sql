USE dbUsers;

CREATE TABLE Users(
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(10),
    password VARCHAR(20)
);

CREATE TABLE Users_Info(
    id_user_info INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT,
    name VARCHAR(50),
    email VARCHAR(50),
    description VARCHAR(50) DEFAULT ' ',
    CONSTRAINT user_info_FK FOREIGN KEY (id_user) REFERENCES Users(id_user)

);

CREATE TABLE Users_Sessions(
    id_user_session INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT,
    log_in BOOLEAN,
    date DATETIME,
    CONSTRAINT user_session_FK FOREIGN KEY (id_user) REFERENCES Users(id_user)
);
