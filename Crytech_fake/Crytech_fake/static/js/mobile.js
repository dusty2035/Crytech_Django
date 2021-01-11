///////////////       mobile menu       ///////////////

var logo_fun = function (f_dir , justify , nav_display  , nav_f_dir  , bor_rad ) {

    x.flexDirection = f_dir;
    x.justifyContent = justify ;
    nav.style.display = nav_display;
    nav.style.flexDirection = nav_f_dir;
    x.borderRadius = bor_rad;
}

document.querySelector('.header__logo-box-img').addEventListener('click' , function () {
    
    if(window.innerWidth < 1025) {
        
        if(status == 1) {
            header("white" , "100%" , "rotate 2s" , "0" , "0 0 0rem gray");
            logo_fun("column" , "left" , "flex" , "column" ,  "0" ) ;
            status = 2;
        }
        else{
            header("transparent" , "6rem" , "rotateback 2s" , "0" , "0 0 0rem gray");
            logo_fun("row" , "center" , "none" , "none" , "row" , "row" , "0");
            status = 1;
        }

    }else {
            header("transparent" , "6rem" , "rotateback 2s" , "0" , "0 0 0rem gray");
            logo_fun("row" , "space-between" , "flex"  , "row" ,  "0 0 4rem 4rem");
            status = 1;
        
    }

}) ;