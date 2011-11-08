jQuery(document).ready(function($) {
    
    $("#feedback_action").click( function() {
        $("#feedback_slider, #feedback_openclose").toggleClass("open","fast" );
        $("#feedback_opener").toggle();
	    return false;
    });

    $("#feedback_form").submit(function(){
        $.post($("#feedback_form").attr("action"),
            $(this).serialize());
        $("#feedback_form textarea").attr("value","");
        $("#feedback_action").click();
        return false;
    }); 

    $("#closeicon").click(function(){
        $("#feedback_action").click();
    });
});
