/**
 * Created by lulizhou on 2015/9/5.
 */
/*
var config = {
    after: '0s',
    enter: 'bottom',
    move: '24px',
    over: '0.66s',
    easing: 'ease-in-out',
    viewportFactor: 0.33,
    reset: true,
    init: true
};
 window.sr = new scrollReveal(config);*/
new WOW().init();
$(function () {
    $(".navbar-nav>li").addClass("animated");
    addremove(".navbar-nav>li","swing")
    addremove("#navbar-brand","swing")

})
function addremove(selector,animate){
    $(selector).hover(function(){
        $(this).addClass(animate)
    },function(){
        $(this).removeClass(animate)
    })
    }