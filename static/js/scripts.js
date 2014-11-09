$(function() {

	$(".rsvp-link").click(function() {

		$("main").fadeOut();
		history.pushState({ clickEvent: "rsvp-link" }, "rsvp", "rsvp");

		$("#ajax").load("rsvp.html > section");
		$("#ajax").fadeIn();

		$(".closebtn").fadeIn();

		return false;

	});

	$(".request-link").click(function() {

		$("main").fadeOut();
		history.pushState({ clickEvent: "request-link" }, "request", "request");

		$("#ajax").load("request.html > section");
		$("#ajax").fadeIn();

		$(".closebtn").fadeIn();

		return false;

	});

	$(".closebtn").click(function() {

		$(this).fadeOut();
		$("#ajax").fadeOut();
		$("main").fadeIn();
		setTimeout(function() {
			$("#ajax").html("<div style='font-size: 250%; color: #ccc; text-align: center; margin-top: 100px'>Loading...</div>");
		}, 500);

		history.pushState({ clickEvent: "home" }, "home", "/");

	});

	$(".dayone").click(function() {
		$("#schedule table:first-of-type").show();
		$("#schedule table:last-of-type").hide();
		$(".toggle-days span").toggleClass("active");
	});

	$(".daytwo").click(function() {
		$("#schedule table:first-of-type").hide();
		$("#schedule table:last-of-type").show();
		$(".toggle-days span").toggleClass("active");
	});

});

/*var initialize = function() {
	
	var themis = new google.maps.LatLng(28.541167, 77.201633);

	var mapOptions = {
		zoom: 16,
		navigationControl: false,
		mapTypeControl: false,
		scaleControl: false,
		draggable: false,
		scrollwheel: false,
		disableDefaultUI: true,
		center: themis
	};

	var map = new google.maps.Map(document.getElementById('travel'), mapOptions);

	var marker = new google.maps.Marker({
		position: themis,
		map: map,
		title: "The Mother's International School"
	});

	var styles = [{
		stylers: [
			//{ hue: "#aaa" },
			{ saturation: -10 }
		]},{
		featureType: "road",
		elementType: "geometry",
		featureType: "road",
		elementType: "labels",
		stylers: [{
			visibility: "off"
		}]
	}];

	map.setOptions({styles: styles});

};

var loadScript = function() {

	var script = document.createElement('script');
	script.type = 'text/javascript';
	script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyDhWkB1TFUPtOv5pBBawtIVOgCcwTPMMms&v=3.exp&callback=initialize';
	
	document.body.appendChild(script);

}

window.onload = loadScript;*/