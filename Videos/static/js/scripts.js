$(document).ready(function(){
	// set like
	$("#like").click(function (){
        var serializedData = $("#culc").serialize();
        $.ajax({
            url: "/culc",
            data: serializedData,
            type: 'post',
            success: function (response){
                $('#amount').text(response.amount);
            }
        })
    });
    // set dislike
	$("#dislike").click(function (){
        var serializedData = $(".dislike").serialize();
        $.ajax({
            url: "/culc",
            data: serializedData,
            type: 'post',
            success: function (response){
                $('#amount').text(response.amount);
            }
        })
    });
});

