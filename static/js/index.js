
var countDownDate = new Date("Nov 19, 2021 11:59:59").getTime();

var myfunc = setInterval(function() {
var now = new Date().getTime();
var timeleft = countDownDate - now;
    
var days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
var hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
var seconds = Math.floor((timeleft % (1000 * 60)) / 1000);


document.getElementById("days").innerHTML = days + "d "
document.getElementById("hours").innerHTML = hours + "h " 
document.getElementById("mins").innerHTML = minutes + "m " 
document.getElementById("secs").innerHTML = seconds + "s"


if (timeleft < 0) {
    clearInterval(myfunc);
    document.getElementById("days").innerHTML = ""
    document.getElementById("hours").innerHTML = "" 
    document.getElementById("mins").innerHTML = ""
    document.getElementById("secs").innerHTML = ""
    document.getElementById("end").innerHTML = "TIME UP!!";
}
}, 1000)


/********************** Adding Audio on Click *************************/

const dot = document.querySelectorAll('.evm span');
const audioElementTag = document.querySelector('#audio');
const audioClickButton = document.querySelectorAll('.evm form button');
const audio = audioElementTag.innerText;
const music = new Audio(audio);

function findIndex(btn){
    index = 0;
    for(b of audioClickButton){
        if(b===btn){
            return index;
        }
        else{
            index = index + 1;
        }
    }
}

audioClickButton.forEach(function(btn){
    btn.addEventListener('click',function(){
        music.play();
        btn.setAttribute("style","pointer-events:none;") ;
        index = findIndex(btn);
        dot[index].style.color = "green";
    });
});