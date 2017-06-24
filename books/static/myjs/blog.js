$(document).ready(function(){
	$("#create_new_blog_button").click(function(){
		$.ajax({
			url: '/blog/create',
			type: 'get',
			dataType: 'json',
			success: function(data){
				$("#blog_form_div").html(data.html_form);
			}
		});
	});
});