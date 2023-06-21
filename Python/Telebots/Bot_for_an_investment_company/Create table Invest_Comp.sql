CREATE TABLE telegramm.invest_comp (
  id INT NOT NULL AUTO_INCREMENT,
  position CHAR(200) NOT NULL,
  area CHAR(200) NOT NULL,
  full_price CHAR(200) NOT NULL,
  current_price CHAR(200) NOT NULL,
  resale_price CHAR(200) NOT NULL,
  projected_price_no_repair CHAR(200) NOT NULL,
  projected_price_whith_repair CHAR(200) NOT NULL,
  planned_profitability CHAR(200) NOT NULL,
  yearly CHAR(200) NOT NULL,
  implementation_period CHAR(200) NOT NULL,
  amount_of_attraction CHAR(200) NOT NULL,
  iden CHAR(200) DEFAULT NULL,
  summa CHAR(200) DEFAULT NULL,
  opisanie CHAR(200) DEFAULT NULL,
  status CHAR(200) DEFAULT NULL,
  PRIMARY KEY (id)
)
ENGINE = INNODB,
AUTO_INCREMENT = 2,
AVG_ROW_LENGTH = 16384,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;