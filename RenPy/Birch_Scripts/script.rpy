# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define n = Character('Никита', color="#c8ffc8")
define d = Character('Дима', color="#f08a5d")
define y = Character('Ясик', color="#17b978")
define t = Character('Татьяна Константиновна', color="#a6b1e1")
define ig = Character('Ирина Генадевна', color="#73b507")
define au = Character('...', color="#fcfefe")
define mn = Character('Мысли Никиты', color="#9e8a8a")
define md = Character('Мысли Димы', color="#9e8a8a")
define mv = Character('Марина Вадимовна', color="#22acc4")
define vse = Character('Все', color="#fcfefe")
define m = Character('Марина', color="#bd2be8")
define st = Character('Аня Ст.', color="#e9af88")
define so = Character('Аня Со.', color="#e3d37b")
define ay = Character('Айдан', color="#917be3")
define i = Character('Ира', color="#cfe37b")
define l = Character('???', color="#fcfefe")
define lu = Character('Любер', color="#17b978")
define mad = Character('Мама Димы', color="#ff003e")
define man = Character('Мама Никиты', color="#ff003e")
define din = Character('Дима и Никита', color="#fcfefe")
define pot = []
define daf = 0
define iko = 3
image bomb_in = Movie(play="C:/Users/user/Desktop/Проекты Python/den/game/bomb_in.webm")
image valve = Movie(play="C:/Users/user/Desktop/Проекты Python/den/game/valve.mp4")
image ea_g = Movie(play="C:/Users/user/Desktop/Проекты Python/den/game/ea_g.mp4")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    stop music
    play movie "ea_gw.webm"
    $ renpy.pause(8, hard=True)
    play movie "valvew.webm"
    $ renpy.pause(17, hard=True)
    play movie "bomb_in.webm"
    $ renpy.pause(10, hard=True)
    show com_non
    au ""                                                       # 1 эпизод
    play sound "Radar.mp3"
    au "{i}<звук будильника>{/i}"
    scene nek_com
    hide com_non
    show nikita at left
    stop sound
    mn "Ах ты..ж"
    mn "Опять вставать.."
    au "{i}Думал он изо дня в день.{/i}"
    mn "Ну ладно, пойду умоюсь..."
    hide nikita
    hide com_nikita
    show com_non
    au ""
    n "Ух водичка, нормалек!"
    mn "{i}Мдаа, лишь прохладные обьятья воды заставляли меня идти дальше каждый божий день.{/i}"
    n "Так, достаем линзу. Берееем и аккуратно вставляем в глаз."
    mn "{i}Линзы так же являются важной частью моей жизни.{/i}"
    mn "{i}Нибудь их, и я бы не увидел красу всех тех чудес, что произошли сегодня...{/i}"
    hide com_non
    scene nek_com
    show nikita at left
    mn "Ну, пойду похаваю."
    hide nikita
    hide com_nikita
    show com_non
    au "{i}Он быстро настряпал себе пару бутербродов и так же быстро их съел.{/i}"
    hide com_non
    scene nek_com
    au ""
    mn "Так, уже 7:40, пора выходить."
    scene nikita_dver
    show nikita
    hide nek_com
    au ""
    mn "{i}Я торопливо оделся и начал отперать входную дверь.{/i}"
    hide nikita
    show nek_gul
    au ""
    hide nek_gul
    play sound "zamok.mp3"
    au "{i}<звук замка двери>{/i}"
    scene nikita_odver
    stop sound
    au ""
    show nek_gul
    mn "{i}Я вышел из квартиры и напрвился к лифту.{/i}"
    hide nek_gul
    scene nek_lift
    hide nikita_odver
    show nek_gul
    mn "{i}Далее я направился к подъездной двери.{/i}"
    scene nikita_dom
    show nek_gul
    hide nek_lift
    mn "{i}Когда я вышел, я почувствовал легкий утренний ветерок, в перемешку с сонной мерзлотой.{/i}"
    mn "{i}На улице было темно. Светили фонари, помогая справиться с поздно-осенней темнотой, освещая дорогу в школу.{/i}"
    au "{i}И он ушёл навтречу приключениям.{/i}"
    hide nek_gul
    scene com_non
    hide nikita_dom
    au ""
    play sound "Hotline Miami - Dust.mp3"
    au "{i}<звук будильника>{/i}"
    scene dima_com
    show dima
    au ""
    stop sound
    md "Эхх, опять в шкилу."
    md "Пойду почищу зубы."
    scene com_non
    hide dima_com
    hide dima
    au "{i}И он ушел чистить зубы.{/i}"
    scene dima_com
    hide com_non
    show dima
    d "Ладно, сделаю себе чаек."
    scene com_non
    hide dima_com
    hide dima
    au "{i}И он пошел пить чай.{/i}"
    scene dima_kuhn
    hide com_non
    d "Ладно, нормальный чай. Сколько там время? Ого, уже 7:30, все, пора одеваться."
    scene dima_pri
    hide dima_kuhn
    show dima_odet
    md "Вот она моя броня!!!"
    au "{i}Сказал дима, выходя из квартиры.{/i}"
    #звук двери
    scene dima_odver
    show dima_odet
    hide dima_pri
    md "{i}Так, где там мои наушники, аа, вот они.{/i}"
    au "{i}Дима Надел наушники.{/i}"
    d "Так, какую музыку бы мне включить."
    menu:
        "Какую бы музыку мне включить?"
        "hyperpop luv":
            play music "hyperpop luv.mp3"
            d "О да. Это она!"
            init python:
                daf = 1
        "Дворы":
            play music "Дворы.mp3"
            d "Да, вот это настальгия."
            init python:
                daf = 3
        "La Seine":
            play music "La Seine.mp3"
            d "Привет Стоговой, а так нормас"
            init python:
                daf = 4
        "Hotline Miami 2 OST Decade Dance":
            play music "Hotline Miami 2 OST Decade Dance.mp3"
            d "Энергичненько"
            init python:
                daf = 5
        "Hotline Miami - Dust":
            play music "Hotline Miami - Dust.mp3"
            d "Спокойненько."
            init python:
                daf = 6
        "Страсть к курению":
            play music "Страсть к курению.mp3"
            d "О, прям в душу"
        "Сети":
            play music "сети.mp3"
            d "Качает как надо!"
        "Freaks":
            play music "Freaks.mp3"
            d "Неплохо"
        "Notion":
            play music "Notion.mp3"
            d "Во, моя любимая!"
        "The Setup":
            play music "The Setup.mp3"
            d "Как будто в гта"
    scene dima_lift
    hide dima_odver
    au "{i}Дима вышел из подъезда и сказал:{/i}"
    au "{i}Удачи мне в школе.{/i}"
    hide dima_odet
    scene com_non
    hide dima_lift
    au "{i}И они встретились в школе...{/i}"
    au "{i}Они переоделись, попутно разговаривая..{/i}"
    scene cab_merc
    hide com_non
    show nek_sk at right
    show dima_sk at left
    n "Да, это было бы классно."
    play sound "zvon.mp3"
    scene zvon
    hide cab_merc
    hide nek_sk
    hide dima_sk
    au "{i}Прозвинел звонок.{/i}"
    stop sound
    scene com_non
    hide zvon
    au "{i}Прошли два муторных урока метематики...{/i}"
    scene cab_merc
    hide com_non
    show nek_sk at right
    show dima_sk at left
    au ""
    hide nek_sk
    hide dima_sk
    show mar_vad at left
    mv "Ребята, следующие уроки будут в 33 кабинете."
    vse "{i}Здравствуйте, хорошо.{/i}"
    hide mar_vad
    show nek_sk at right
    show dima_sk at left
    n "Ну, раз так, пойду занесу вещи и прогуляюсь по школе."
    hide nek_sk with moveoutright
    show dima_sk at center with moveinright
    d "Хорошо, если что я в кабинете буду!"
    scene cab_33
    hide cab_merc
    show dima_sk at center
    menu:
        "С кем бы поговорить?"
        "Марина":
            show dima_sk at right
            show marina at left
            m "О, привет дим."
            m "Смотри какие у меня ноготочки."
            d "Фигня какая то."
            play sound "пощечина.mp3"
            au "<звук пощечины>"
            d "Ай, дура безмозглая!"
            m "Фу, Дима чмо!"
            hide marina
        "Аня стогова":
            show dima_sk at right
            show stogova at left
            d "Привет стогова."
            play sound "stog.mp3"
            st "Да блин отстань уже, надоел."
            stop sound
            d "Сама отстань!"
            hide stogova
        "Аня солодова":
            show dima_sk at right
            show solodova at left
            d "Привет."
            so "Привет."
            d "Пока."
            so "Пока."
            hide solodova
        "Айдан":
            show dima_sk at right
            show aydan at left
            d "Привет."
            ay "Принет."
            d "Где мой браслет?"
            ay "А все, его нет, отстань."
            hide aydan
        "Лиза":
            show dima_sk at right
            show liza at left
            md "{i}Ну нафиг, пробитая вся.{/i}"
            hide liza
        "Ира":
            show dima_sk at right
            show ira at left
            d "Привет."
            i "Привет."
            d "Скинь ножки."
            i "Сейчас))"
            d "Жду))"
            scene com_non
            hide cab_33
            hide dima_sk
            hide ira
            au "{i}Через некоторое время...{/i}"
            scene cab_33
            hide com_non
            show dima_sk at right
            show ira at left
            i "Все, скинула."
            d "Но они же из кфс..."
            i "А все, а все, попустила ботика!"
            hide ira
        "Артем":
            show dima_sk at right
            show artem at left
            d "Привет."
            d "Как там дела у маргариты?"
            play sound "art.mp3"
            hide artem with moveoutright
            au "{i}Артем заплакал и убежал.{/i}"
            stop sound
            hide artem
        "Ясик":
            show dima_sk at right
            show yasik at left
            d "Привет, как дела?"
            y "Нормально."
            d "А у меня?"
            y "Нормально."
            d "Опа, попался нефор."
            y "Сам такой."
            hide yasik
    menu:
        "С кем бы поговорить?"
        "Марина":
            show dima_sk at right
            show marina at left
            m "О, привет дим."
            m "Смотри какие у меня ноготочки."
            d "Фигня какая то."
            play sound "пощечина.mp3"
            au "<звук пощечины>"
            d "Ай, дура безмозглая!"
            m "Фу, Дима чмо!"
            hide marina
        "Аня стогова":
            show dima_sk at right
            show stogova at left
            d "Привет стогова."
            play sound "stog.mp3"
            st "Да блин отстань уже, надоел."
            stop sound
            d "Сама отстань!"
            hide stogova
        "Аня солодова":
            show dima_sk at right
            show solodova at left
            d "Привет."
            so "Привет."
            d "Пока."
            so "Пока."
            hide solodova
        "Айдан":
            show dima_sk at right
            show aydan at left
            d "Привет."
            ay "Принет."
            d "Где мой браслет?"
            ay "А все, его нет, отстань."
            hide aydan
        "Лиза":
            show dima_sk at right
            show liza at left
            md "{i}Ну нафиг, пробитая вся.{/i}"
            hide liza
        "Ира":
            show dima_sk at right
            show ira at left
            d "Привет."
            i "Привет."
            d "Скинь ножки."
            i "Сейчас))"
            d "Жду))"
            scene com_non
            hide cab_33
            hide dima_sk
            hide ira
            au "{i}Через некоторое время...{/i}"
            scene cab_33
            hide com_non
            show dima_sk at right
            show ira at left
            i "Все, скинула."
            d "Но они же из кфс..."
            i "А все, а все, попустила ботика!"
            hide ira
        "Артем":
            show dima_sk at right
            show artem at left
            d "Привет."
            d "Как там дела у маргариты?"
            play sound "art.mp3"
            hide artem with moveoutright
            au "{i}Артем заплакал и убежал.{/i}"
            stop sound
            hide artem
        "Ясик":
            show dima_sk at right
            show yasik at left
            d "Привет, как дела?"
            y "Нормально."
            d "А у меня?"
            y "Нормально."
            d "Опа, попался нефор."
            y "Сам такой."
            hide yasik
    menu:
        "С кем бы поговорить?"
        "Марина":
            show dima_sk at right
            show marina at left
            m "О, привет дим."
            m "Смотри какие у меня ноготочки."
            d "Фигня какая то."
            play sound "пощечина.mp3"
            au "<звук пощечины>"
            d "Ай, дура безмозглая!"
            m "Фу, Дима чмо!"
            hide marina
        "Аня стогова":
            show dima_sk at right
            show stogova at left
            d "Привет стогова."
            play sound "stog.mp3"
            st "Да блин отстань уже, надоел."
            stop sound
            d "Сама отстань!"
            hide stogova
        "Аня солодова":
            show dima_sk at right
            show solodova at left
            d "Привет."
            so "Привет."
            d "Пока."
            so "Пока."
            hide solodova
        "Айдан":
            show dima_sk at right
            show aydan at left
            d "Привет."
            ay "Принет."
            d "Где мой браслет?"
            ay "А все, его нет, отстань."
            hide aydan
        "Лиза":
            show dima_sk at right
            show liza at left
            md "{i}Ну нафиг, пробитая вся.{/i}"
            hide liza
        "Ира":
            show dima_sk at right
            show ira at left
            d "Привет."
            i "Привет."
            d "Скинь ножки."
            i "Сейчас))"
            d "Жду))"
            scene com_non
            hide cab_33
            hide dima_sk
            hide ira
            au "{i}Через некоторое время...{/i}"
            scene cab_33
            hide com_non
            show dima_sk at right
            show ira at left
            i "Все, скинула."
            d "Но они же из кфс..."
            i "А все, а все, попустила ботика!"
            hide ira
        "Артем":
            show dima_sk at right
            show artem at left
            d "Привет."
            d "Как там дела у маргариты?"
            play sound "art.mp3"
            hide artem with moveoutright
            au "{i}Артем заплакал и убежал.{/i}"
            stop sound
            hide artem
        "Ясик":
            show dima_sk at right
            show yasik at left
            d "Привет, как дела?"
            y "Нормально."
            d "А у меня?"
            y "Нормально."
            d "Опа, попался нефор."
            y "Сам такой."
            hide yasik
    scene zvon
    hide cab_33
    hide dima_sk
    hide yasik
    hide ira
    hide stogova
    hide solodova
    hide liza
    hide marina
    play sound "zvon.mp3"
    au "<Звонок>"
    scene com_non
    hide zvon
    stop sound
    au "Начался урок русского языка..."
    scene cab_33
    hide com_non
    show shitovas at left
    t "Тише, ну все, начинаем урок."
    t "У нас еще так много работы, а четверть уже кончается."
    t "Нужно все отшлифовать, по этому я дам вам небольшие работки со смешанными орфограммами."
    au "{i}Им выдали работы и они начали писать...{/i}"
    scene rab_nek
    hide cab_33
    hide shitovas
    mn "{i}Ну, вроде все понятно, она разрешила пользоваться папками, по этому пожалуй я ее использую...{/i}"
    scene com_non
    hide rab_nek
    au "{i}Тем временем работа Димы{/i}"
    scene rab_dima
    hide com_non
    md "{i}Да блин, опять эти работки, эхх, опять получу 2...{/i}"
    scene com_non
    hide rab_dima
    au ""
    au "{i}Прошло 20 минут и пришло время здавать работы.{/i}"
    scene cab_33
    hide com_non
    show shitovas at left
    mn "{i}Надеюсь хотябы 4 там будет.{/i}"
    md "{i}Хоть бы не 2, хоть бы не 2...{/i}"
    scene zvon
    hide cab_33
    hide shitovas
    play sound "zvon.mp3"
    au "<звонок>"
    scene cab_33
    hide zvon
    show shitovas at left
    stop sound
    t "Ну чтож, урок окончен."
    scene vtor
    hide shitovas
    show dima_sk at right
    au ""
    au "{i}Дима был на перемене и смотрел тик ток, но его прервал Никита.{/i}"
    show nek_sk at center with moveinleft
    n "Слушай, давай сегодня к горе сходим, чай попьем?"
    d "Ну вроде много на завтра не задавали, давай."
    n "Тогда во сколько примерно будем выходить?"
    d "А, я позвоню как все сделаю."
    d "Ты сможешь ко мне зайти?"
    n "Да, конечно."
    n "Тогда после школы созвонимся."
    d "Ага."
    scene com_non
    hide vtor
    hide nek_sk
    hide dima_sk
    au "{i}После уроков они встретились возле школы и решили пройтись...{/i}"
    scene dorsk
    hide com_non
    show dima_gul
    d "Слушай, нек, а что мы вообще будем делать на горе кроме чая?"
    hide dima_gul
    show nek_gul
    n "Ну, сейчас вроде сухо, можно будет костер развести."
    n "Веток и мелкого хвороста вроде должно нам хватить."
    hide nek_gul
    show dima_gul
    d "Да, будет классно, еще можно в ленту за маршмеллоу зайти."
    hide dima_gul
    show dima_gul_sm with dissolve
    d "Правда у меня деньги на карточке закончились..."
    d "Не мог бы ты..."
    hide dima_gul_sm
    show nek_gul
    n "Да да, конечно."
    hide nek_gul
    show dima_gul
    d "Фух, хорошо, спасибо."
    hide dima_gul
    show nek_gul
    n "Не за что)"
    n "Ну тогда пойдем дальше."
    hide nek_gul
    show dima_gul
    d "Ага."
    scene com_non
    hide dima_gul
    au "{i}Они прошлись и, будучи дома, Никита услышал звонок...{/i}"
    scene nek_dom_sid
    hide com_non
    play sound "call.mp3"
    au "<Звонок дискорда>"
    scene dis_govd
    hide nek_dom_sid
    stop sound
    play sound "join.mp3"
    au ""
    d "Привет"
    stop sound
    scene dis_govn
    hide dis_govd
    n "Привет"
    scene dis_govd
    hide dis_govn
    d "Ты как, сделал домашку?"
    scene dis_govn
    hide dis_govd
    n "Да, я уже поел, так что в принципе я готов выходить."
    scene dis_govd
    hide dis_govn
    d "Можешь тогда подходить, я пока алгебру доделаю."
    scene dis_govn
    hide dis_govd
    n "Хорошо, тогда я собираться, давай."
    scene dis_govd
    hide dis_govn
    d "Давай"
    au ""
    play sound "disconnect.mp3"
    scene com_non
    hide dis_govd
    au "Никита оделся и направился к дому димы, параллельно читая краткое содержание произведения, которое им задали в школе."
    au "Перед тем, как Никита зашел в дом, в него зашел еще один человек, и Никита кинулся к открытой двери."
    au "Он догнал дверь и вызвал лифт."
    scene dima_lift
    hide com_non
    show nek_gul
    mn "Блин, где там это лифт!"
    mn "Ааа, мне же дима говорил, что сейчас он очень плохо ездит и надо идти по лестнице."
    hide nek_gul with moveoutleft
    au ""
    scene dima_odver
    hide dima_lift
    au ""
    show nek_gul at center with moveinleft
    n "Фух, поднялся."
    mn "Так, пойду постучусь в дверь."
    play sound "zamok.mp3"
    au ""
    stop sound
    show nek_gul at right with moveinleft
    show dima_doma at left with moveinleft
    d "Привет Некит."
    n "Привет, вижу ты меня уже встречаешь."
    d "Ага, ты заходи, раздевайся."
    n "А, сейчас."
    scene dima_pri
    hide dima_odver
    hide dima_doma
    hide nek_gul
    show nek_gul
    play sound "zamok.mp3"
    au "Никита запер дверь и разделся."
    stop sound
    hide nek_gul
    show nek_doma with dissolve
    d "Иди помой пока руки!"
    n "Хорошо!"
    scene com_non
    hide dima_pri
    hide nek_doma
    au "Никита помыл руки и они начали обсуждать, что возьмут на гору."
    scene dima_kuhn
    hide com_non
    show nek_doma at right
    show dima_doma at left
    n "Ну давай пока поставим чайник."
    d "Ага"
    d "Я предлягаю еще бутербродов сделать и криветок сварить."
    n "О, давай, будет хоть чем там занться."
    d "Тогда ты пока делай бутерброды, хлеб в ящике а все остальное в холодильнике найдешь."
    n "Ага"
    d "А я пока криветки сварю."
    scene com_non
    hide dima_kuhn
    hide dima_doma
    hide nek_doma
    au "Пока они готовили, Дима завел разговор..."
    scene dima_pri
    hide com_non
    d "Слушай, я тут в одном паблике по Ярославлю прочитал, что где то на горажах видели какой то странный силуэт, стоявший прямо у склона горы."
    n "Ну наверно это был просто какой то человек, например работник с заправки неподалеку."
    n "Мы их давольно много раз там видели."
    d "Нет, это точно не просто какой то человек, его рост был больше двух метров и все тело было чем то обтянуто, что не видно было ни рук не ног."
    n "Интересно, но я все таки думаю что это просто какой то человек."
    n "В любом случае, посмотрим как оно будет."
    d "Ага"
    scene com_non with dissolve
    hide dima_pri
    au "А ведь они даже не подазревали, во что им это обернется..."
    scene dima_kuhn
    hide com_non
    show nek_doma at right
    show dima_doma at left
    au " "
    d "Так, ну вроде все убрали, пойдем одеваться."
    n "Пойдем"
    scene dima_pri
    hide dima_kuhn
    au " "
    hide nek_doma
    hide dima_doma
    show nek_gul at right
    show dima_gul
    d "Ну все, пойдем."
    scene com_non
    hide dima_pri
    hide nek_gul
    hide dima_gul
    play sound "zamok.mp3"
    au "Они вышли."
    stop sound
    au "Дима спросил"
    d "Куда сначала пойдем?"
    menu:
        "Куда сначала пойдем?"
        "Пойдем лучше сразу на гору":
            d "Ну ладно, давай"
        "Пойдем в ленту, как и договаривались":
            d "Ага, пошли."
            au "Они пошли в ленту и купили там 2 пачки маршмеллоу, одну простую, белую, вторую рузовую, клубничную."
            au "Никита все оплотил и они направились к горе."
    scene gor_per
    hide com_non
    show nek_gul at right
    show dima_gul at left
    d "Вот мы и пришли."
    n "Мда, уже успело нормально так потемнеть."
    n "Ну ладно, я пошел за хворостом, а ты пока все разложи."
    d "Хорошо."
    hide nek_gul
    hide dima_gul
    au "Никита ушлел собирать хворост, а Дима разбирать вещи."
    au "Когда Дима разобрал вещи, он начал помогать Никите."
    au "Никита отдавал Диме найденный хворост, а он сооружал их него подобие костра, и вскоре костер был готов."
    md "Пожалуй выключу пока музыку и наслажусь звуками костра."
    stop music
    play music "koster.mp3"
    scene gulkost with dissolve
    d "О да, вкусный чай получился, давай маршмеллоу открывать."
    n "Давай"
    au " "
    play sound "Freaks.mp3" volume 0.1
    d "Слушай, Нек."
    n "Что?"
    d "Как ты думаешь, сколько вот мы еще будем так гулять."
    d "Типа, когда то же мы можем разойтись, например я останусь на второй год, или уйду после 9, а ты будешь еще учиться в 10"
    n "Слушай, как по мне, если есть дружба и занятие, бодобно этому, которые приносит нам обоим лишь радостные воспоминания, я уверен, что мы всеми силами будем пытаться это все удержать."
    n "Не зависимо от приграждающих обстоятельств, мы будем дружить и гулять так же, как и сейчас."
    n "Возможно мы когда то выростем, у нас появятся дела и работа, но это все никогда не отберет у нас это чувство. И чем оно сильнее, тем выше рвение его заполучить вновь."
    d "Понятно, спасибо, а то в последнее время я начал задоваться этим вопросом."
    d "Кстати, а что это за музыка?"
    n "Да это я включил как обычно."
    d "Понятно"
    d "А, этот, чай будешь?"
    n "А, да, да"
    n "Конечно."
    stop sound
    play sound "vetka.mp3"
    "???" "<Хруст ветки>"
    d "Нек, ты слышал."
    d "Сверху ветка хрустнула."
    n "Ну ветер наверно надломил."
    d "Да нет, ее как будто кто то сломал."
    scene gulkost with zoomin
    d "НЕК!!!"
    d "ПОСМОТРИ НАВЕРХ!!!"
    scene luber_ber with dissolve
    hide gulkost
    n "Боже мой, что это такое!"
    d "Незнаю, но лучше не подовая виду потушить костер и уйти."
    n "Да, давай."
    scene com_non
    hide luder_ber
    stop music
    au "Они стремительно потушили костер и ушли без оглядки на нечто."
    au "Уйдя достаточно далеко они решили разойтись по домам..."
    scene nikita_dver with dissolve
    hide com_non
    au " "
    show nek_gul with dissolve
    n "Фухх"
    n "Я дома."
    hide nek_gul
    show nek_doma with dissolve
    au " "
    mn "Пойду в комнату, отдохну."
    hide nek_doma with zoomin
    scene nek_com
    show nek_doma at left with moveinright
    au " "
    hide nek_doma with moveoutright
    mn "Мдаа, пожалуй полчасика полежу"
    scene com_non with dissolve
    hide nek_com
    au "Тем временем у димы..."
    scene dima_pri with dissolve
    hide com_non
    show dima_odet
    au " "
    hide dima_odet
    show dima_doma with dissolve
    md "Фух, пойду за компик"
    hide dima_doma with zoomout
    scene dima_com
    hide dima_pri
    show dima_doma with zoomin
    d "Вот и компик!"
    hide dima_doma with zoomout
    scene com_non with dissolve
    hide dima_com
    au "Снова переместимся к Никите спустя 30 минут..."
    scene nek_com with dissolve
    n "Ну вроде отдохнул, пойду за компик."
    show nek_doma with moveinleft
    hide nek_doma with zoomout
    scene nek_dom_sid with dissolve
    hide nek_com
    mn "О, дима в Разных сидит."
    mn "Можно впринципе зайти."
    scene dis_govn
    play sound "join.mp3"
    n "Привет"
    scene dis_govd
    hide dis_govn
    d "Привет, ты нормально дошел?"
    scene dis_govn
    hide dis_govd
    n "Да, а ты?"
    scene dis_govd
    hide dis_govn
    d "Тоже"
    d "Я же днем говорил что там кто то будет."
    d "Думаешь это он?"
    scene dis_govn
    hide dis_govd
    n "Думаю да, но это точно не обычный человек был."
    n "Давай завтра сходим, проверим, только днем, что бы разглядеть если кто то будет."
    scene dis_govd
    hide dis_govn
    d "Ну давай, только как начнет темнеть сразу уйдем."
    scene dis_govn
    hide dis_govd
    n "Хорошо."
    n "Тогда до завтра."
    scene dis_govd
    hide dis_govn
    d "Да, давай."
    play sound "disconnect.mp3"
    scene com_non with dissolve
    hide dis_govd
    centered "Конец первого дня..."
    au ""                                                                       # 2 эпизод
    play sound "Radar.mp3"
    au "{i}<звук будильника>{/i}"
    stop sound
    scene nek_com with dissolve
    hide com_non
    au "..."
    show nek_sk at left with zoomin
    mn "Фух, хорошо умылся."
    mn "Ухх, ничего себе..."
    hide nek_sk
    scene nek_okn with dissolve
    mn "Вот это снегу за ночь наволило."
    mn "Нужно бы зимние ботинки уже одевать."
    scene nek_com
    hide nek_okn
    show nek_sk at left
    mn "Блин, времени уже 7:38, получается покушать я уже не успею."
    mn "Больно поздно встал, я ведь вчера после звонка даже ничего толком не успел сделать, сразу уснул."
    mn "Так и проспал"
    mn "Ну ладно, пойду тогда одеваться."
    hide nek_sk with zoomout
    scene com_non with dissolve
    au "Тем временем у Димы..."
    au ""
    play sound "Hotline Miami - Dust.mp3"
    au "{i}<звук будильника>{/i}"
    scene dima_com
    show dima
    stop sound
    au ""
    md "Да уж, что то я не выспался."
    md "Ну ладно, пойду покушаю."
    hide dima with moveoutright
    scene dima_kuhn
    hide dima_com
    au " "
    scene com_non with dissolve
    hide dima_kuhn
    au "Через 10 минут..."
    scene dima_kuhn with dissolve
    hide com_non
    d "Даа, хорошо позавтракал."
    d "Пойду одеваться."
    scene dima_pri
    hide dima_kuhn
    show dima_odet
    md "Вот так, можно выходить"
    scene dima_odver
    show dima_odet
    hide dima_pri
    md "Хм, что бы включить сегодня?"
    menu:
        "Хм, что бы включить сегодня?"
        "hyperpop luv":
            play music "hyperpop luv.mp3"
            d "О да. Это она!"
            init python:
                daf = 1
        "Дворы":
            play music "Дворы.mp3"
            d "Да, вот это настальгия."
            init python:
                daf = 3
        "La Seine":
            play music "La Seine.mp3"
            d "Привет Стоговой, а так нормас"
            init python:
                daf = 4
        "Hotline Miami 2 OST Decade Dance":
            play music "Hotline Miami 2 OST Decade Dance.mp3"
            d "Энергичненько"
            init python:
                daf = 5
        "Hotline Miami - Dust":
            play music "Hotline Miami - Dust.mp3"
            d "Спокойненько."
            init python:
                daf = 6
        "Страсть к курению":
            play music "Страсть к курению.mp3"
            d "О, прям в душу"
        "Сети":
            play music "сети.mp3"
            d "Качает как надо!"
        "Freaks":
            play music "Freaks.mp3"
            d "Неплохо"
        "Notion":
            play music "Notion.mp3"
            d "Во, моя любимая!"
        "The Setup":
            play music "The Setup.mp3"
            d "Как будто в гта"
    hide dima_odet with zoomout
    scene com_non with dissolve
    hide dima_odver
    au "Они направились в школу"
    au "Но по пути они встретились возле входа."
    scene sk_sn
    show nek_gul at left with moveinright
    au " "
    show dima_gul with moveinright
    n "О, привет Дим"
    d "Привет"
    n "Ну что, как поспал?"
    d "Я что то не сильно выспался, а ты?"
    n "Ну вроде неплохо поспал."
    d "Понятно."
    d "Пойдем дальше."
    n "Да, пойдем"
    scene com_non with dissolve
    hide sk
    au "..."
    scene cab_geogr with dissolve
    hide com_non
    show nek_sk at right with moveinleft
    show dima_sk at left with moveinleft
    n "Да, надеюсь не будет контрольной"
    show nek_sk at center with moveinright
    hide nek_sk with zoomout
    show dima_sk at center with moveinleft
    hide dima_sk with zoomout
    scene zvon
    hide cab_geogr
    play sound "zvon.mp3"
    au "<звонок>"
    stop sound
    scene com_non with dissolve
    hide zvon
    au "Прошел урок географии..."
    scene cab_merc with dissolve
    hide com_non
    show dima_sk at left with moveinleft
    show nek_sk at right with moveinright
    n "Слушай, Дим, а во сколько мы сегодня на гору пойдем."
    n "Просто мы довольно рано заканчиваем"
    d "Ну давай примерно через 2 часа, там как раз уроки сделаем."
    n "Ну хорошо, тогда созвонимся в дискорде."
    d "Ага"
    scene zvon with dissolve
    hide cab_merc
    hide nek_sk
    hide dima_sk
    play sound "zvon.mp3"
    au "<звонок>"
    stop sound
    scene com_non with dissolve
    hide zvon
    au "Начался урок алгебры."
    au "После алгебры Дима и Никита особо не разговаривали"
    au "Поскольку выпал снег урок физ-ры решили провести на лыжах..."
    scene dvsk_sn with dissolve
    show nek_gul with moveinleft
    show dima_gul at left with moveinleft
    d "Так, Нек, поможешь одеть лыжи?"
    n "Да, давай я встану на них."
    d "Давай"
    scene dvsk_sn with zoomin
    show dima_gul at left
    show nek_gul
    d "Спасибо."
    d "Тебе помочь?"
    n "Да не, сам одену."
    d "Ну хорошо, я тогда поехал."
    n "Ага"
    hide dima_gul with moveoutright
    scene dvsk_sn with zoomin
    show nek_gul with dissolve
    n "Ну вроде одел."
    n "Погнали!"
    hide nek_gul with moveoutright
    scene com_non with dissolve
    hide dvsk_sn
    au "Они катались, изредко перебрасываясь шутками между собой."
    au "Урок литературы ничем особым не выделялся."
    au "После уроков Дима сразу же ушел домой, поскольку у него был репетитор."
    au "А Никита в это время успел сделать все заданные уроки."
    scene nek_com_ur with dissolve
    hide com_non
    mn "Так, ну вроде все сделал."
    mn "Что там по времени?"
    scene nek_com_ur with zoomin
    mn "Хм, уже пол второго."
    mn "Что там Дима делает?"
    scene nek_dom_sid with dissolve
    hide nek_com_ur
    mn "Так, ну пока его онлайн нет, пойду пока видосики посмотрю."
    scene com_non
    hide nek_dom_sid
    au "Пара серий смешариков спустя..."
    scene nek_dom_sid with dissolve
    hide com_non
    play sound "call.mp3"
    mn "О, Дима звонит."
    stop sound
    play sound "join.mp3"
    scene dis_govd
    hide nek_dom_sid
    d "Привет"
    scene dis_govn
    hide dis_govd
    n "Привет"
    scene dis_govd
    hide dis_govn
    d "Можешь уже выходить."
    scene dis_govn
    hide dis_govd
    n "А ты уроки то сделал?"
    scene dis_govd
    hide dis_govn
    d "Ну я не все конечно сделал, ну остальное потом сделаю."
    scene dis_govn
    hide dis_govd
    n "Ясно, тогда я выхожу."
    scene dis_govd
    hide dis_govn
    d "Ага, я жду."
    d "Пока"
    scene dis_govn
    hide dis_govd
    n "Пока"
    play sound "disconnect.mp3"
    scene com_non with dissolve
    hide dis_govn
    au " "
    au "Никита, как и вчера, оделся, вышел и направился к диме."
    au "Возле подъезда Никита увидел бродячую вокруг да около собаку."
    au "Но так как это довольно распространенное явление, Никита не придал этому никакого значения и вошел в подъезд."
    scene dima_lift with dissolve
    hide com_non
    show nek_gul with moveinright
    au " "
    mn "О, вроде едет, это хорошо…"
    scene dima_lift with zoomin
    show nek_gul
    mn "Все, приехал"
    hide nek_gul with zoomout
    scene dima_odver
    show nek_gul with moveinleft
    mn "Хм, что то он меня не встречает, ну ладно, нужно постучать"
    show nek_gul at left with moveinleft
    play sound "stuk.mp3"
    au "<Стук в дверь>"
    stop sound
    play sound "zamok.mp3"
    au "<Дима отпирает дверь>"
    stop sound
    show nek_gul at center with moveinright
    show dima_doma at left with moveinleft
    d "Привет Нек"
    n "Привет"
    d "Заходи, я буду на кухне собираться"
    n "Хорошо"
    hide dima_doma with moveoutleft
    hide nek_gul with moveoutleft
    scene dima_pri
    hide dima_odver
    show nek_gul with zoomin
    hide nek_gul with dissolve
    show nek_doma with dissolve
    d "Иди сюда!"
    n "Сейчас!"
    hide nek_doma with moveoutright
    scene dima_kuhn
    hide dima_pri
    show dima_doma at left
    show nek_doma with moveinleft
    d "Так, мы же сегодня пораньше выходим, по этому давай сделаем что-нибудь по быстрому."
    n "Ну тогда я думаю лучше много всего не делать, давай сделаем пару бутеров и семечек возьмем."
    d "Давай, а мы будем костер разжигать?"
    n "Думаю нет, поскольку куча снега наволило, и все ветки скорее всего промокли."
    n "Можно просто посидеть, семечек поесть."
    d "Ну как то скучно одни семечки есть, давай хотя бы в ленту за чипсиками зайдем."
    n "Хорошо, а у тебя есть деньги?"
    d "Да, мне мама перевела."
    n "Тогда ладно."
    d "О чайник вскипел."
    hide dima_doma with moveoutleft
    d "Помоги с пакетиками."
    n "Ага."
    hide nek_doma with moveoutleft
    scene com_non with dissolve
    hide dima_kuhn
    au "Сделав чай и собрав все отстальное в рюкзак, они двинулись к выходу."
    au "Выйдя из подьезда, они увидели все ту же собаку и решили к ней подойти."
    au "Когда они подошли, она не убежала, а послушно пристроилась к их направлению."
    au "Дима решил погладить её, она тут же стала более энергичной и тоже начала осыпать Диму лаской."
    scene kisel with dissolve
    d "Нек, давай её назовем что ли."
    n "Давай, может компот?"
    d "Не, компот горький, давай лучше кисель, он вскуснее."
    n "Давай."
    d "Ну тогда ладно, пойдем дальше."
    n "Пойдем."
    scene com_non with dissolve
    hide kisel
    au "Но когда они пошли дальше, кисель пошла за ними и даже не отставала."
    au "Они попробывали пойти быстрее, но кисель все равно догоняла их."
    scene com_non with zoomin
    au "Так продолжалось до самой ленты."
    au "Дима попросил Никиту постоять на улице с киселем, пока он покупает чипсы."
    au "Кисель все так же послушно сидела возле Никиты."
    au "Дима вышел, и они пошли дальше."
    au "Прийдя на место, они тчательно все осмотрели."
    au "Но никаких следов кроме отломанной ветки найти не удалось."
    scene com_non with zoomin
    au "Уже изрядно стемнело..."
    scene gor_per_bl_zim with dissolve
    hide com_non
    show dima_gul
    show nek_gul at right
    n "Неплохо так уже потемнело."
    d "Ага, пойдем посмотрим что там кисель делает."
    n "Пойдем."
    hide nek_gul with moveoutright
    hide dima_gul with moveoutright
    scene gor_zad_kisel
    hide gor_per_bl_zim
    show nek_gul at right with moveinright
    show dima_gul with moveinright
    d "Она спит."
    d "Слушай, а давай её покормим, я сейчас в ленту сбегаю за сосисками."
    n "Давай, я с киселем посижу."
    d "Ага, я побежал."
    hide dima_gul with moveoutleft
    show nek_gul at center with moveinleft
    scene com_non with dissolve
    hide nek_gul with dissolve
    au "Дима убежал, а Никита сел возле киселя."
    au "А кисель все то пыталась уснуть, то подсаживалась к Никите, что бы он ее погладил."
    scene com_non with zoomin
    au "Через 15 минут Дима прибежал и принес пачку сосисок."
    au "Они кормили киселя по очререди, одну даст Дима, вторую Никита и так далее."
    au "Так кисель съела все сосиски и беззаботно легла спать."
    au "После этого Дима и Никита встали возле березы, у которой вчера жгли костер."
    scene gor_zad_zim with dissolve
    show nek_gul
    show dima_gul at left
    d "А сколько там время сейчас?"
    n "Сейчас 18:50, еще минут сорок посидим и пойдем."
    d "Хорошо."
    d "Давай тогда чипсики поедим."
    n "Давай, а ты где рюкзак кстати оставил?"
    d "А, он там, у склона."
    d "Сейчас принесу."
    hide dima_gul with moveoutleft
    au "Пока дима отошел, Никита услышал какой то звук возле березы, похожий на шаги."
    au "Он решил проверить и пошел подниматься к березе."
    show nek_gul at right with moveinright
    hide nek_gul with zoomout
    scene gor_zad_zim with zoomin
    show dima_gul with moveinleft
    d "Некит, ты где!"
    show nek_gul at right with zoomin
    show nek_gul at left with moveinright
    n "<слушай, там за березой кто то идет сюда>"
    d "<всмысле, кто это>"
    n "<не знаю, но это точно не заправщик>"
    n "<он себя в полотенце какое то замотал, и ходит босиком>"
    d "<слушай, а может это он>"
    d "<надо побыстрей бежa..."
    stop music
    show luber_bl at right with dissolve
    d "З-здрасте."
    au "Кисель почувствовала что то не ладное и залаела на незнакомца, но они ее успокоили."
    l "..."
    l "Привет"
    l "Что вы тут делаете?"
    d "Просто гуляем, да?"
    n "Ага."
    l "А что там на земле, не с березы ли сожженые ветки?"
    d "Ну не все конечно, мы просто костер вчера делали."
    l "А вы попросили разрешение у березы, извинились?"
    d "Вроде нет, а что такого, это же просто береза."
    l "Нет, это не просто береза."
    l "Когда мне было двадцать лет, я водил машину ночью и не справился с управлением."
    l "Если бы не эта береза, меня бы уже не было."
    l "Когда я ударился, меня начали отдавать на обследования разным врачам, и все говорили что у меня проблемы с головой."
    l "Они отправили меня в псих больницу, где эти 'врачи' делали мне уколы и давали кучу таблеток."
    l "Потом меня выписали, и я вернулся к своей спасительнице."
    d "Понятно, а сейчвс вы себя как чувствуете?"
    l "Голова все еще болит, а на лодони появилось какое то родимое пятно."
    l "А у тебя есть такое? протини руку."
    au "Дима протягивает руку, и незнакомец проводит пальцем по руке димы очертания своего пятна."
    d "Что вы делаете?!"
    l "Как я вижу у тебя его нет, это хорошо."
    n "<может пойдем уже от него>"
    d "Ааа, Некит, а сколько время?"
    n "19:10"
    d "Блин, нам нужно дома уже в 19:30 быть"
    d "Мы тогда пойдем"
    d "До свидания."
    l "Давайте"
    hide nek_gul with moveoutleft
    hide dima_gul with moveoutleft
    scene com_non with dissolve
    hide luber_bl with dissolve
    hide gor_zad_zim
    au "Дима и Никита, скрывшись из поля зрения незнакомца, побежали со всех ног к ленте, где много людей."
    au "Подойдя к ленте они заметили, что кисель по пути убежала в другом направлении."
    au "Дима попытался подозвать киселя, но она не возвращалась."
    au "Разочарованные Дима и Никита, зайдя в ленту, поднялись на футкорт, сели за стол и просидели там еще 30 минут, обсуждая произошедшее."
    au "Они были уверены, что он и был тем самым силуэтом, появляющемся на горе каждый день."
    scene com_non with zoomin
    au "После они прошлись до старого дома Никиты и разошлись на перекрестке."
    scene com_non with zoomin
    scene dima_lift with dissolve
    hide com_non
    show dima_gul with moveinleft
    d "Так, лифт едет, это хорошо."
    $ renpy.pause(1)
    d "А вот и он."
    hide dima_gul with zoomout
    scene dima_odver
    hide dima_lift
    show dima_gul with moveinleft
    d "..."
    hide dima_gul with zoomout
    scene dima_pri
    hide dima_odver
    show dima_gul with zoomin
    hide dima_gul with dissolve
    show dima_doma with dissolve
    mad "Дима! Ну как, собаку накормили."
    d "Да, все съела."
    mad "А сейчас она где, с Никитой?"
    d "Да нет, пока мы шли, она просто свернула и ушла в другую сторону."
    mad "Понятно, жалко конечно."
    d "Ага."
    hide dima_doma with zoomout
    scene dima_com
    hide dima_pri
    show dima_doma at right with moveinright
    md "Ну пойду за компик"
    show dima_doma at center with moveinright
    hide dima_doma at center with zoomout
    scene com_non with dissolve
    hide dima_com
    au "Тем временем Никита..."
    scene nikita_dom with dissolve
    hide com_non
    show nek_gul with moveinright
    hide nek_gul with zoomout
    scene nek_lift with dissolve
    show nek_gul
    hide nikita_dom
    hide nek_gul with moveoutright
    scene nikita_odver
    show nek_gul with zoomin
    play sound "zamok.mp3"
    n "..."
    stop sound
    scene nikita_dver
    show nek_gul with zoomin
    hide nek_gul with dissolve
    show nek_doma with dissolve
    man "Никит, ты!?"
    n "Да мам!"
    man "Что то ты долго сегодня, ничего не случилось?"
    n "Нет, просто в ленте засиделись."
    man "Ну ладно."
    hide nek_doma with zoomout
    scene nek_com with dissolve
    hide nikita_dver
    show nek_doma at left with zoomin
    mn "Так, ну пойду за компом отдохну"
    show nek_doma at center with moveinleft
    hide nek_doma with zoomout
    scene nek_dom_sid
    hide nek_com
    mn "Так, видимо я снова первый пришел домой, димы пока нет."
    mn "Ну что-ж, время видосиков!"
    scene com_non with dissolve
    hide nek_dom_sid
    au "Еще пару серий смешариков спустя."
    scene nek_dom_sid with dissolve
    hide com_non
    n "Давай Крош, вали эту няню."
    play sound "call.mp3"
    n "О, Дима звонит."
    stop sound
    scene dis_govn
    play sound "join.mp3"
    n "Привет"
    stop sound
    scene dis_govd
    hide dis_govn
    d "Привет, слушай, я тут подороге домой все искал, как того мужика вообще зовут или называют, но ничего не нашел."
    scene dis_govn
    hide dis_govd
    n "Ну может тогда сами его как нибудь назовем."
    scene dis_govd
    hide dis_govn
    d "Давай, какие идеи будут?"
    scene dis_govn
    hide dis_govd
    n "Ну смотри, я понял что он любит березы, можно из этого что то придумать."
    n "Как насчет 'Любер'."
    scene dis_govd
    hide dis_govn
    d "А что, неплохо звучит."
    d "Кстати, когда вот он по моей руке пальцем провел, у меня какой то след остался и не отмывается."
    scene dis_govn
    hide dis_govd
    n "Ну наверно это от того, что он не мылся уже сколько времени."
    scene dis_govd
    hide dis_govn
    d "Ну наверно, тогда ладно, до завтра."
    scene dis_govn
    hide dis_govd
    n "Давай, до завтра."
    scene com_non with dissolve
    play sound "disconnect.mp3"
    centered "Конец второго дня..."
    au ""                                                                   # 3 эпизод
    play sound "Radar.mp3"
    au "{i}<звук будильника>{/i}"
    stop sound
    scene nek_com with dissolve
    hide com_non
    show nek_sk with zoomin
    show nek_sk at left with moveinright
    n "Ууу-ааа! Хорошо выспался!"
    n "Даже встал пораньше, сейчас всего 6:30."
    mn "Пойду умоюсь да позавтракаю."
    hide nek_sk with zoomout
    scene com_non with dissolve
    hide nek_com
    au "Никита умылся, одел линзу и пошел завтракать."
    scene nek_kuhn with dissolve
    hide com_non
    show nek_sk at left with zoomin
    mn "Так, раз уж у меня столько времени, можно и яичницу с чаем сделать."
    show nek_sk at center with moveinleft
    hide nek_sk with zoomout
    scene com_non with dissolve
    hide nek_kuhn
    au "Никита принялся готовить кушать."
    au "После чего он покушал и пошел в комнату отлежаться до выхода."
    scene nek_com with dissolve
    hide com_non
    show nek_sk at left with zoomin
    mn "Уже 7:20, до 40 еще 20 минуток можно полежать..."
    show nek_sk at center with moveinleft
    hide nek_sk with zoomout
    scene com_non with dissolve
    hide nek_com
    au "Спустя 20 минут..."
    scene nek_com with dissolve
    hide com_non
    show nek_sk with zoomin
    show nek_sk at left with moveinright
    mn "Ну все, пора выходить."
    hide nek_sk with zoomout
    scene com_non with dissolve
    hide nek_com
    au "Тем временем у Димы..."
    au ""
    play sound "Hotline Miami - Dust.mp3"
    au "{i}<звук будильника>{/i}"
    scene dima_com
    show dima
    stop sound
    au ""
    d "Ууу-ааа! Какой то странный сон мне приснился."
    md "Ну ладно, пойду умываться и завтракать."
    show dima at right with moveinleft
    hide dima with zoomout
    scene com_non with dissolve
    hide dima_com
    au "Дима умылся и пошел завтракать."
    scene dima_kuhn with dissolve
    show dima at left with zoomin
    show dima at center with moveinleft
    md "Что бы покушать? Может просто бутеры сделаю, а то время уже 7:10"
    hide dima with zoomout
    scene com_non with dissolve
    hide dima_kuhn
    au "Дима сделал бутерброды и начал кушать."
    au "Он все вспоминал свой сон, там он видел этого 'Любера', он говорил с ним, что то борматал про дружбу и скорую разлуку с дорогим человеком."
    au "Он последние минуты сна твердил одну и ту-же фразу: 'ОСТЕРЕГАЙСЯ ЕГО!'. "
    au "Дима думал, что это просто какой то кошмар, но перед сном в тик-токе Дима увидел видео про вещие сны и подумал, что это он."
    scene dima_kuhn with dissolve
    show dima with zoomin
    d "Ну вроде хорошо подкрепился."
    d "Пойду одеваться."
    hide dima with moveoutleft
    scene dima_pri
    hide dima_kuhn
    show dima with moveinright
    hide dima with dissolve
    show dima_gul with dissolve
    md "Все, можно выходить."
    scene dima_odver with dissolve
    show dima_gul with moveoutleft
    hide dima_pri
    md "Что бы включить сегодня?"
    menu:
        "Что бы включить сегодня?"
        "hyperpop luv":
            play music "hyperpop luv.mp3"
            d "О да. Это она!"
            init python:
                daf = 1
        "Дворы":
            play music "Дворы.mp3"
            d "Да, вот это настальгия."
            init python:
                daf = 3
        "La Seine":
            play music "La Seine.mp3"
            d "Привет Стоговой, а так нормас"
            init python:
                daf = 4
        "Hotline Miami 2 OST Decade Dance":
            play music "Hotline Miami 2 OST Decade Dance.mp3"
            d "Энергичненько"
            init python:
                daf = 5
        "Hotline Miami - Dust":
            play music "Hotline Miami - Dust.mp3"
            d "Спокойненько."
            init python:
                daf = 6
        "Страсть к курению":
            play music "Страсть к курению.mp3"
            d "О, прям в душу"
        "Сети":
            play music "сети.mp3"
            d "Качает как надо!"
        "Freaks":
            play music "Freaks.mp3"
            d "Неплохо"
        "Notion":
            play music "Notion.mp3"
            d "Во, моя любимая!"
        "The Setup":
            play music "The Setup.mp3"
            d "Как будто в гта"
    show dima_gul with moveinright
    hide dima_gul with zoomout
    scene com_non with dissolve
    hide dima_odver
    au "Они пришли в школу."
    au "Перед уроками им не довелось поговорить, так как дима пришел чуть позднее звонка к началу урока информатики."
    au "После урока информатики Никита решил подойти к Диме пока они шли в зал."
    scene vtor with dissolve
    show dima_zadr_ot at left
    hide com_non
    show dima_zadr_ot at center with moveinleft
    show nek_zadr_ot at left with moveinleft
    n "Привет Дим."
    d "Привет."
    hide dima_zadr_ot with zoomout
    n "А во скольк..."
    show nek_zadr_ot at center with moveinleft
    mn "Чего это он? Ну ладно, нужно переодеваться."
    hide nek_zadr_ot with zoomout
    scene com_non with zoomout
    hide vtor
    au "После этого Никита не стал подходить к Диме, думал: 'Может покушать не успел? Потому и внимания на людей не обращает.'"
    au "'Возможно стоит поговорить с ним после того, как он покушает в столовой.'- предположил Никита..."
    scene stol with dissolve
    hide com_non
    show dima_sk with moveinleft
    show nek_sk at left with moveinleft
    n "Слушай, Дим."
    d "Ну что, только быстрее!"
    n "Во сколько мы на гору сегодня пойдем?"
    d "Как вчера, все, мне пора на урок."
    hide dima_sk with moveoutright
    show nek_sk at center with moveinleft
    mn "Похоже голод не единственная проблема, интересно, что с ним?"
    hide nek_sk with moveoutright
    scene cab_merc with dissolve
    show dima_sk at left
    hide stol
    show nek_sk at right with moveinright
    mn "Так, вчера мы в 15:30 вышли, значит и сегодня так."
    mn "Кажется, лучше ему написать, что-бы мы просто у остановки встретились. В гости лучше сегодня не ходить."
    scene zvon with dissolve
    hide cab_merc
    hide dima_sk
    hide nek_sk
    play sound "zvon.mp3"
    au "<звонок>"
    scene cab_merc
    hide zvon
    show dima_sk at left
    show nek_sk at right
    hide dima_sk with zoomout
    mn "Ну, пора на урок."
    show nek_sk at left with moveinright
    hide nek_sk with zoomout
    scene com_non with dissolve
    hide cab_merc
    au "Так прошел и весь учебный день, Никита стоял в одном углу, а Дима в другом."
    au "После последнего урока они так же не встретились, поскольку Никита просто ушел раньше."
    scene com_non with zoomin
    au "Дима, прийдя домой, сразу лег спать, так как сегодня было много уроков."
    au ""
    play sound "Hotline Miami - Dust.mp3"
    au "{i}<звук будильника>{/i}"
    stop sound
    scene dima_com
    show dima_doma with zoomin
    show dima_doma at right with moveinleft
    md "Так, сколько время, а 15:00, значит я всего 1 час поспал, ну ладно."
    md "Пойду уроки сделаю."
    show dima_doma at center with moveinright
    hide dima_doma with zoomout
    au "Делая уроки, Дима вспоминал сон, приснившийся только что."
    md "Блин, опять 'Любер' приснился, второй раз уже!"
    md "Теперь ему надо, что бы я не шел на остановку к Некиту, а вместо этого подождал еще час дома и пошел сразу на гору без ничего, даже телефона."
    md "Как же он меня достал, но делать нечего, два раза подряд это вряд-ли совпадение..."
    scene com_non with dissolve
    hide dima_com
    au "Тем временем Никита..."
    scene nikita_dom with dissolve
    hide com_non
    show nek_gul with moveinright
    hide nek_gul with zoomout
    scene nek_lift with dissolve
    show nek_gul
    hide nikita_dom
    hide nek_gul with moveoutright
    scene nikita_odver
    show nek_gul with zoomin
    play sound "zamok.mp3"
    n "..."
    stop sound
    scene nikita_dver
    show nek_gul with zoomin
    hide nek_gul with dissolve
    show nek_sk with dissolve
    n "Привет Мам!"
    man "Привет, что получил?"
    n "4 по истории и 5 по геометрии."
    man "Ну молодец. Кушать будешь?"
    n "Попозже, когда уроки сделаю."
    man "Хорошо."
    hide nek_sk with zoomout
    scene nek_com with dissolve
    hide nikita_dver
    show nek_sk at left with zoomin
    hide nek_sk with dissolve
    show nek_doma at left with dissolve
    mn "Ну, пойду тогда сразу уроки сделаю, а то уже кушать хочется."
    show nek_doma at center with moveinleft
    hide nek_doma with zoomout
    scene com_non with dissolve
    hide nek_com
    au "Никита сделал уроки и покушал."
    au "До выхода остовалось еще 30 минут, и Никита решил посидеть за компом."
    scene nek_dom_sid with dissolve
    mn "Хм, Дима еще даже в дискорд не зашел, как бы он не проспал встречу."
    mn "Ну ладно. Смешарики, ждите меня!"
    scene com_non with dissolve
    hide nek_dom_sid
    au "30 минут просмотра смешариков спустя.."
    scene nek_dom_sid with dissolve
    hide com_non
    mn "О, уже 15:30, пора выходить."
    scene com_non with dissolve
    hide nek_dom_sid
    au "Никита оделся, вышел и пошел на остановку."
    au "По пути он думал, прийдет ли Дима, или опять прийдется его будить?"
    au "Смотря на остановку там небыло никого, похожего на Диму, Никита подумал, что может он просто где-то вне поля зрения или просто еще дома."
    au "Но прийдя на место опасение подтвердилось, Димы нигде небыло, Никита позвонил ему уже 5-й раз, но трубку так ни кто и не взял."
    au "Так как такая ситуация уже происходила, Никита знал, что нужно делать."
    au "Он пошел к дому Димы и начал звонить в домофон. Ведь: 'В тот раз же проснулся, значит и сейчас должен проснуться.'"
    scene com_non with zoomin
    au "Но он не просыпался."
    au "По крайней мере делал вид, что спит, мы ведь все знаем, 'почему' он не отвечает..."
    scene dima_odver with dissolve
    hide com_non
    show nek_gul at left
    show nek_gul at center with moveinleft
    mn "Блин, даже на стук не реагирует, может там все таки никого нет."
    mn "Тогда где же Дима, не уж-то он взял и без меня куда то пошел даже не предупредив."
    mn "Вот что действительно на него не похоже."
    mn "Но куда он мог уйти, да и если ушел, то наверно должен был в телефон хоть раз заглянуть и увидеть что я ему звоню."
    mn "А ну ка..."
    au "Никита захотел проверить, не остался ли телефон в квартире и позвонил Диме еще раз."
    show nek_gul at left with moveinright
    play sound "gudki.mp3"
    au "<Пошли гудки>"
    stop sound
    au "Никита прислушался, было плохо слышно, но он отчетливо разобрал мелодию на рингтоне Димы."
    show nek_gul at center with moveinleft
    mn "Ну конечно, телефон там."
    mn "Но зачем Дима ушел без телефона, может он просто в магазин пошел, это же быстро, телефон там не нужен."
    mn "Так, тогда нужно обойти все магазины, куда может пойти Дима."
    show nek_gul at left with moveinright
    hide nek_gul with zoomout
    play sound "zamok.mp3"
    au ""
    show dima_doma with moveinleft
    md "Так, он ушел, уже почти час прошел, нужно уходить."
    hide dima_doma with moveoutleft
    play sound "zamok.mp3"
    au ""
    stop sound
    scene com_non with dissolve
    hide dima_odver
    au "Никита сразу же побежал в лотос, так как он был ближе всего."
    au "Нужно было двигаться быстро, потому что никто не знает, когда и из какого магазина он выйдет."
    au "В лотосе Димы не окозалось, и он побежал в магнит через дорогу, все время поглядывая по сторонам."
    scene com_non with zoomin
    au "Близится вечер, а Никита так и не нашел Диму."
    au "Оббежав все магазины, он простоял еще полтора часа возле Диминого дома, даже успел сбегать в пекарню, так как проголодался."
    au "И все же, через пол часа приехала мама Димы. Она обратила на замерзшего Никиту внимание и спросила, почему он тут стоит."
    au "Никита ответил, что ждет Диму. Но она возразила, ведь перед выходом Дима позвонил маме и сказал, что ушел гулять с Никитой на гору."
    au "На что Никита, импровизируя, ответил: 'А он мусор забыл выбросить, вот стою, жду.'"
    au "В тот момент Никите сильно повезло, ведь мама действительно попросила Диму вынести мусор, но он это сделал сразу же, как ушел."
    au "Они разошлись и Никита тут-же понял что осталось единственное место - Гора."
    scene com_non with zoomin
    au "Тем временем Дима пришел на гору..."
    scene gor_per_bl_zim with dissolve
    hide com_non
    show dima_gul at left with moveinright
    d "Ну и что мне здесь дел..."
    show luber_bl with moveinright
    lu "Ну здравствуй Дима."
    d "Так это все таки было не совпадение."
    lu "Да, но что важнее, ты сделал так, как я сказал тебе ночью?"
    d "Да, но я думаю Никита на меня сильно обидется после этого."
    lu "Ты сделал как нужно."
    d "Всмысле?! Что в этом хорошего?"
    lu "В этом есть нечто очень хорошее..."
    lu "ДЛЯ МЕНЯ!"
    d "Всмысле?!"
    show dima_gul at right with moveinleft
    d "почему?!!"
    lu "Похоже 'бродяга' сработала не так как надо."
    lu "По сути ты должен отключиться и забыть своего друга через 3..."
    lu "...2..."
    lu "...1..."
    hide dima_gul with zoomout
    lu "..."
    lu "А, значит все сработало как надо."
    lu "Пойду к березе."
    hide luber_bl with moveoutright
    scene com_non with dissolve
    hide gor_per_bl_zim
    au "К тому времени Никита несся со всех ног к горе."
    au "Уже возле пешеходного перехода Никита встретил нежданного гостя."
    au "'Кисель!'- радостно воскликнул Никита."
    au "Она видимо привязалась к этому месту и подумала, что сегодня в это время она сново встретит Диму и Никиту."
    au "И не прогодала! Она сразу, узнав голос Никиты подбежала к нему и тут же начала провожать Никиту через дорогу."
    au "Возможно в прошлом она была поводырем? Но когда Никита вдруг побежал она не стала медлить и бросилась в догонку."
    au "Прибежав на место они обнаружили жуткую картину."
    au "Дима лежит без сознания, а 'Любер' что то бормочит возле березы..."
    scene gor_per_bl_zim with dissolve
    show nek_gul with moveinright
    n "Господи! Дима!"
    show nek_gul at right with moveinleft
    hide nek_gul with zoomout
    n "Дима! Вставай!"
    au "Дима все не приходил в себя, а тем временем 'Любер' направился на шум."
    au "Но Кисель вдруг залаела громче Никиты и набросилась на 'Любера', повалив его на снег."
    n "О, проснулся!"
    show nek_gul at right with zoomin
    show nek_gul at center with moveinright
    show dima_gul at right with zoomin
    d "Ты кто вообще, что тут происходит, я же просто был в школе!!"
    n "Дима, ты что, ничего не помнишь?"
    d "Нет и откуда ты меня знаешь?"
    n "Я же твой друг, Никита, мы же знакомы больше 5 лет!"
    d "Я ничего такого не помню."
    n "Просто поверь мне, попробуй вспомнить."
    n "Как мы с тобой играли на переменах, болтали по дискорду, гуляли в конце концов!"
    d "Я пытаюсь, ничего не выходит, ни кто из моих друзей Никит так со мной не общались, тем более не учились!"
    n "Так, ладно, у нас мало времени, просто слушай..."
    hide nek_gul
    hide dima_gul
    stop music
    scene gulkost_pom with dissolve
    hide gor_per_bl_zim
    play sound "Freaks.mp3" volume 0.1
    d "Слушай, Нек."
    n "Что?"
    d "Как ты думаешь, сколько вот мы еще будем так гулять."
    d "Типа, когда то же мы можем разойтись, например я останусь на второй год, или уйду после 9, а ты будешь еще учиться в 10"
    n "Слушай, как по мне, если есть дружба и занятие, бодобно этому, которые приносит нам обоим лишь радостные воспоминания, я уверен, что мы всеми силами будем пытаться это все удержать."
    n "Не зависимо от приграждающих обстоятельств, мы будем дружить и гулять так же, как и сейчас."
    n "Возможно мы когда то выростем, у нас появятся дела и работа, но это все никогда не отберет у нас это чувство. И чем оно сильнее, тем выше рвение его заполучить вновь."
    stop sound
    scene gor_per_bl_zim with dissolve
    hide gulkost_pom
    show nek_gul
    show dima_gul at right
    d "Понятно, спасибо, а то в последнее время я начал задоваться этим вопросом."
    n "Д-дима, ты что-же, вспомнил это?"
    d "Да нек, я все помню, в том числе и то, что 'Любер' наложил мне на руку какую то 'бродягу', которая упровляет моим разумом."
    d "А это же..."
    d "Кисель раздирает 'Любера'?!"
    n "Да, я встретил ее по дороге."
    n "Пойдем, подойдем к нему."
    d "Ну пошли."
    hide dima_gul with moveoutright
    hide nek_gul with moveoutright
    scene gor_zad_zim
    show nek_gul with moveinleft
    show dima_gul at left with moveinleft
    lu "УБЕРИТЕ ЭТУ СОБАКУ!!!"
    n "Только если ты уберешь 'Бродягу' с руки Димы и уберешься из Ярославля!"
    lu "Хорошо! Хорошо!"
    au "И вдруг 'Бродяга' с руки Димы исчезла."
    n "Кисель, ко мне!"
    show luber_bl at right with zoomin
    lu "Она же меня чуть не загрызла!"
    din "Выпоняй вторую часть договора!"
    lu "Ладно, остовяю свою березу вам, делайте с ней все что ходите."
    hide luber_bl with moveoutright
    au "'Любер' ушел и будто растворился в глуши деревьев."
    n "Ну что Димас, с ним покончено!"
    d "Ага, пошли домой, а то уже сильно стемнело."
    n "Да, пошли."
    hide dima_gul with moveoutleft
    hide nek_gul with moveoutleft
    scene com_non with dissolve
    au "Они со спокойной душой пошли к дому Никиты, но они и не заметили, как Кисель снова ушла в неизвестном направлении. Они решили сесть и поговорить."
    scene razg_dim with dissolve
    hide com_non
    d "Слушай, а ты не обижаешься на меня за сегодня?"
    scene razg_nek
    hide razg_dim
    n "Нет конечно, я же понимаю что это ты не со зла"
    scene razg_dim
    hide razg_nek
    d "Фух, хорошо, слушай, а сколько в итоге время то?"
    d "Я то просто свой телефон дома оставил."
    scene razg_nek
    hide razg_dim
    n "А, сейчас, 20:11 уже."
    n "Блин, тут даже мне уже нужно дома быть."
    n "А тебя не наругают, когда ты прийдешь?"
    scene razg_dim
    hide razg_nek
    d "Да вроде не должны."
    scene razg_nek
    hide razg_dim
    n "А, еще забыл самое главное сказать."
    n "Я же, когда у твоего дома стоял тебя ждал приехала твоя мама и спросила что я тут стою."
    n "А я ответил что ты забыл мусор выбрасить и просто стою жду тебя у подьезда."
    scene razg_dim
    hide razg_nek
    d "Кстати хорошо ответил, она как раз попросила меня его выбросить, но я его выбрасил, когда только вышел."
    d "Тебе повезло"
    scene razg_nek
    hide razg_dim
    n "О, класс, тогда давай, до дискорда."
    scene razg_dim
    hide razg_nek
    d "Да, до дискорда."
    scene com_non with dissolve
    hide razg_dim
    au "Они разошлись, и так как Никита был уже рядом со своим домом с него и начнем..."
    scene nikita_dver with dissolve
    show nek_gul
    play sound "zamok.mp3"
    au ""
    stop sound
    hide nek_gul with dissolve
    show nek_doma with dissolve
    man "Никит, ты опять поздно приходишь, что ты там делаешь?"
    n "Да ничего, просто заговорились во дворе, я думал к 20:00 прийду."
    man "Ну ладно, тебе макароны наложить?"
    n "Да, давай."
    hide nek_doma with zoomout
    scene nek_com with dissolve
    hide nikita_dver
    show nek_doma at left with zoomin
    mn "Блин, как же я устал от этой беготни, ну ладно, пойду в дискорд зайду."
    show nek_doma at center with moveinleft
    hide nek_doma with zoomout
    scene nek_dom_sid with dissolve
    hide nek_com
    mn "Так, все, пока там Дима идет домой схожу покушаю."
    scene com_non with dissolve
    hide nek_dom_sid
    au "Дима уже добежал до дома, давайте посмотрим на это..."
    scene dima_pri with dissolve
    hide com_non
    show dima_gul
    play sound "zamok.mp3"
    au ""
    stop sound
    hide dima_gul with dissolve
    show dima_doma with dissolve
    mad "Дим!"
    d "Что!"
    mad "А почему ты Никиту у подьезда оставил, пустил бы в подьезд, он там замерз уже весь."
    d "Да, это, он сам попросил, я там быстро сбегал."
    mad "Ну хорошо."
    hide dima_doma with zoomout
    scene dima_com with dissolve
    hide dima_pri
    show dima_doma with moveinleft
    d "Как же я устал, пойду с Некитом поговорю и спать."
    hide dima_doma with zoomout
    scene com_non with dissolve
    hide dima_com
    au "А Никита уже и покушать успел..."
    scene nek_dom_sid with dissolve
    hide com_non
    mn "Так, о, Дима в дискорде."
    scene dis_govn
    hide nek_dom_sid
    play sound "join.mp3"
    n "Привет Дим."
    scene dis_govd
    hide dis_govn
    d "Привет, слушай, а ты спать не хочешь?"
    scene dis_govn
    hide dis_govd
    n "Нет конечно, я же не бегал за тобой 3 часа подряд!"
    scene dis_govd
    hide dis_govn
    d "Ну да, тупой вопрос, я тоже сильно устал."
    d "Ты пойдешь завтра гулять?"
    scene dis_govn
    hide dis_govd
    n "Да, если не будет много домашки, а хотя завтра же пятница."
    n "Тогда пойду."
    scene dis_govd
    hide dis_govn
    d "Класс, ну что, пойдем на гору?"
    scene dis_govn
    hide dis_govd
    n "Конечно, зря 'Любера' выгоняли что ли."
    n "Сожжем столько веток с его березы, сколько сможем достать."
    scene dis_govd
    hide dis_govn
    d "Да, давай, и маршмеллоу купим."
    scene dis_govn
    hide dis_govd
    n "Ага, я оплачу."
    scene dis_govd
    hide dis_govn
    d "Хорошо, спасибо."
    d "Ну что, тогда до завтра."
    scene dis_govn
    hide dis_govd
    n "Да, до завтра, спокойной ночи. Друг"
    scene dis_govd
    hide dis_govn
    d "И тебе спокойной ночи. Друг"
    scene com_non with dissolve
    hide dis_govd
    play sound "disconnect.mp3"
    au ""
    stop sound
    centered "Конец третьего дня..."
    centered "Поздравляем с прохождением нашей игры!"
    centered "И большое спасибо за ваше внимение!"
    play movie "titri 2.avi"
    $ renpy.pause(72, hard=True)
    menu:
        "Выберите доступное DLC"
        "В Главное меню":
            pass
        "На рабочий стол":
            python:
                import os
                os.system("taskkill /im pythonw.exe")

    return