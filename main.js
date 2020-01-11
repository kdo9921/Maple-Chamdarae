isCurrentIsHome = true;
function HomeToAbout() {
    if(!isCurrentIsHome) {
        return 0;
    }
    animateCSS('#home', 'bounceOutLeft', function() {
        document.getElementById("home").style.display ='none';
        document.getElementById("about").style.display ='inline-block';
        animateCSS('#about', 'bounceInRight');
    });
    isCurrentIsHome = false;
}
function AboutToHome() {
    if(isCurrentIsHome) {
        return 0;
    }
    animateCSS('#about', 'bounceOutRight', function() {
        document.getElementById("about").style.display ='none';
        document.getElementById("home").style.display ='inline-block';
        animateCSS('#home', 'bounceInLeft');
    });
    isCurrentIsHome = true;
}