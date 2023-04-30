# Internet Cafe Database

This is a MySQL database that I created to demonstrate my current skills. It was created on the Internet cafe theme, like a telegram bot, so using some libraries and making small changes to the bot code, you can connect this database to it.

### I used:
* dbForge Studio 2020 for MySQL tool for writing code and queries, as well as editing the table itself through the built-in parameters of Alter Table.
* MySQL workbench to visualize the result in the form of a Model(diagram).
* MySQL command line client to fulfill requests.


## Internet Cafe Client

This table is for storing user data. This is the key table, which will be visible on the diagram.
The [code for creating](Create_table_internet_cafe_client.sql) this table looks like this:
```
CREATE TABLE internet_cafe.internet_cafe_client (
  ID int NOT NULL AUTO_INCREMENT,
  Name text NOT NULL,
  Email text NOT NULL,
  Password text NOT NULL,
  Key_word text NOT NULL,
  Code_Comp int NOT NULL,
  PRIMARY KEY (ID)
);
```
Here the values ​​of each column cannot be NULL. The ID column is a Primary key and uses Auto_Increment to automatically populate the ID numbering. [Data is loaded](Insert_internet_cafe_client.sql) into this table using INSERT INTO.

Request:
```
SELECT *
FROM internet_cafe_client;
```
gives us:

| ID | Name        | Email                               | Password   | Key_word    | Code_Comp |
|----|-------------|-------------------------------------|------------|-------------|-----------|
|  1 | Josh        | Joshbvg25@mail.com                  | 123548Jo   | Mother      |         1 |
|  2 | Kevin       | Kevinbvg29@mail.com                 | 86597548Ke | Father      |         2 |
|  3 | Mike        | Mikebvg23@mail.com                  | 55488664Mi | Puppy       |         3 |
|  4 | James       | pivemoimaffa-6688@yopmail.com       | XVYqJeef   | reception   |         4 |
|  5 | Scott       | cissifewudau-9456@yopmail.com       | soYzlnKA   | involvement |         5 |
|  6 | Jonathan    | greugrureujoja-3427@yopmail.com     | jwNuGJQa   | motion      |         6 |
|  7 | Fred        | kunautuceddi-1364@yopmail.com       | RLicKBco   | nephew      |         7 |
|  8 | William     | greyolummewu-4727@yopmail.com       | XRbLCNAv   | coefficient |         8 |
|  9 | Thomas      | praddaudediqua-3684@yopmail.com     | QsBxTNBZ   | bucket      |         9 |
| 10 | Ronnie      | quabregrenoillei-5159@yopmail.com   | CfMqOOYZ   | sieve       |        10 |
| 11 | Edwin       | ruwufrufazoi-3206@yopmail.com       | QPWavkAg   | reputation  |         5 |
| 12 | Johnny      | ninnocregettei-5819@yopmail.com     | tnEXXHbS   | accordion   |         2 |
| 13 | Sam         | pequeupparuxou-4786@yopmail.com     | PcORTbpu   | whisper     |         7 |
| 14 | Richard     | meruffobrille-2305@yopmail.com      | JeIJSUlx   | candor      |         6 |
| 15 | Calvin      | siwoittollusse-5670@yopmail.com     | hefLTjgF   | octopus     |         1 |
| 16 | Carl        | wammeureukappi-6085@yopmail.com     | CTtqIxMS   | scorpion    |         5 |
| 17 | William     | fitriwixoite-1796@yopmail.com       | uSRyopeL   | rack        |         7 |
| 18 | Jacob       | gicevatrillei-5752@yopmail.com      | pjaHXjLg   | liturgy     |        10 |
| 19 | Thomas      | hutabrebreura-2212@yopmail.com      | QIBbEyzt   | drawer      |         8 |
| 20 | Rick        | rauddoiprillufu-3223@yopmail.com    | LBOQQaXh   | korbut      |         4 |
| 21 | Christopher | kesseuffafrenna-5035@yopmail.com    | YhPIMFzR   | sardis      |         8 |
| 22 | Michael     | quopeitittouve-4006@yopmail.com     | xlDKouWY   | abject      |         9 |
| 23 | Timothy     | zokelumoima-9316@yopmail.com        | yyhkfEaj   | andira      |         1 |
| 24 | Elmer       | voivurausuttau-7305@yopmail.com     | JTkvlYMJ   | angary      |         3 |
| 25 | Bruce       | tesseuxannequo-5033@yopmail.com     | zToUAJbV   | angina      |         2 |
| 26 | Ernest      | nipoiqueveyau-3944@yopmail.com      | GjTUmsgY   | battak      |         6 |
| 27 | Roger       | keddayileyeu-2117@yopmail.com       | fUDtCflq   | bearer      |         4 |
| 28 | Howard      | kagritrefrirei-5487@yopmail.com     | prDVXkSN   | bebled      |         8 |
| 29 | Andrew      | cagezofrissi-1060@yopmail.com       | xyOICPrL   | beltis      |         3 |
| 30 | Roy         | crennoizaddoxi-8249@yopmail.com     | UIjkctjC   | hello       |         5 |
| 31 | Antonio     | heimmeizoteille-2956@yopmail.com    | qPTuecTg   | heroic      |         7 |
| 32 | Joshua      | trawallulauppi-9033@yopmail.com     | D4B4Dh5Z   | judger      |         1 |
| 33 | James       | raufroholloullou-9388@yopmail.com   | t97d3vqE   | kishke      |         5 |
| 34 | Robert      | wufrappeipoucre-2176@yopmail.com    | AcH75jh2   | kojang      |         2 |
| 35 | Danny       | zottoufretrottau-8973@yopmail.com   | Du3bxU77   | ladies      |         9 |
| 36 | David       | ramapuceifru-8152@yopmail.com       | 429RbWsd   | lathen      |         8 |
| 37 | Jose        | graddayomaquo-3051@yopmail.com      | 5s4E3Oru   | levana      |         5 |
| 38 | Warren      | graquoizesiffau-1083@yopmail.com    | 43getvhj95 | mewler      |         7 |
| 39 | Anthony     | poucofrouwebri-9625@yopmail.com     | 4m6Lps1z7H | cute        |         3 |
| 40 | Gary        | nodoinneutteuseu-7018@yopmail.com   | V8F26nQH3R | mostly      |        10 |
| 41 | Clyde       | leidaunnacecra-5724@yopmail.com     | 8dUc6QI3R2 | navajo      |         4 |
| 42 | Christopher | soddautreitittu-1376@yopmail.com    | h0HhBs64w3 | ribose      |         6 |
| 43 | Russell     | dadeloihazi-9431@yopmail.com        | 1jINMsl690 | morpho      |         8 |
| 44 | Milton      | voufuddautono-9406@yopmail.com      | y4sBj425eJ | deltic      |         2 |
| 45 | Allan       | froteyauleussi-7742@yopmail.com     | 1x40Zt4jzJ | kopeck      |         1 |
| 46 | Raymond     | zaneuddatouru-5832@yopmail.com      | s476Jv0ef  | cutler      |         7 |
| 47 | Matthew     | queummeimmabreumou-5887@yopmail.com | 6V480ixDtK | huipil      |         9 |
| 48 | Peter       | jaxeipepouji-6411@yopmail.com       | lK5A4G27yo | naming      |         5 |
| 49 | Charles     | praxeujoibrisse-7897@yopmail.com    | GtwB91CJ37 | eileen      |         3 |
| 50 | Dwight      | sohofroloiteu-6768@yopmail.com      | n1y9EuYK21 | valuer      |         9 |


## Internet Cafe PC

This table contains data about computers located in the Internet cafe. It can also be auxiliary if you need, for example, to calculate the revenue from vip and pro computers, referring to their booking requests for the last month. Where is the rate per hour 3$.

The request for this will look like this:
```
SELECT 3*sum(Game_time_hour) AS Proceeds
FROM internet_cafe_reserv 
WHERE user_code_comp IN (
  SELECT Code 
  FROM internet_cafe_pc
  WHERE Status IN ('pro', 'vip')
);
```
With the result:

| Proceeds |
|----------|
|111       |


The [code for creating](Create_table_internet_cafe_PC.sql) this table looks like this:
```
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
```

It differs from the previous one by using a different data type for writing text, has a special ENUM data type that is well suited for entering computer status and has DEFAULT values.

[Data is loaded](Insert_internet_cafe_PC.sql) into the table no longer through INSERT INTO TABLE VALUES, but instead of VALUES, SELECT is used to enter data through an aggregate function applied to another table.

Request:
```
SELECT *
FROM internet_cafe_PC;
```
gives us:

| Code | Server_Name | CPU                                            | Main_Memory_Gb | RAM_Gb | GPU                                                    | Status | Users |
|------|-------------|------------------------------------------------|----------------|--------|--------------------------------------------------------|--------|-------|
|    1 | Nekit_1     | AMD Ryzen Threadripper 3990X 64-Core Processor |           2048 |     16 |  RTX 2080 Ti  TU102-300   1350Mhz 1545Mhz   11Gb GDDR6 | pro    |     5 |
|    2 | Nekit_2     | AMD EPYC 7R13 48-Core Processor                |           1024 |      8 |  GTX 1650 TU117-300 1485Mhz 1665Mhz 4Gb GDDR6          | def    |     5 |
|    3 | Nekit_3     | Intel Core I7-13700KF                          |           1024 |      8 |  GTX 980 Ti GM200-310 1000Mhz 1076Mhz 6Gb GDDR5        | def    |     5 |
|    4 | Nekit_4     | AMD Ryzen 5 7600X 6-Core Processor             |           1024 |      8 |  GTX 1080 Ti GP102-350 1480Mhz 1582Mhz 11Gb GDDR5X     | def    |     4 |
|    5 | Nekit_5     | AMD Ryzen 3 1200 Quad-Core Processor           |           1024 |      8 | GTX 1050 Ti GP107-400 1291Mhz 1392Mhz 4Gb GDDR5        | def    |     7 |
|    6 | Nekit_6     | AMD Ryzen 7 5700X 8-Core Processor             |           2048 |     16 | RTX 2060 TU106-300 1365Mhz 1680Mhz 6Gb GDDR6           | pro    |     4 |
|    7 | Nekit_7     | Intel Xeon CPU E5-2680 v3 @ 2.50GHz            |           2048 |     16 | RTX 2080 Super TU104-450 1350Mhz 1545Mhz 8Gb GDDR6     | pro    |     6 |
|    8 | Nekit_8     | AMD Ryzen 7 7700X 8-Core Processor             |           2048 |     32 | RTX 3060 GA106-300 1320Mhz 1777Mhz 8/16Gb GDDR6        | pro    |     6 |
|    9 | Nekit_9     | AMD Ryzen 9 3950X 16-Core Processor            |          10240 |     64 | RTX 3080 Ti GA102-225 1365Mhz 1665Mhz 12Gb GDDR6X      | vip    |     5 |
|   10 | Nekit_10    | Intel Xeon Platinum 8375C CPU @ 2.90GHz        |          10240 |     64 | RTX 3090 Ti GA102-350 1560Mhz 1860Mhz 24Gb GDDR6X      | vip    |     3 |


## Internet Cafe Reserv

This table has already appeared in the previous explanation. This table stores all online booking requests for the month. With its help, the staff of the Internet cafe can see which seats will be occupied and for how long. This will help when placing an order to customers who came to the institution itself.

The [code for creating](Create_table_internet_cafe_client.sql) this table looks like this:
```
CREATE TABLE internet_cafe.internet_cafe_reserv (
  ID int NOT NULL AUTO_INCREMENT,
  Date datetime NOT NULL DEFAULT '2023-04-29 00:00:00',
  Game_time_hour int NOT NULL DEFAULT 1,
  User_ID int NOT NULL DEFAULT 0,
  Name_user char(200) NOT NULL DEFAULT '',
  User_code_comp int NOT NULL DEFAULT 1,
  PRIMARY KEY (ID)
)
```

 In this case, the code to create does not differ from the previous one. You can only notice that another new DATETIME data type is used here, which allows you to quickly fill in with the date and time of booking using the NOW() function in the [data insertion request](Insert_internet_cafe_reserv.sql).
 To quickly add data to this table, I decided to use INSERT INTO TABLE SELECT and selection FROM internet_cafe_client ORDER BY RAND() LIMIT 1, which allows you to select random values (1 from each column) from the internet_cafe_client table and add them to the desired table. This allowed me to greatly reduce the time for entering data. 


Request:
```
SELECT *
FROM internet_cafe_PC;
```
gives us:

| ID | Date                | Game_time_hour | User_ID | Name_user | User_code_comp |
|----|---------------------|----------------|---------|-----------|----------------|
|  1 | 2023-04-29 21:02:25 |              2 |      10 | Ronnie    |             10 |
|  2 | 2023-04-29 21:02:25 |              3 |      16 | Carl      |              5 |
|  3 | 2023-04-29 21:02:25 |              2 |      29 | Andrew    |              3 |
|  4 | 2023-04-29 21:02:25 |              3 |       5 | Scott     |              5 |
|  5 | 2023-04-29 21:02:25 |              4 |      25 | Bruce     |              2 |
|  6 | 2023-04-29 21:02:25 |              1 |      17 | William   |              7 |
|  7 | 2023-04-29 21:02:25 |              5 |      30 | Roy       |              5 |
|  8 | 2023-04-29 21:02:25 |              5 |      13 | Sam       |              7 |
|  9 | 2023-04-29 21:02:25 |              3 |      43 | Russell   |              8 |
| 10 | 2023-04-29 21:02:25 |              6 |       2 | Kevin     |              2 |
| 11 | 2023-04-29 21:02:25 |              5 |      39 | Anthony   |              3 |
| 12 | 2023-04-29 21:02:25 |              6 |       1 | Josh      |              1 |
| 13 | 2023-04-29 21:02:25 |              2 |       7 | Fred      |              7 |
| 14 | 2023-04-29 21:02:25 |              5 |      37 | Jose      |              5 |
| 15 | 2023-04-29 21:02:26 |              4 |       8 | William   |              8 |
| 16 | 2023-04-29 21:02:26 |              3 |       4 | James     |              4 |
| 17 | 2023-04-29 21:02:26 |              2 |      23 | Timothy   |              1 |
| 18 | 2023-04-29 21:02:26 |              1 |       3 | Mike      |              3 |
| 19 | 2023-04-29 21:02:26 |              1 |      31 | Antonio   |              7 |
| 20 | 2023-04-29 21:02:26 |              4 |      49 | Charles   |              3 |
| 21 | 2023-04-29 21:02:26 |              4 |      33 | James     |              5 |
| 22 | 2023-04-29 21:02:26 |              3 |      15 | Calvin    |              1 |
| 23 | 2023-04-29 21:02:26 |              5 |      18 | Jacob     |             10 |
| 24 | 2023-04-29 21:02:26 |              2 |       6 | Jonathan  |              6 |
| 25 | 2023-04-29 21:02:26 |              1 |      46 | Raymond   |              7 |
