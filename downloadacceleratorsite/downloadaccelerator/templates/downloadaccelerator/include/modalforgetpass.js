
  
      /* Reinitialize password on forgotten Password modal */
      $('#forgetPassButton').click(
        function(){
  
          if(($('#forgetPassEmail').val().length === 0) |(!(/^[a-zA-Z](?:[a-zA-Z0-9_.-])*@[a-zA-Z]+\.[a-z]{2,5}/.test($('#forgetPassEmail').val())))){
            if(!$('#forgetPassEmail').hasClass('border-danger'))
              $('#forgetPassEmail').addClass('border-danger');
            $('#forgetPassEmail').tooltip({placement: 'right'}).tooltip('show');
          }
          else{
            filledInput($('#forgetPassEmail'), $('#forgetPassNameDanger'))
            $('#forgetPassEmail').tooltip('disable');
            if(checkUserMail($('#forgetName').val(), $('#forgetPassEmail').val())){
              $(this).closest('.modal').modal('toggle');
              passwordReset($('#forgetPassForm'));
              $('#loadingpasswordreset').modal('show');
            }
            else {
              var warn = 'This mail does not belongs to ' + $('#forgetName').val();
              dangerInput($('#forgetPassEmail'), $('#forgetPassNameDanger'), $('#forgetPassNameDanger small'), warn);
            }
          }
        }
      );
  
      /* check if an email belong to user */
      function checkUserMail(username, usermail){
        
        var ret = false;
        $.ajax({
          async: false,
          type: 'GET',
          url: "{% url 'Discussion_forum:checkUserMail' %}",
          data: {"username": username, "email": usermail},
          success: function (response) {
            if (response["valid"]){
              ret = true;
            }
          }
        });
  
        return ret;
      }
  
      function passwordReset(forgetPassForm){
        var serializedData = forgetPassForm.serialize();
        $.ajax({
          type: 'POST',
          url: "{% url 'Discussion_forum:passwordreset' %}",
          data: serializedData,
          success: function(response){
            $('#loadingpasswordreset').modal('hide');
            window.open("/password_reset/done/", "_self");
          }
        });
      }