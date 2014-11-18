$(document).ready(function(){

  $("#add-website").click(function(e){
    e.preventDefault();
    var order = $("#other_profiles li").length + 1;
    $("#other_profiles").append('\n '+
      '<li class="short"> ' +
        '<label for="id_website_name_' + order + '">Nombre</label> ' +
        '<input id="id_website_name_' + order + '" maxlength="100" name="website_name_' + order + '" type="text" class="form-control"> ' +
        '<label for="id_website_url_' + order + '">URL</label> ' +
        '<input id="id_website_url_' + order + '" maxlength="100" name="website_url_' + order + '" type="text" class="form-control"> \n'+
      '</li>'
    );
    $('#num_websites').val(order);
  });

});