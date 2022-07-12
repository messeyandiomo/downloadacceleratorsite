
    
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
        url: "{% url 'Discussion_forum:user' %}",
        data: {"username": username},
        success: function (response) {
          if (!response["valid"]) {
            ret = true;
          }
        }
      });
      return ret;
    }

    function dangerInput(objectInput, objectNotice, objectWarning, warning){
      if(!objectInput.hasClass('border-danger')){
        objectInput.addClass('border-danger');
      }
      if(!objectNotice.hasClass('text-danger')){
        objectNotice.removeClass('text-white');
        objectNotice.addClass('text-danger');
      }
      objectWarning.html(warning);
    }

    function filledInput(objectInput, objectNotice){
      if(objectInput.hasClass('border-danger')){
        objectInput.removeClass('border-danger');
      }
      if(objectNotice.hasClass('text-danger')){
        objectNotice.removeClass('text-danger');
        objectNotice.addClass('text-white');
      }
    }
