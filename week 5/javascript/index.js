let age = 0
let msg = ""

document.getElementById("confirm_btn").onclick=function(){
console.log("Button clicked !")
age = document.getElementById("age").innerHTML.valueOf()
if(age <= 18){
    msg = "You are not allowed"
    document.getElementById("get_in").innerHTML.msg
}else{
    msg = "Welcome to the club"
    document.getElementById("get_in").innerHTML.msg

    }
};




