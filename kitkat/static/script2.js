var expected_vals_6MV = 
	{	'2571/2044':2.522,
		'2581/769':1.972,
		'2581/875':1.976,
		'2581/1120':2.030
	}

var expected_reading = null
	
//console.log("hi cat");
$(document).ready(function(){

	var chosen = $("#id_qa_test_def_id").find(":selected").val()
	$("#id_qa_test_def_id > option[value!="+parseInt(chosen)+"]").remove()
	chosen = $("#id_machine_id").find(":selected").val()
	$("#id_machine_id > option[value!="+parseInt(chosen)+"]").remove()




	$("p:has( > label[for=id_f1-mean_value])").append("<p>Expected Reading: <span id='expected_reading'></span></p>")

	$("textarea[id=id_f1-entered_values]").change(function(){
		var k = $("textarea[id=id_f1-entered_values]").val()
	$("input[name=f1-mean_value]").val(mean_of_values(k))
	$("input[name=f2-value]").val(mean_of_values(k)/expected_reading)
	console.log(expected_reading)
	});

	$("textarea[id=id_f3-entered_values]").change(function(){
		var k = $("textarea[id=id_f3-entered_values]").val()	
		console.log(k)	
		$("input[name=f3-mean_value]").val(mean_of_values(k))
		var g = parseFloat($("input[name=f3-mean_value]").val())/parseFloat($("input[name=f1-mean_value]").val())
		console.log(g)
		$("input[name=f4-value]").val(g)
	});
/*	$("input[name=f3-mean_value]").change(function(){
		var g = parseFloat($("input[name=f3-mean_value]").val())/parseFloat($("input[name=f1-mean_value]").val())
		console.log(g)
		$("input[name=f4-value]").val(g)
});
*/
	$("#id_f_equip-ionchamber").change(function(){
		var ion_chamber = $(this).find(":selected").text();
		$("#expected_reading").empty()
		expected_reading = expected_vals_6MV[ion_chamber]
		$("#expected_reading").append(expected_reading)

	});


});


var mean_of_values = function(string){
	var values = string.split('\n');
	var total = 0.0
	var counter = 0
	for(var i=0; i<values.length; i++){
		//need to add case for brackets
		if(!isNaN(values[i]) && values[i].length !=0 ){
			total = total + parseFloat(values[i]);
			counter += 1;
			}
		}
	return total/counter;	
//	return total
}

