// function onClickMenu(){
//     document.getElementById('menu-bar').classList.toggle('change');
//     document.getElementById('nav').classList.toggle('change-btn');
    
// }

$(window).scroll(function(){

    $('div').toggleClass('scrolled', $(this).scrollTop() > 880);
});
