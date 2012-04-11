jQuery(document).ready(function($) {
    
    $("#feedback_action").click( function() {
        $("#feedback_slider, #feedback_openclose").toggleClass("open");
	    return false;
    });

    $("#feedback_form").submit(function(){
        var submit = $('#feedback_form input[type="submit"]');
        var old_val = submit.val();
        submit.val(submit.attr('sending_value'));
        $.post($("#feedback_form").attr("action"),
            $(this).serialize(), function(data){
                submit.after($('<div></div>').text(data.msg));
                submit.val(submit.attr('sent_value'));
        });
        setTimeout(function(){
            $("#feedback_form textarea").attr("value","");
            submit.val(old_val);
            $("#feedback_action").click();
        }, 2000);
        return false;
    }); 

    $("#closeicon").click(function(){
        $("#feedback_action").click();
    });
});
