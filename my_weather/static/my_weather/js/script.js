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
 $(document).ready(function(){
     $('#update_source input[type="checkbox"]').click(function (event) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url : "update_source/",
            type : "POST",
            data : { 'csrfmiddlewaretoken': csrftoken,
                    pk: $(this).data('source-id') },

            success : function() {
//                $('#is_update').val('');
//                console.log(json);
                console.log("success");
            },
        });
    });
});
