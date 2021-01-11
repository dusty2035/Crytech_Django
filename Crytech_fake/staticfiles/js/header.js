//////////////       header       ////////////////

var  x = document.getElementById("header").style ;
var logo = document.getElementById("logo") ;
var logo_text = document.getElementById("logo_text").style ;
var nav = document.getElementById("nav") ;
var icon = document.getElementById("icon") ;
var status = 1 ;

var header = function (backgroundColor , height , animation , width , boxShadow) {
    x.backgroundColor = backgroundColor;
    x.height = height ;
    logo.style.animation = animation ;
    logo_text.width = width ;
    x.boxShadow = boxShadow;
} ;

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    
    if (status == 1) {
        if (window.innerWidth > 3000) {
            if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
                
                header("white" , "16rem" , "rotate 1s" , "0" , "0 0 4rem gray");
                
            } else {
    
                header("transparent" , "24rem" , "rotateback 1s" , "32rem" , "0 0 0rem gray");
              
                }

        } 
            
        else if (window.innerWidth > 1025) {

                if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
                    
                    header("white" , "8rem" , "rotate 1s" , "0" , "0 0 4rem gray");
                    
                } else {
        
                    header("transparent" , "14rem" , "rotateback 1s" , "16rem" , "0 0 0rem gray");
                  
                }
        } 
            
        else if (window.innerWidth < 361) {
                if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                    header("white" , "5rem" , "rotate 1s" , "0" , "0 0 4rem gray");
                    
                } else {
        
                    header("transparent" , "8rem" , "rotateback 1s" , "16rem" , "0 0 0rem gray");
                }
        }
            
        else {
                if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                    header("white" , "6rem" , "rotate 1s" , "0" , "0 0 4rem gray");
                    
                    
                    
                } else {
                    header("transparent" , "10rem" , "rotateback 1s" , "0" , "0 0 0rem gray");
                }
        }
    }   
};  