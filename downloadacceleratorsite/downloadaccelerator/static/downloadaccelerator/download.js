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
        if(($('#name').val().length === 0) | (!(/^[a-zA-Z][a-zA-Z0-9_-]*$/.test($('#name').val())))){
          $('#name').css('border-color', 'red');
        }
        else {
          $('#name').css('border-color', 'blue');
        }
        if($('input[placeholder = "Create password"]').val() != $('input[placeholder = "Repeat password"]').val()){
          $('input[placeholder = "Create password"]').css('border-color', 'red');
          $('input[placeholder = "Repeat password"]').css('border-color', 'red');
        }
      }
    );
    
    
});