$(function() {
    /**
     * management of password button
     */
    $('.fa-eye-slash').click(
      function () {
        var newType = $(this).siblings('input').attr('type') === 'password' ? 'text' : 'password';
        $(this).siblings('input').attr('type', newType);
        $(this).toggleClass('fa-eye-slash').toggleClass('fa-eye');
      }
    );
    

    /**
     * management of name submitting button
     */
    function userExist(username) {
      var ret = false;
      $.ajax({
        async: false,
        type: 'GET',
        url: "{% url 'user' username %}",
        success: function (data) {
          ret = data;
        }
      });
      return ret;
    }
    
    $('#btn-createAccount').click(
      function () {
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
        }
        if($('input[placeholder = "Create password"]').val() != $('input[placeholder = "Repeat password"]').val()){
          $('input[placeholder = "Create password"]').addClass('border-danger');
          $('input[placeholder = "Repeat password"]').addClass('border-danger');
          $('input[placeholder = "Repeat password"]').attr('title', 'This password is not equal to the previous ! Please, fix this').tooltip({placement: 'right'}).tooltip('show');
        }
        else{
          if ($('input[placeholder = "Create password"]').hasClass('border-danger')) {
            $('input[placeholder = "Create password"]').removeClass('border-danger');
          }
          if ($('input[placeholder = "Repeat password"]').hasClass('border-danger')) {
            $('input[placeholder = "Repeat password"]').removeClass('border-danger');
            $('input[placeholder = "Repeat password"]').tooltip('disable');
          }
        }
      }
    );
    
    
});