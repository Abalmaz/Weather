 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function updateSource(){
  $('#update_source input[type="checkbox"]').click(function (event) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url : "update_source/",
            type : "POST",
            data : { 'csrfmiddlewaretoken': csrftoken,
                    pk: $(this).data('source-id') },

            success : function() {
                console.log("success");
            },
        });
    });
}

function runScript(){
    $('#run_script input[type="button"]').click(function (event) {
    var csrftoken = getCookie('csrftoken');
        $.ajax({
            url : "update_weather/",
            type : "POST",
            data : {'csrfmiddlewaretoken': csrftoken,
                    pk: $(this).data('source-id') },
            success : function() {
                console.log("success");
            },
        });
    });
}

 $(document).ready(function(){
    $('#loading').hide();
    $("#loading").bind("ajaxSend", function(){
        $(this).show(); // показываем элемент
        console.log("show")
    }).bind("ajaxComplete", function(){
   $(this).hide(); // скрываем элемент
});
    updateSource();
    runScript();
});
