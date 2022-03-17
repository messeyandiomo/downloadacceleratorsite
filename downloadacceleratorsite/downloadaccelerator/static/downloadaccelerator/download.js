$(function() {
    /**
     * management of password button
     */
    $('#togglePassword').click(
      () => {
        var newType = $('#password').attr('type') === 'password' ? 'text' : 'password';
        $('#password').attr('type', newType);
        $('#togglePassword').toggleClass('fa-eye-slash').toggleClass('fa-eye');
      }
    );

    $('#togglePassword2').click(
        () => {
          var newType = $('#password2').attr('type') === 'password' ? 'text' : 'password';
          $('#password2').attr('type', newType);
          $('#togglePassword2').toggleClass('fa-eye-slash').toggleClass('fa-eye');
        }
    );
    /**
     * management of name input text
     */
    
    $('#btn-createAccount').click(
      () => {
        if (($('#name').val() === "")|(!(/^[a-zA-Z][a-zA-Z0-9_-]*$/.test($('#name').val())))){
          $('#name').css('border-color', 'red');
          $('#name').tooltip();
        }
        else {
          $('#name').css('border-color', 'blue');
        }
        if(($('#email').val() === "")|(!(/[a-zA-Z][a-zA-Z0-9_-]*@[a-zA-Z]+\.[a-z]{2,5}/.test($('#email').val())))){
          $('#email').css('border-color', 'red');
          $('#email').tooltip();
        }
        if($('#password').val() === ""){
          $('#password').css('border-color', 'red');
          $('#password').tooltip();
        }
        if($('#password2').val() === ""){
          $('#password2').css('border-color', 'red');
          $('#password2').tooltip();
        }
        if($('#password').val() != $('#password2').val()){
          $('#password').css('border-color', 'red');
          $('#password2').css('border-color', 'red');
        }
      }
    );
    
});