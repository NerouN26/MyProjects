CREATE TABLE internet_cafe.internet_cafe_reserv (
  ID int NOT NULL AUTO_INCREMENT,
  Date datetime NOT NULL DEFAULT '2023-04-29 00:00:00',
  Game_time_hour int NOT NULL DEFAULT 1,
  User_ID int NOT NULL DEFAULT 0,
  Name_user char(200) NOT NULL DEFAULT '',
  User_code_comp int NOT NULL DEFAULT 1,
  PRIMARY KEY (ID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;