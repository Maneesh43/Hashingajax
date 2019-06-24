$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				text1 : $('#textInput').val(),
				hash1 : $('#selectInput').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.text1).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});