CREATE TABLE internet_cafe.internet_cafe_client (
  ID int NOT NULL AUTO_INCREMENT,
  Name text NOT NULL,
  Email text NOT NULL,
  Password text NOT NULL,
  Key_word text NOT NULL,
  Code_Comp int NOT NULL,
  PRIMARY KEY (ID)
)

ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;
