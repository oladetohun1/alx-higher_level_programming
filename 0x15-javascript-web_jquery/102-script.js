$(document).ready(function () {
	$('#btn_translate').click(function () {
		$.get('https://www.fourtonfish.com/hellosalut/hello/' + $('#language_code').val() + '/', function (data) {
			 $('#hello').text(data.hello);
		});
	});
});