$(document).ready(function(){

  $("#add-website").click(function(e){
    e.preventDefault();
    var order = $("#other_profiles li").length + 1;
    $("#other_profiles").append('\n '+
      '<li class="short" data-toggle="tooltip" data-placement="bottom" title="Comprueba los datos">' +
        '<label for="id_website_name_' + order + '">Nombre</label> ' +
        '<input id="id_website_name_' + order + '" maxlength="100" name="website_name_' + order + '" type="text" class="form-control"> ' +
        '<label for="id_website_url_' + order + '">URL</label> ' +
        '<input id="id_website_url_' + order + '" maxlength="100" name="website_url_' + order + '" type="text" class="form-control"> \n'+
      '</li>'
    );
    $('#num_websites').val(order);
  });


  $('#group-detail').submit(function(e){
    $(this).attr("action", $(this).find("select").val());//e.preventDefault();

  });

  $(".dropdown-menu li").click(function(e){
    var $t = $(this);
    $(".dropdown-menu li.active").removeClass("active");
    $t.addClass("active");

    if($t.data("group")=="all"){
      $("#community tbody tr").show();
    }else{
      $("#community tbody tr:not("+ $t.data("group") +")").hide();
      $("#community tbody tr."+ $t.data("group")).show();
    }
  });

  $("#cityList li").each(function(){
    var $t = $(this),
        len = $("#community tbody tr."+ $t.data("group")).length;
    console.log($t.data("group")+ ":"+len);
    $t.text($t.text()+" ("+len+")");
  });

  
  $('#myModal').modal({
    show:false
  });
  $("#community tbody tr").click(function(e){
    var $t = $(this);
    //debugger
    $(".modal-title").text($t.find(".first_name").text() + " " + $t.find(".last_name").text());
    $(".modal .status").text($t.find(".status").text());
    $(".modal .last_activity").text($t.find(".last_activity").text());
    $(".modal .email").text($t.find(".email").text());
    $(".modal .phone").text($t.find(".phone").text());
    $(".modal .secondary_emails").text($t.find(".secondary_emails").text());
    $(".modal .bio").text($t.find(".bio").text());
    $(".modal .role").text($t.find(".role").text());
    $(".modal .profiles").html($t.find(".profiles").html());
    $(".modal .photo").attr("src", $t.find(".img").data("src"));
    $(".modal .groups").text($t.find(".groups").text());
    $('#myModal').modal('show');
  });
  
});
