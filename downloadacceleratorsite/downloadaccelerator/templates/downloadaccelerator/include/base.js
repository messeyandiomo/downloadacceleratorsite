

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
    if ('{{ username }}' != '') {
      if (logout('{{ username }}')) {
        $(this).prop('disabled', true);
        window.open($(location).attr('href').split('?')[0], "_self");
      }
    }
  }
);

$('#idbuttonuser').hover(
  function () {
    if ($(this).html().length != 0) {
      $(this).html("SignOut");
    }
  },
  function () {
    $(this).html('{{ username }}');
  }
);
    
function logout(name) {
  var ret = false;
  $.ajax({
    async: false,
    type: 'GET',
    url: "{% url 'downloadaccelerator:logoutuser' %}",
    data: {"username": name},
    success: function (response) {
      if (response["success"]){
        ret = true;
      }
    }
  });
  return ret;
}
