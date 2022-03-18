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
    
    $('#btn-createAccount').click(
      function () {
        var err = false;
        if(($('#name').val().length === 0) | (!(/^[a-zA-Z][a-zA-Z0-9_-]*$/.test($('#name').val())))){
          $('#name').css('border-color', 'red');
          $('#name').tooltip({placement: 'right'}).tooltip('show');
          err = true;
        }
        if(($('#email').val().length === 0) |(!(/^[a-zA-Z](?:[a-zA-Z0-9_.-])*@[a-zA-Z]+\.[a-z]{2,5}/.test($('#email').val())))){
          $('#email').addClass('border-danger');
          $('#email').tooltip({placement: 'right'}).tooltip('show');
          err = true;
        }
        else{
          if ($('#email').hasClass('border-danger')) {
            $('#email').removeClass('border-danger');
            $('#email').tooltip('disable');
          }
        }
        if($('input[placeholder = "Create password"]').val() != $('input[placeholder = "Repeat password"]').val()){
          $('input[placeholder = "Create password"]').css('border-color', 'red');
          $('input[placeholder = "Repeat password"]').css('border-color', 'red');
          $('input[placeholder = "Repeat password"]').attr('title', 'This password is not equal to the previous ! Please, fix this').tooltip({placement: 'right'}).tooltip('show');
          err = true;
        }
        if(err)
          return false;
      }
    );
    
    
});