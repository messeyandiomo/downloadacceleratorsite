//import "common.js";

function createUser(username, email, password){
    var ret = false;
    $.ajax({
      async: false,
      type: 'GET',
      url: "{% url 'downloadaccelerator:createuser' %}",
      data: {"username": username, "email": email, "password": password},
      success: function (response) {
        if (response["register"]){
          ret = true;
        }
      }
    });
    return ret;
  }

  var percentage = 0;
  function checkProgressbar(n, m){
    if (n < 6) {
      percentage = 0;
      $("#progressbar").css("background", "#dd4b39");
    }
    else if (n < 8) {
      percentage = 20;
      $("#progressbar").css("background", "#9c27b0");
    }
    else if (n < 10) {
      percentage = 40;
      $("#progressbar").css("background", "#ff9800");
    }
    else {
      percentage = 60;
      $("#progressbar").css("background", "#4caf50");
    }
    // Check for the character-set constraints
    // and update percentage variable as needed.
         
    //Lowercase Words only
    if ((m.match(/[a-z]/) != null)) {
      percentage += 10;
    }
    //Uppercase Words only
    if ((m.match(/[A-Z]/) != null)) {
      percentage += 10;
    }
    //Digits only
    if ((m.match(/0|1|2|3|4|5|6|7|8|9/) != null)) {
      percentage += 10;
    }
    //Special characters
    if ((m.match(/\W/) != null) && (m.match(/\D/) != null)){
      percentage += 10;
    }
    // Update the width of the progress bar
    $("#progressbar").css("width", percentage + "%");
    /* print the password state on progress bar */
    if(percentage < 50){
      $('#progressbar').html('LOW');
    }
    else if(percentage < 70){
      $('#progressbar').html('NORMAL');
    }
    else if(percentage < 85){
      $('#progressbar').html('MEDIUM');
    }
    else if(percentage < 95){
      $('#progressbar').html('STRONG');
    }
    else{
      $('#progressbar').html('VERY STRONG');
    }
  }

  /* manage of keyup inside password input */
  $('input[placeholder = "Create password"]').keyup(
    function() {
      var m = $(this).val();
      var n = m.length;
      // Function for checking progress bar
      checkProgressbar(n, m);
    }
  );
  
  $('#btn-createAccount').click(
    function () {
      var nameClean = false;
      var emailClean = false;
      var passwordClean = false;

      if(($('#name').val().length === 0) | (!(/^[a-zA-Z][a-zA-Z0-9_-]*/.test($('#name').val())))){
        if(!$('#name').hasClass('border-danger'))
          $('#name').addClass('border-danger');
        $('#name').tooltip('dispose');
        $('#name').attr('title', 'This field must not be empty and should begin with alphabetic character').tooltip({placement: 'right'}).tooltip('show');
      }
      else if(userExist($('#name').val())){
        if(!$('#name').hasClass('border-danger'))
          $('#name').addClass('border-danger');
        $('#name').tooltip('dispose');
        $('#name').attr('title', 'A user with that name already exist. Suggest another name').tooltip({placement: 'right'}).tooltip('show');
      }
      else{
        if ($('#name').hasClass('border-danger')) {
          $('#name').removeClass('border-danger');
          $('#name').tooltip('disable');
        }
        nameClean = true;
      }
      if(($('#email').val().length === 0) |(!(/^[a-zA-Z](?:[a-zA-Z0-9_.-])*@[a-zA-Z]+\.[a-z]{2,5}/.test($('#email').val())))){
        if(!$('#email').hasClass('border-danger'))
          $('#email').addClass('border-danger');
        $('#email').tooltip({placement: 'right'}).tooltip('show');
      }
      else{
        if ($('#email').hasClass('border-danger'))
          $('#email').removeClass('border-danger');
        $('#email').tooltip('disable');
        emailClean = true;
      }
      if($('input[placeholder = "Create password"]').val() != $('input[placeholder = "Repeat password"]').val()){
        $('input[placeholder = "Create password"]').addClass('border-danger');
        $('input[placeholder = "Repeat password"]').addClass('border-danger');
        $('input[placeholder = "Repeat password"]').attr('title', 'This password is not equal to the previous! Please, fix this!').tooltip({placement: 'right'}).tooltip('show');
      }
      else if(percentage < 70){
        if (!$('input[placeholder = "Create password"]').hasClass('border-danger')) {
          $('input[placeholder = "Create password"]').addClass('border-danger');
        }
        $('input[placeholder = "Create password"]').attr('title', 'This password too weak. Please adjust it').tooltip({placement: 'right'}).tooltip('show');
      }
      else{
        if ($('input[placeholder = "Create password"]').hasClass('border-danger')) {
          $('input[placeholder = "Create password"]').removeClass('border-danger');
          $('input[placeholder = "Create password"]').tooltip('disable');
        }
        if ($('input[placeholder = "Repeat password"]').hasClass('border-danger')) {
          $('input[placeholder = "Repeat password"]').removeClass('border-danger');
          $('input[placeholder = "Repeat password"]').tooltip('disable');
        }
        passwordClean = true;
      }
      if(nameClean && emailClean && passwordClean){
        /* add user in the data base */
        createUser($('#name').val(), $('#email').val(), $('input[placeholder = "Create password"]').val());
      }
    }
  );

  $('input[placeholder = "Create password"]').change(
    function(){
        checkProgressbar($(this).val().length, $(this).val());
    }
);

/* initialisation of progress bar */
checkProgressbar($('input[placeholder = "Create password"]').val().length, $('input[placeholder = "Create password"]').val());

