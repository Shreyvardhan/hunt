$(function() {

	$("#primaryNav a").click(function() {

		var hashLink = "#" + $(this).attr("href");

		$("html, body").animate({
			scrollTop: $(hashLink).offset().top
		}, 500);

		history.pushState({ clickEvent: "pseudo-link" }, "link", $(this).attr("href"));

		return false;

	});

});

$(window).scroll(function() {

	var scrollTop = $(window).scrollTop();

//	if(scrollTop > $("#x").offset().top && scrollTop < $("#schedule").offset().top) {
//		history.pushState({ clickEvent: "pseudo-link" }, "link", "x");
//	}

});
