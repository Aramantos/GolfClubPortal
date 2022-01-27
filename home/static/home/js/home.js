const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
const dates = ["0", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", 
                "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", 
                "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]
const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];

var date = new Date();
var day = weekday[date.getDay()];
var num_date = dates[date.getDate()];
var month = months[date.getMonth()]
var year = date.getFullYear();
var time = date.toLocaleTimeString();

document.getElementById('date').innerHTML = day + " - " + num_date + " - " + month + " - " + year;

$(document).ready(function () {
    $('.home-list-item').on("hover", function() {
        $('.home-list-item-a').css("color", "white");
    });
});