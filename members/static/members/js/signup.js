$(document).ready(function(){

  //$('[data-toggle="tooltip"]').tooltip()

  var email_fields = [
    "id_primary_email",
    "id_secondary_emails"
  ];

  var url_fields = [
      "id_linkedin",
      "id_twitter"
  ];

  $("#signup-form").submit(function(){
    var i = 0, j, $input, $inputs, name, emails, url, form;

    form = this;
    $(this).attr("valid","true");

    for(i = 0; i < email_fields.length; i++){
      $input = $("#"+email_fields[i]);
      emails = $input.val().split(",");

      for(j = 0; j < emails.length; j++){
        if(!is_email(emails[j])){
          $input.tooltip('show');
          $(this).attr("valid","false");
        }
      }
    }

    for(i = 0; i < url_fields.length; i++){
      $input = $("#"+url_fields[i]);
      url = $input.val();

      if(!is_url(url)){
        $input.tooltip('show');
        $(this).attr("valid","false");
      }
    }

    $("#other_profiles li").each(function(i,elem){
      $inputs = $(elem).find("input");
      name = $($inputs[0]).val();
      url = $($inputs[1]).val();

      if(name || url){
        if(name.length == 0 || url.length == 0){
          $(elem).tooltip('show');
          $(form).attr("valid","false");
          console.log("Direc. incompleta")
        }else if(!is_url(url)){
          $(elem).tooltip('show');
          $(form).attr("valid","false");
          console.log("Url inválida")
        }
      }
    })

    if($(this).attr("valid") == "false")
      return false;
    else
      return true;
  });
});


function is_url(url) {
  var reurl = /^(http[s]?:\/\/){1}(www\.){0,1}[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,5}[\.]{0,1}/;
  return reurl.test(url);
}

function is_email(email) {
  if ((/(.+)@(.+){2,}\.(.+){2,}/.test(email)) || email=="" || email==null) {
    return true;
  }
  return false;
}
