CREATE TABLE internet_cafe.internet_cafe_pc (
  Code int NOT NULL AUTO_INCREMENT,
  Server_Name char(200) NOT NULL DEFAULT '',
  CPU char(200) NOT NULL DEFAULT '',
  Main_Memory_Gb int NOT NULL DEFAULT 500,
  RAM_Gb int NOT NULL DEFAULT 8,
  GPU char(200) NOT NULL DEFAULT '',
  Status enum ('def', 'pro', 'vip') DEFAULT 'def',
  Users int NOT NULL DEFAULT 0,
  PRIMARY KEY (Code)
)

ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;
