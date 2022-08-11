

/* click on connexion button */
    $('#connexionButton').click(
        function(){
          
          var emptyName = ($('#connexionName').val().length === 0) ? true : false;
          var emptyPassword = ($('#connexionPassword').val().length === 0) ? true : false;
          var warn = 'This field must not be empty';
          
          if(!emptyName && !emptyPassword){
            userAuth($('#connexionForm'));
            $('body').css('cursor', 'wait');
            $(this).css('cursor', 'wait');
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
        var serializedData = connexionForm.serialize();
        $.ajax({
          type: 'POST',
          url: "{% url 'Discussion_forum:userauth' %}",
          data: serializedData,
          success: function(response){
            $('body').css('cursor', 'default');
            $('#connexionButton').css('cursor', 'pointer');
            if(response["auth"]){
              window.open("{% url 'Discussion_forum:forums' %}" + "?username=" + $('#connexionName').val(),"_self");
            }
            else{
              $('#connexionName').tooltip('enable').tooltip('show');
              $('#connexionPassword').val('');
              $('#connexionPassword').focus();
              filledInput($('#connexionPassword'), $('#passwordDanger'));
            }
          }
        });
    }
    
    
    
