jQuery(document).ready(function($) {
    
    $("#feedback_action").click( function() {
        if ($("#feedback_opener").is(":hidden")) {
            $("#feedback_slider, #feedback_openclose").toggleClass("open","fast" );
            $("#feedback_opener").show();
        } else {
            $("#feedback_slider, #feedback_openclose").toggleClass("open","fast");	
            $("#feedback_opener").hide();
	    return false;
        }
    });
    $("#feedback_form").submit(function(){
	$.post(FEEDBACK_POST_URL,$(this).serialize());
	$("#feedback_form textarea").attr("value","");
	$("#feedback_action").click();
	return false;
    }); 

    $("#closeicon").click(function(){
        $("#feedback_action").click();
    });
});
