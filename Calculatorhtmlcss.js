function getHistory(){
    return document.getElementById("history-value").innerText;
}
function printHistory(num){
    document.getElementById("history-valur").innerText=num;
}
function getOutput(){
    return document.getElementById("output-value").innterText;
}
function printOutput(num){
    if(num==""){
        document.getElementById("output-value").innterText=num;
    }
    else{
        document.getElementById("output-value").innerText=getFormattedNumber(num);
    }
}
function getFormattedNumber(num){
    if(num==""){
        return "";
    }
    var n = Number(num);
    var value = n.toLocaleString("en");
    return value;
}
function reverseNumberFormat(num){
    return Number(num.replace(/,/g,''));
}
var operator = document.getElementsByClassName("operator");
for(var i =0;i<operator.length;i++){
    operator[i].addEventListener('click'),function(){
        if(this.id=="clear"){
            printHistory("");
            printOutput("");
        }
    }
}