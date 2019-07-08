$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				t1 : $('#email').val(),
				t2 : $('#pwd').val(),
                                t3 : $('#comment').val()
			},
			type : 'POST',
			url : '/sendmail'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$("#btn1").text('sent').button("refresh");
alert("Mail sent succesfully");  
				$('#successAlert').text(data.text1).show();
				$('#errorAlert').hide();
               


			}

		});

		event.preventDefault();

	});

});