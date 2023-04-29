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
