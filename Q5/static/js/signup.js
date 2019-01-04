$(function(){
	$('button').click(function(){
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '/signUpUser',
			data: $('form').serialize(),
			type: 'POST',
			dataType: 'json',
			success: function(response){
				console.log(response);
				var input_email_address = response.user;
				var inputPassword = response.pass;
				//<!-- https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById -->
				var confirm_message = document.getElementById('confirm_message');



				if (response.status == 'OK'){
				confirm_message.innerHTML = "Congratulations on registering for CSE6242, "+input_email_address+"! Redirecting you to the course homepage...";
				setTimeout(function(){document.location = "http://poloclub.gatech.edu/cse6242/"},3000); /*3000ms = 3s*/
				/*Reference https://www.w3schools.com/jsref/met_form_reset.asp*/
				document.getElementById("myForm").reset();

				}



				else{
				error_msg = input_email_address+", the password in invalid because it"
				if(response.pass.indexOf(1) > -1){
					error_msg += ', 1. Should be at least 8 characters in length';
				}
				if(response.pass.indexOf(2) > -1){
					error_msg += ', 2. Should have at least 1 uppercase character';
				}
				if(response.pass.indexOf(3) > -1){
					error_msg += ', 3. Should have at least 1 number';
				}
				confirm_message.innerHTML = error_msg;
				$('#inputPassword').val("");
			}

			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
