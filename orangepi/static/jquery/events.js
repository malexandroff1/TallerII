	
$(function () {

	var STATES = {
	ON: 2,
	OFF: 3,
	ON_OFF: 4,
	properties: {
	2: {name: "ON", value: 1, code: "ON"},
	3: {name: "OFF", value: 0, code: "OFF"},
	4: {name: "ON/OFF", value: 1, code: "ON/OFF"}
	}
	};

	var state_ctrl = {
	2 : STATES.ON_OFF,
	3 : STATES.ON_OFF,
	4 : STATES.ON_OFF
	};

	var old_state = [];

	var pines = [];

	{% if selects %}
	pines.push({{ selects|safe }});

	$.each( pines, function( index, pin ){
		var  i = 0;

		$.each( pin, function( index, port ){
			 old_state.push(port['state']);
		});
	});

	var p = 2;

	for (var i = 0; i < old_state.length; i++) {
		if(old_state[i] == 'ON'){
			state_ctrl[p] = STATES.ON;
		}else{
			state_ctrl[p] = STATES.OFF;
		}
		p++;
	}


			

	$("#button-ctr-1").html(STATES.properties[state_ctrl[2]].name);
	$("#button-ctr-2").html(STATES.properties[state_ctrl[3]].name);
	$("#button-ctr-3").html(STATES.properties[state_ctrl[4]].name);

	var port = 2;
	var button = 1;


	for (var i = 0; i < old_state.length; i++) {
		if(STATES.properties[state_ctrl[port]].name == 'ON'){
			$("#button-ctr-" + button).removeClass("btn-warning");
			$("#button-ctr-" + button).addClass("btn-success");
		}else{
			$("#button-ctr-" + button).removeClass("btn-warning");
			$("#button-ctr-" + button).addClass("btn-danger");
		}
		button++;
		port++;
	}


	$( "#button-ctr-1" ).click(function() {
		if (state_ctrl[2] == STATES.ON_OFF) {
			$(this).removeClass("btn-warning");
			$(this).removeClass("btn-danger");
			$(this).addClass("btn-success");
			state_ctrl[2] = STATES.ON;
		}else{
			if (state_ctrl[2]== STATES.ON) {
				$(this).removeClass("btn-success");
				$(this).removeClass("btn-warning");
				$(this).addClass("btn-danger");
				
				state_ctrl[2] = STATES.OFF;
			}else{
				if (state_ctrl[2] == STATES.OFF) {
					$(this).removeClass("btn-danger");
					$(this).removeClass("btn-warning");
					$(this).addClass("btn-success");
					state_ctrl[2] = STATES.ON;
				}
			}
		}
		$(this).html(STATES.properties[state_ctrl[2]].name);
		setLed(2,state_ctrl[2]);
		
	});

	$( "#button-ctr-2" ).click(function() {
		if (state_ctrl[3] == STATES.ON_OFF) {
			$(this).removeClass("btn-warning");
			$(this).removeClass("btn-danger");
			$(this).addClass("btn-success");
			state_ctrl[3] = STATES.ON;
		}else{
			if (state_ctrl[3] == STATES.ON) {
				$(this).removeClass("btn-success");
				$(this).removeClass("btn-warning");
				$(this).addClass("btn-danger");
				
				state_ctrl[3] = STATES.OFF;
			}else{
				if (state_ctrl[3] == STATES.OFF) {
					$(this).removeClass("btn-danger");
					$(this).removeClass("btn-warning");
					$(this).addClass("btn-success");
					state_ctrl[3] = STATES.ON;
				}
			}
		}
		$(this).html(STATES.properties[state_ctrl[3]].name);
		setLed(3,state_ctrl[3]);
		
	});

	$( "#button-ctr-3" ).click(function() {
		if (state_ctrl[4] == STATES.ON_OFF) {
			$(this).removeClass("btn-warning");
			$(this).removeClass("btn-danger");
			$(this).addClass("btn-success");
			state_ctrl[4] = STATES.ON;
		}else{
			if (state_ctrl[4] == STATES.ON) {
				$(this).removeClass("btn-success");
				$(this).removeClass("btn-warning");
				$(this).addClass("btn-danger");
				state_ctrl[4] = STATES.OFF;
			}else{
				if (state_ctrl[4] == STATES.OFF) {
					$(this).removeClass("btn-danger");
					$(this).removeClass("btn-warning");
					$(this).addClass("btn-success");
					state_ctrl[4] = STATES.ON;
				}
			}
		}
		$(this).html(STATES.properties[state_ctrl[4]].name);
		setLed(4,state_ctrl[4]);
		
	});

	function setLed(control,stateCtrl) {
	  $.ajax({
		url: 'controler',
		type: 'POST',    //passing data as post method
		dataType: 'json', // returning data as json
		data:{ led: "" + control + "", state : "" + STATES.properties[stateCtrl].code + ""},
		success: function(result) {
			//var counts = jQuery.parseJSON(json);
			//var status = result[0].status;
			//$("#mh").html(m_humidity + " %");
			//console.log("El estado es: " + status);
			console.log(result);    						
		},
		error: function() {
			console.log("ERROR !!!");
		}
	  });
	}

});
