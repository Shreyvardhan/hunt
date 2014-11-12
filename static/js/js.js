$(document).ready(function(){

	member_count = $('#number').attr('value');
	
	$("input[type='button'].add-member").click(function(){

		$("#member-" + parseInt(parseInt(member_count) + 1)).removeClass('hidden');
		member_count++;

		if (member_count == 4) {

			$(this).hide();
			$("#save-member-container").removeClass("grid-50");
			$("#save-member-container").addClass("grid-100");

		}
		
	});

});