# Bot_for_an_investment_company
### Link internet cafe bot: [Nekit_investment_company_bot](http://t.me/Nekit_investment_company_bot)

I decided to fulfill one order that interested me on one russian freelance exchange, see how it is and everything is going.

![order](order.png)

The customer writes: You need to develop a bot for an investment company with an attached TS.
Since the order condition did not specify the order completion time, I set myself the task of completing it in 1 day.

Directly TS:

![TS](TS_on_the_bot.jpg)

Also here is the [pdf format](TS_on_the_bot.pdf)

## Nekit_investment_company_bot

So, it's 20:20 and the bot is ready, and I started at 14:00
Well, I think it turned out quite well. First, I started [creating a table](create_table_Invest_comp.sql) based on the data in the message with the lot characteristics and mandatory data when describing the existing object. Well, it turned out a lot of columns...

| id | position                                  | area       | full_price      | current_price | resale_price  | projected_price_no_repair | projected_price_whith_repair | planned_profitability | yearly | implementation_period | amount_of_attraction     | iden   | summa   | opisanie                     | status  |
----|-------------------------------------------|------------|-----------------|---------------|---------------|---------------------------|------------------------------|-----------------------|--------|-----------------------|--------------------------|--------|---------|------------------------------|---------|
|  1 | Cанкт-Петербург, ул.Замшина, д.31, корп.4 | 17.8 кв.м. | 2.142 млн. руб. | 190 тыс. руб. | 315 тыс. руб. | 2.8 млн. руб.             | 3.2 млн. руб.                | 20-24%                | 36-41% | 3-4 мес.              | от 0.3 до 1.15 млн. руб. | Nikita | 1000000 | помещение площадью 17,8 кв.м | нежилое |

Next, I registered all the selection requests, formatted the strings and saved them to a list, the data from which goes to the object message. I wrote a yield calculator using the same data from the table and began to rewrite all the messages from the "Варианты инвестирования" section and attach the corresponding buttons to them.

I also took care of the "Мои объекты" section in advance. In the same MySQL table, I added 4 additional columns with the necessary data, included respectively in 1 and the same record. In a good way, it was necessary to create 2 tables with separate attachments, so that later it would be easier for the administrator to enter separate data, but this option is also suitable for demonstration.

### In conclusion
It is safe to say that the order was successfully completed on time.