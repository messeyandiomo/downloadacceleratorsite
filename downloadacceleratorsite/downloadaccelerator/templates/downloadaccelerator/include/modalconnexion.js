

/* click on connexion button */
    $('#connexionButton').click(
        function(){
          
          var emptyName = ($('#connexionName').val().length === 0) ? true : false;
          var emptyPassword = ($('#connexionPassword').val().length === 0) ? true : false;
          var warn = 'This field must not be empty';
          
          if(!emptyName && !emptyPassword){
            if(userAuth($('#connexionForm'))){
              $(this).parents('.modal').modal('toggle');
              $("#welcomemessage").html($('#connexionName').val() + " welcome to forums");
              $('#welcome').modal('show');
            }
            else{
              $('#connexionName').tooltip('enable').tooltip('show');
              $('#connexionPassword').val('');
              $('#connexionPassword').focus();
              filledInput($('#connexionPassword'), $('#passwordDanger'));
            }
          }
          else if(emptyName && emptyPassword){
            dangerInput($('#connexionName'), $('#nameDanger'), $('#nameDanger small'), warn);
            dangerInput($('#connexionPassword'), $('#passwordDanger'), $('#passwordDanger small'), warn);
            $('#connexionName').tooltip('disable');
          }
          else if(emptyName && !emptyPassword){
            dangerInput($('#connexionName'), $('#nameDanger'), $('#nameDanger small'), warn);
            filledInput($('#connexionPassword'), $('#passwordDanger'));
            $('#connexionName').tooltip('disable');
          }
          else if(!emptyName && emptyPassword){
            dangerInput($('#connexionPassword'), $('#passwordDanger'), $('#passwordDanger small'), warn);
            filledInput($('#connexionName'), $('#nameDanger'));
            $('#connexionName').tooltip('disable');
          }
        }
    );


    /* click on forgot password link */
    $('#forgotPassword').click(
        function(e){
          var emptyName = ($('#connexionName').val().length === 0) ? true : false;
          if(emptyName){
            dangerInput($('#connexionName'), $('#nameDanger'), $('#nameDanger small'), 'This field must not be empty');
          }
          else {
            if(userExist($('#connexionName').val())){
              filledInput($('#connexionName'), $('#nameDanger'));
              $('#modal-connexion').modal('hide');
              $('#modal-forget-password').modal('show');
              $('#forgetName').val($('#connexionName').val());
            }
            else{
              dangerInput($('#connexionName'), $('#nameDanger'), $('#nameDanger small'), 'This user does not exists');
            }
          }
        }
      );
    

    function userAuth(connexionForm){
        var ret = false;
        var serializedData = connexionForm.serialize();
        $.ajax({
          async: false,
          type: 'POST',
          url: "{% url 'downloadaccelerator:userauth' %}",
          data: serializedData,
          success: function(response){
            if(response["auth"]){
              ret = true;
            }
          }
        });
        return ret;
    }
