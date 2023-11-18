let ves = document.querySelector(".Butt_ves");
let dan = document.querySelector(".Butt_Dan");
let ras = document.querySelector(".Butt_Ras");
let vr = document.querySelector(".Butt_Vr");
let temp = document.querySelector(".Butt_Temp");
let con_ves = document.getElementById("con_ves");
let con_dan = document.getElementById("con_dan");
let con_ras = document.getElementById("con_ras");
let con_vr = document.getElementById("con_vr");
let con_temp = document.getElementById("con_temp");
let mill = document.querySelector(".Butt2_mill");
let gramm = document.querySelector(".Butt2_gramm");
let kilo = document.querySelector(".Butt2_kilo");
let cent = document.querySelector(".Butt2_cent");
let tonn = document.querySelector(".Butt2_tonn");
let bit = document.querySelector(".Butt2_bit");
let bait = document.querySelector(".Butt2_bait");
let kiloba = document.querySelector(".Butt2_kiloba");
let mega = document.querySelector(".Butt2_mega");
let giga = document.querySelector(".Butt2_giga");
let tera = document.querySelector(".Butt2_tera");
let peta = document.querySelector(".Butt2_peta");
let millme = document.querySelector(".Butt2_millme");
let sant = document.querySelector(".Butt2_sant");
let deci = document.querySelector(".Butt2_deci");
let met = document.querySelector(".Butt2_met");
let kilome = document.querySelector(".Butt2_kilome");
let megame = document.querySelector(".Butt2_megame");
let millsec = document.querySelector(".Butt2_millsec");
let sec = document.querySelector(".Butt2_sec");
let min = document.querySelector(".Butt2_min");
let chas = document.querySelector(".Butt2_chas");
let sut = document.querySelector(".Butt2_sut");
let ned = document.querySelector(".Butt2_ned");
let god = document.querySelector(".Butt2_god");
let cels = document.querySelector(".Butt2_cels");
let far = document.querySelector(".Butt2_far");
let kelv = document.querySelector(".Butt2_kelv");
let Rassch = document.getElementById("Rassch");
let sbr = document.getElementById("sbr");
let inputa = document.getElementById("input");
let pri = document.getElementById("pri");

var c = [con_ves.className, con_dan.className, con_ras.className, con_vr.className, con_temp.className];
var prim = ["container_ves_on", "container_Dann_on", "container_Rass_on", "container_Vr_on", "container_Temp_on"];
var x = "";
var ri = 0;
var a = 0;
var b = 0;
var t = 0;
var d = 0;
var e = 0;
var j = 0;
var g = 0;
var k = 0;
var elementBr = document.createElement('br');

function prco_ve(a, b, t, d, j) {
    pri.innerHTML = a + ' Миллиграмм <br>' + b + ' Грамм <br>' + t + ' Килограмм <br>' + d + ' Центнеров <br>' + j + ' Тонн';
};

function prco_d(a, b, t, d, j, e, g) {
    pri.innerHTML = a + ' Бит <br>' + b + ' Байт <br>' + t + ' Килобайт <br>' + d + ' Мегабайт <br>' + j + ' Гигабайт <br>' + e + ' Терабайт <br>' + g + ' Петобайт';
};

function prco_r(a, b, t, d, j, e) {
    pri.innerHTML = a + ' Миллиметров <br>' + b + ' Сантиметров <br>' + t + ' Дециметров <br>' + d + ' Метров <br>' + j + ' Километров <br>' + e + ' Мегаметров';
};

function prco_vr(a, b, t, d, j, e, g) {
    pri.innerHTML = a + ' Миллисекунд <br>' + b + ' Секунд <br>' + t + ' Минут <br>' + d + ' Часов <br>' + j + ' Суток <br>' + '≈ ' + e + ' Недель <br>' + g + ' Лет';
};

function prco_t(a, b, t) {
    pri.innerHTML = a + ' Градусов по Цельсию <br>' + b + ' Градусов по Фаренгейту <br>' + t + ' Градусов по Кельвину';
};

function f() {
    c = [con_ves.className, con_dan.className, con_ras.className, con_vr.className, con_temp.className];
    var result = c.some(function(element) {
        if (prim.includes(element)) {
            foundValue = element;
            return true;
        }
        else {
            foundValue = 0;
        }
        return false;
    });
    console.log(c);
    console.log(result);
    console.log(foundValue);
};

/*------------------------------------------------------------------------*/

function refreshPage() {
    location.reload(true);
};

sbr.onclick = function() {
    if (con_ves.className == prim[0]) {
        con_ves.classList.toggle("container_ves_on");
        con_ves.classList.toggle("container_ves_off");
    };
    if (con_dan.className == prim[1]) {
        con_dan.classList.toggle("container_Dann_off");
        con_dan.classList.toggle("container_Dann_on");
    };
    if (con_ras.className == prim[2]) {
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
    };
    if (con_vr.className == prim[3]) {
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");  
    };
    if (con_temp.className == prim[4]) {
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
    };
    if (ri == 1) {
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
        ri = 0;
    };
    if (inputa.value != null || inputa.value != undefined) {
        inputa.value = null;
    };
    if (pri.textContent != null || pri.textContent != undefined) {
        pri.textContent = '';
    };
    if (inputa.value != 1000) {
        inputa.value = 1000;
    };
};

ves.onclick = function() {
    f();
    if (foundValue == 0) {
        con_ves.classList.toggle("container_ves_on");
        con_ves.classList.toggle("container_ves_off");
        sbr.classList.toggle("sbr_off");
        sbr.classList.toggle("sbr_on");
    };
    if (foundValue == prim[0]) {
        con_ves.classList.toggle("container_ves_on");
        con_ves.classList.toggle("container_ves_off");
        sbr.classList.toggle("sbr_on");   
    };
    if (foundValue == prim[1]) {
        con_dan.classList.toggle("container_Dann_off");
        con_dan.classList.toggle("container_Dann_on");
        con_ves.classList.toggle("container_ves_on");
        con_ves.classList.toggle("container_ves_off");
    };
    if (foundValue == prim[2]) {
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
        con_ves.classList.toggle("container_ves_on");
        con_ves.classList.toggle("container_ves_off");
    };
    if (foundValue == prim[3]) {
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");
        con_ves.classList.toggle("container_ves_on");
        con_ves.classList.toggle("container_ves_off");
    };
    if (foundValue == prim[4]) {
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
        con_ves.classList.toggle("container_ves_on");
        con_ves.classList.toggle("container_ves_off");
    };
};

dan.onclick = function() {
    f();
    if (foundValue == 0) {
        con_dan.classList.toggle("container_Dann_on");
        con_dan.classList.toggle("container_Dann_off");
    }
    if (foundValue == prim[0]) {
        con_ves.classList.toggle("container_ves_off");
        con_ves.classList.toggle("container_ves_on");
        con_dan.classList.toggle("container_Dann_on");
        con_dan.classList.toggle("container_Dann_off");
    };
    if (foundValue == prim[1]) {
        con_dan.classList.toggle("container_Dann_on");
        con_dan.classList.toggle("container_Dann_off");  
    };
    if (foundValue == prim[2]) {
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
        con_dan.classList.toggle("container_Dann_on");
        con_dan.classList.toggle("container_Dann_off");
    };
    if (foundValue == prim[3]) {
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");
        con_dan.classList.toggle("container_Dann_on");
        con_dan.classList.toggle("container_Dann_off");
    };
    if (foundValue == prim[4]) {
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
        con_dan.classList.toggle("container_Dann_on");
        con_dan.classList.toggle("container_Dann_off");
    };
};

ras.onclick = function() {
    f();
    if (foundValue == 0) {
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off"); 
    };
    if (foundValue == prim[0]) {
        con_ves.classList.toggle("container_ves_off");
        con_ves.classList.toggle("container_ves_on");
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
    };
    if (foundValue == prim[1]) {
        con_dan.classList.toggle("container_Dann_on");
        con_dan.classList.toggle("container_Dann_off");
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
    };
    if (foundValue == prim[2]) {
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
    };
    if (foundValue == prim[3]) {
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
    };
    if (foundValue == prim[4]) {
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
    };
};

vr.onclick = function() {
    f();
    if (foundValue == 0) {
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");   
    };
    if (foundValue == prim[0]) {
        con_ves.classList.toggle("container_ves_off");
        con_ves.classList.toggle("container_ves_on");
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");
    };
    if (foundValue == prim[1]) {
        con_dan.classList.toggle("container_Dann_on");
        con_dan.classList.toggle("container_Dann_off");
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");
    };
    if (foundValue == prim[2]) {
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");
    };
    if (foundValue == prim[3]) {
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");
    };
    if (foundValue == prim[4]) {
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");
    };
};

temp.onclick = function() {
    f();
    if (foundValue == 0) {
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
    };
    if (foundValue == prim[0]) {
        con_ves.classList.toggle("container_ves_off");
        con_ves.classList.toggle("container_ves_on");
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
    };
    if (foundValue == prim[1]) {
        con_dan.classList.toggle("container_Dann_on");
        con_dan.classList.toggle("container_Dann_off");
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
    };
    if (foundValue == prim[2]) {
        con_ras.classList.toggle("container_Rass_on");
        con_ras.classList.toggle("container_Rass_off");
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
    };
    if (foundValue == prim[3]) {
        con_vr.classList.toggle("container_Vr_on");
        con_vr.classList.toggle("container_Vr_off");
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
    };
    if (foundValue == prim[4]) {
        con_temp.classList.toggle("container_Temp_on");
        con_temp.classList.toggle("container_Temp_off");
    };
};

mill.onclick = function() {
    x = "mill";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

gramm.onclick = function() {
    x = "gramm";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

kilo.onclick = function() {
    x = "kilo";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

cent.onclick = function() {
    x = "cent";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

tonn.onclick = function() {
    x = "tonn";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

bit.onclick = function() {
    x = "bit";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

bait.onclick = function() {
    x = "bait";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

kiloba.onclick = function() {
    x = "kiloba";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

mega.onclick = function() {
    x = "mega";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

giga.onclick = function() {
    x = "giga";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

tera.onclick = function() {
    x = "tera";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

peta.onclick = function() {
    x = "peta";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

millme.onclick = function() {
    x = "millme";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

sant.onclick = function() {
    x = "sant";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

deci.onclick = function() {
    x = "deci";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

met.onclick = function() {
    x = "met";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

kilome.onclick = function() {
    x = "kilome";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

megame.onclick = function() {
    x = "megame";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

millsec.onclick = function() {
    x = "millsec";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

sec.onclick = function() {
    x = "sec";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

min.onclick = function() {
    x = "min";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

chas.onclick = function() {
    x = "chas";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

sut.onclick = function() {
    x = "sut";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

ned.onclick = function() {
    x = "ned";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

god.onclick = function() {
    x = "god";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

cels.onclick = function() {
    x = "cels";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

far.onclick = function() {
    x = "far";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

kelv.onclick = function() {
    x = "kelv";
    if (ri == 0) {
        ri = 1;
        Rassch.classList.toggle("Rassch_on");
        Rassch.classList.toggle("Rassch_off");
    };
};

Rassch.onclick = function() {
    switch (x) {
        case "mill":
            try {
                a = inputa.value;
                b = inputa.value / 1000;
                t = inputa.value / 1000 / 1000;
                d = inputa.value / 1000 / 1000 / 100;
                j = inputa.value / 1000 / 1000 / 1000;
                prco_ve(a, b, t, d, j);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "gramm":
            try {
                a = inputa.value * 1000;
                b = inputa.value;
                t = inputa.value / 1000;
                d = inputa.value / 1000 / 100;
                j = inputa.value / 1000 / 1000;
                prco_ve(a, b, t, d, j);
            } catch (error) {
                console.log(error);
            };
            break;    
        
        case "kilo":
            try {
                a = inputa.value * 1000 * 1000;
                b = inputa.value * 1000;
                t = inputa.value;
                d = inputa.value / 100;
                j = inputa.value / 1000;
                prco_ve(a, b, t, d, j);
            } catch (error) {
                console.log(error);
            };
            break;     

        case "cent":
            try {
                a = inputa.value * 100 * 1000 * 1000;
                b = inputa.value * 100 * 1000;
                t = inputa.value * 100;
                d = inputa.value;
                j = inputa.value / 10;
                prco_ve(a, b, t, d, j);
            } catch (error) {
                console.log(error);
            };
            break;

        case "tonn":
            try {
                a = inputa.value * 1000 * 1000 * 1000;
                b = inputa.value * 1000 * 1000;
                t = inputa.value * 1000;
                d = inputa.value * 10;
                j = inputa.value;
                prco_ve(a, b, t, d, j);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "bit":
            try {
                a = inputa.value;
                b = inputa.value / 8;
                t = inputa.value / 8 / 1024;
                d = inputa.value / 8 / 1024 / 1024;
                j = inputa.value / 8 / 1024 / 1024 / 1024;
                e = inputa.value / 8 / 1024 / 1024 / 1024 / 1024;
                g = inputa.value / 8 / 1024 / 1024 / 1024 / 1024 / 1024;
                prco_d(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;

        case "bait":
            try {
                a = inputa.value * 8;
                b = inputa.value;
                t = inputa.value / 1024;
                d = inputa.value / 1024 / 1024;
                j = inputa.value / 1024 / 1024 / 1024;
                e = inputa.value / 1024 / 1024 / 1024 / 1024;
                g = inputa.value / 1024 / 1024 / 1024 / 1024 / 1024;
                prco_d(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;

        case "kiloba":
            try {
                a = inputa.value * 8 * 1024;
                b = inputa.value * 1024;
                t = inputa.value;
                d = inputa.value / 1024;
                j = inputa.value / 1024 / 1024;
                e = inputa.value / 1024 / 1024 / 1024;
                g = inputa.value / 1024 / 1024 / 1024 / 1024;
                prco_d(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "mega":
            try {
                a = inputa.value * 8 * 1024 * 1024;
                b = inputa.value * 1024 * 1024;
                t = inputa.value * 1024;
                d = inputa.value;
                j = inputa.value / 1024;
                e = inputa.value / 1024 / 1024;
                g = inputa.value / 1024 / 1024 / 1024;
                prco_d(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "giga":
            try {
                a = inputa.value * 8 * 1024 * 1024 * 1024;
                b = inputa.value * 1024 * 1024 * 1024;
                t = inputa.value * 1024 * 1024;
                d = inputa.value * 1024;
                j = inputa.value;
                e = inputa.value / 1024;
                g = inputa.value / 1024 / 1024;
                prco_d(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "tera":
            try {
                a = inputa.value * 8 * 1024 * 1024 * 1024 * 1024;
                b = inputa.value * 1024 * 1024 * 1024 * 1024;
                t = inputa.value * 1024 * 1024 * 1024;
                d = inputa.value * 1024 * 1024;
                j = inputa.value * 1024;
                e = inputa.value;
                g = inputa.value / 1024;
                prco_d(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;

        case "peta":
            try {
                a = inputa.value * 8 * 1024 * 1024 * 1024 * 1024 * 1024;
                b = inputa.value * 1024 * 1024 * 1024 * 1024 * 1024;
                t = inputa.value * 1024 * 1024 * 1024 * 1024;
                d = inputa.value * 1024 * 1024 * 1024;
                j = inputa.value * 1024 * 1024;
                e = inputa.value * 1024;
                g = inputa.value;
                prco_d(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
        
        case "millme":
            try {
                a = inputa.value;
                b = inputa.value / 10;
                t = inputa.value / 10 / 10;
                d = inputa.value / 10 / 100;
                j = inputa.value / 10 / 100 / 1000;
                e = inputa.value / 10 / 100 / 1000 / 1000;
                prco_r(a, b, t, d, j, e);
            } catch (error) {
                console.log(error);
            };
            break;    
        
        case "sant":
            try {
                a = inputa.value * 10;
                b = inputa.value;
                t = inputa.value / 10;
                d = inputa.value / 100;
                j = inputa.value / 100 / 1000;
                e = inputa.value / 100 / 1000 / 1000;
                prco_r(a, b, t, d, j, e);
            } catch (error) {
                console.log(error);
            };
            break;

        case "deci":
            try {
                a = inputa.value * 10 * 10;
                b = inputa.value * 10;
                t = inputa.value;
                d = inputa.value / 10;
                j = inputa.value / 10 / 1000;
                e = inputa.value / 10 / 1000 / 1000;
                prco_r(a, b, t, d, j, e);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "met":
            try {
                a = inputa.value * 100 * 10;
                b = inputa.value * 100;
                t = inputa.value * 10;
                d = inputa.value;
                j = inputa.value / 1000;
                e = inputa.value / 1000 / 1000;
                prco_r(a, b, t, d, j, e);
            } catch (error) {
                console.log(error);
            };
            break;    

        case "kilome":
            try {
                a = inputa.value * 1000 * 10 * 10 * 10;
                b = inputa.value * 1000 * 10 * 10;
                t = inputa.value * 1000 * 10;
                d = inputa.value * 1000;
                j = inputa.value;
                e = inputa.value / 1000;
                prco_r(a, b, t, d, j, e);
            } catch (error) {
                console.log(error);
            };
            break;

        case "megame":
            try {
                a = inputa.value * 1000 * 1000 * 10 * 10 * 10;
                b = inputa.value * 1000 * 1000 * 10 * 10;
                t = inputa.value * 1000 * 1000 * 10;
                d = inputa.value * 1000 * 1000;
                j = inputa.value * 1000;
                e = inputa.value;
                prco_r(a, b, t, d, j, e);
            } catch (error) {
                console.log(error);
            };
            break;    
            
        case "millsec":
            try {
                a = inputa.value;
                b = inputa.value / 1000;
                t = inputa.value / 1000 / 60;
                d = inputa.value / 1000 / 60 / 60;
                j = inputa.value / 1000 / 60 / 60 / 24;
                e = inputa.value / 1000 / 60 / 60 / 24 / 7;
                g = inputa.value / 1000 / 60 / 60 / 24 / 365;
                prco_vr(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;

        case "sec":
            try {
                a = inputa.value * 1000;
                b = inputa.value;
                t = inputa.value / 60;
                d = inputa.value / 60 / 60;
                j = inputa.value / 60 / 60 / 24;
                e = inputa.value / 60 / 60 / 24 / 7;
                g = inputa.value / 60 / 60 / 24 / 365;
                prco_vr(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "min":
            try {
                a = inputa.value * 1000 * 60;
                b = inputa.value * 60;
                t = inputa.value;
                d = inputa.value / 60;
                j = inputa.value / 60 / 24;
                e = inputa.value / 60 / 24 / 7;
                g = inputa.value / 60 / 24 / 365;
                prco_vr(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "chas":
            try {
                a = inputa.value * 1000 * 60 * 60;
                b = inputa.value * 60 * 60;
                t = inputa.value * 60;
                d = inputa.value;
                j = inputa.value / 24;
                e = inputa.value / 24 / 7;
                g = inputa.value / 24 / 365;
                prco_vr(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "sut":
            try {
                a = inputa.value * 1000 * 60 * 60 * 24;
                b = inputa.value * 60 * 60 * 24;
                t = inputa.value * 60 * 24;
                d = inputa.value * 24;
                j = inputa.value;
                e = inputa.value / 7;
                g = inputa.value / 365;
                prco_vr(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "ned":
            try {
                a = inputa.value * 1000 * 60 * 60 * 24 * 7;
                b = inputa.value * 60 * 60 * 24 * 7;
                t = inputa.value * 60 * 24 * 7;
                d = inputa.value * 24 * 7;
                j = inputa.value * 7;
                e = inputa.value;
                g = inputa.value / 52;
                prco_vr(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "god":
            try {
                a = inputa.value * 1000 * 60 * 60 * 24 * 365;
                b = inputa.value * 60 * 60 * 24 * 365;
                t = inputa.value * 60 * 24 * 365;
                d = inputa.value * 365 * 24;
                j = inputa.value * 365;
                e = inputa.value * 52;
                g = inputa.value;
                prco_vr(a, b, t, d, j, e, g);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "cels":
            try {
                a = inputa.value;
                b = (inputa.value * 9/5) + 32;
                t = (inputa.value*1) + 273.15;
                prco_t(a, b, t);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "far":
            try {
                a = 5/9 * (inputa.value - 32);
                b = inputa.value;
                t = (inputa.value - 32) * 5/9 + 273.15;
                prco_t(a, b, t);
            } catch (error) {
                console.log(error);
            };
            break;
            
        case "kelv":
            try {
                a = inputa.value - 273.15;
                b = (inputa.value - 273.15) * 5/9 + 32;
                t = inputa.value
                prco_t(a, b, t);
            } catch (error) {
                console.log(error);
            };

        default:
            break;
    };
};

