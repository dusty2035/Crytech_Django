///////////////////      slide-show-shop(game-info)        ////////////////////

var slides = document.getElementsByClassName("container-mySlides");
var thumbnails = document.getElementsByClassName("container-demo");
var i ;

function reset_thumbnail () {
    for (i = 0 ; i < 6 ; i++) {
        thumbnails[i].style.opacity = "0.4" ;
    }
}

function currentSlide (n) {

    reset_thumbnail () ;

    for (i=0 ; i < slides.length ; i++) {
        slides[i].style.display = "none" ;
    } ;

    slides[n-1].style.display = "block" ;
    thumbnails[n-1].style.opacity = "1" ;
} ;

///////////////  switching description - System requirements  ////////////////

var des_btn = document.getElementById("description") ;
var sys_btn = document.getElementById("system_requirements") ;
var des_box = document.getElementById("des_box") ;
var sys_box = document.getElementById("sys_box") ;

function des_btn_f() {

    des_btn.style.borderBottom = ".2rem solid blue" ;
    sys_btn.style.borderBottom = "none" ;
    des_box.style.display = "block" ;
    sys_box.style.display = "none" ;

} ;


function sys_btn_f() {

    sys_btn.style.borderBottom = ".2rem solid blue" ;
    des_btn.style.borderBottom = "none" ;
    des_box.style.display = "none" ;
    sys_box.style.display = "block" ;
    
} ;



//////////////   login_signup   ///////////////

var signup_btn = document.getElementById("signup") ;
var login_btn = document.getElementById("login") ;
var signup_form = document.getElementById("signup_form") ;
var login_form = document.getElementById("login_form") ;
var signup_box = document.getElementById("signup_box") ;
var login_box = document.getElementById("login_box") ;


function signup() {

    signup_form.style.height = "auto" ;
    signup_box.style.width = "80%" ;
    login_form.style.height = "0" ;
    login_box.style.width = "0" ;
    signup_btn.style.backgroundColor = "transparent" ;
    login_btn.style.backgroundColor = "rgba(242,242,242,0.9)" ;
} ;

function login() {

    signup_form.style.height = "0" ;
    signup_box.style.width = "0" ;
    login_form.style.height = "auto" ;
    login_box.style.height = "auto"
    login_box.style.width = "80%" ;
    signup_btn.style.backgroundColor = "rgba(242,242,242,0.9)" ;
    login_btn.style.backgroundColor = "transparent" ;
} ;
