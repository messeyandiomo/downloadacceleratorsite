    /* click on button which gives access to forums */
    $('#forumModal').click(
        function(){
          $('#welcome').modal('toggle');
          window.open("{% url 'downloadaccelerator:forums' %}","_self");
        }
    );