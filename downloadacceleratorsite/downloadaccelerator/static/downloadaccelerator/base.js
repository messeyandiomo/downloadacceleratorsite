$(function() {

  var username = "";

    $('.btn-download').click(
      function() {
        window.open("https://addons.mozilla.org/fr/firefox/addon/download_accelerator/");
      }
    );

    
    $('#forumsList').hover(
      function(){
        $('.dropdown-menu').slideDown('slow');
      },
      function () {
        setTimeout(function () {
          if (!$('.dropdown-menu').is(':hover')) {
            $('.dropdown-menu').slideUp('slow');
          }
        }, 1000);
      }
    );

    $('.dropdown-menu').mouseleave(
      function(){
        $(this).slideUp('slow');
      }
    );

    $('.navbar-toggler').click(
      function () {
        if($('.navbar-toggler > span').hasClass('fa-angle-down')){
          $('.navbar-toggler > span').removeClass('fa-angle-down');
          $('.navbar-toggler > span').addClass('fa-angle-up');
        } else {
          $('.navbar-toggler > span').removeClass('fa-angle-up');
          $('.navbar-toggler > span').addClass('fa-angle-down');
        }
      }
    );

    $('#idbuttonuser').click(
      function () {
        $(this).html('');
        $(this).addClass('disabled text-white');
      }
    );

    $('#idbuttonuser').hover(
      function () {
        username = $(this).html();
        if (username.length != 0) {
          $(this).html("SignOut");
        }
      },
      function () {
        $(this).html(username);
      }
    );
    
    
    
    
});