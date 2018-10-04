$( document ).ready(function(){

	var STATES = {
	  ON: 1,
	  OFF: 2,
	  ON_OFF: 3,
	  properties: {
		1: {name: "ON", value: 1, code: "ON"},
		2: {name: "OFF", value: 0, code: "OFF"},
		3: {name: "ON/OFF", value: 1, code: "ON/OFF"}
	  }
	};

	var state_ctrl_1 = STATES.ON_OFF;
	var state_ctrl_2 = STATES.ON_OFF;
	var state_ctrl_3 = STATES.ON_OFF;

	$("#button-ctr-1").html(STATES.properties[state_ctrl_1].name);
	$("#button-ctr-2").html(STATES.properties[state_ctrl_1].name);
	$("#button-ctr-3").html(STATES.properties[state_ctrl_1].name);


	$( "#button-ctr-1" ).click(function() {
		if (state_ctrl_1 == STATES.ON_OFF) {
			$(this).removeClass("btn-warning");
			$(this).removeClass("btn-danger");
			$(this).addClass("btn-success");
			state_ctrl_1 = STATES.ON;
		}else{
			if (state_ctrl_1 == STATES.ON) {
				$(this).removeClass("btn-success");
				$(this).removeClass("btn-warning");
				$(this).addClass("btn-danger");
				
				state_ctrl_1 = STATES.OFF;
			}else{
				if (state_ctrl_1 == STATES.OFF) {
					$(this).removeClass("btn-danger");
					$(this).removeClass("btn-warning");
					$(this).addClass("btn-success");
					state_ctrl_1 = STATES.ON;
				}
			}
		}
		$(this).html(STATES.properties[state_ctrl_1].name);
		setLed(10,state_ctrl_1);
		
	});

	$( "#button-ctr-2" ).click(function() {
		if (state_ctrl_2 == STATES.ON_OFF) {
			$(this).removeClass("btn-warning");
			$(this).removeClass("btn-danger");
			$(this).addClass("btn-success");
			state_ctrl_2 = STATES.ON;
		}else{
			if (state_ctrl_2 == STATES.ON) {
				$(this).removeClass("btn-success");
				$(this).removeClass("btn-warning");
				$(this).addClass("btn-danger");
				
				state_ctrl_2 = STATES.OFF;
			}else{
				if (state_ctrl_2 == STATES.OFF) {
					$(this).removeClass("btn-danger");
					$(this).removeClass("btn-warning");
					$(this).addClass("btn-success");
					state_ctrl_2 = STATES.ON;
				}
			}
		}
		$(this).html(STATES.properties[state_ctrl_2].name);
		setLed(3,state_ctrl_2);
		
	});

	$( "#button-ctr-3" ).click(function() {
		if (state_ctrl_3 == STATES.ON_OFF) {
			$(this).removeClass("btn-warning");
			$(this).removeClass("btn-danger");
			$(this).addClass("btn-success");
			state_ctrl_3 = STATES.ON;
		}else{
			if (state_ctrl_3 == STATES.ON) {
				$(this).removeClass("btn-success");
				$(this).removeClass("btn-warning");
				$(this).addClass("btn-danger");
				state_ctrl_3 = STATES.OFF;
			}else{
				if (state_ctrl_3 == STATES.OFF) {
					$(this).removeClass("btn-danger");
					$(this).removeClass("btn-warning");
					$(this).addClass("btn-success");
					state_ctrl_3 = STATES.ON;
				}
			}
		}
		$(this).html(STATES.properties[state_ctrl_3].name);
		setLed(4,state_ctrl_3);
		
	});

	function setLed(control,state_control) {
	  $.ajax({
		url: 'controler',
		type: 'POST',    //passing data as post method
		dataType: 'json', // returning data as json
		data:{ led: "" + control + "", state : "" + STATES.properties[state_control].code + ""},
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
	
	/*

	var counts = jQuery.parseJSON('{{ test|safe }}');

	var a_temperature,a_humidity,a_pressure,a_windspeed,m_temperature,m_humidity,m_pressure,m_windspeed;


	a_temperature = counts[0].temp;
	m_temperature = counts[1].temp;
	

	$("#at").html(a_temperature + " °C");
	

	*/

});