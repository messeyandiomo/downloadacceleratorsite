$(function() {
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
    
});