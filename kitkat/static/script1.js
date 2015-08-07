var daily_photon_test_upper_bound = 197.5
var daily_photon_test_lower_bound = 186.0

/*
$.ajax({
    type: 'POST',
    url: 'popup.aspx/GetJewellerAssets',
    contentType: 'application/json; charset=utf-8',
    data: { jewellerId: filter, locale: 'en-US' },
    dataType: 'json',
    success: AjaxSucceeded,
    error: AjaxFailed
});
*/



$(document).ready(function(){
//	$("#testing").append(".....")
	var machine = $("#id_machine_id").find(":selected").text();
	//$('form').append(machine + "...")
	$("html").append("<div id='flot' style='width:700px;height:300px'></div>")
	$.get('/kitkat/recent_results_daily_photon_output_test/', {machine_name: machine}, function(data){
		console.log(data)
		//$('form').append(data);
		var plot_data = []
		var points = data.split("/")
		for(var j=0; j<points.length; j++){
			var sep = (points[j]).split(" ")
			plot_data.push([parseInt(sep[0]), parseFloat(sep[1])])
			}
		console.log(plot_data[0])
		var options = {
			xaxis: { mode: "time" }, 
			series: {
    				lines: {
        				show: true,
        				lineWidth: 2,
					color: "red"
        				//fill: true,
        				//fillColor: "red"
    				}
			}
		};

		$.plot("#flot", [{data:plot_data, color:"red", hoverable:true}], options);

	});

	console.log("in the script");
	$("p:has( > label[for=id_f1-value])").append("<p id='pass_fail'>&nbsp</p>")
//	console.log($("pass_fail")
//  $("p").append(" Yes, a frog")
//	$("input[name=f1-value]").change(function(){
	$("input[name=f1-value]").change(function(){
		console.log("...")
//		$("#testing").append(".....")
   		var toAdd = $("input[name=f1-value]").val();
		console.log(toAdd)

//   var toAdd = $("input[name=f1-value]").val();
//   $("form").append("<p col='red'>hi!!! " + toAdd +"</p")
//	$("#pass").empty()
//	$("#pass").append(toAdd)
	if( (toAdd >= daily_photon_test_lower_bound) && (toAdd <= daily_photon_test_upper_bound) ){
//		$("p:has( > label[for=id_f1-value])").append("<p><font color='green'>OK</font></p>");
//		console.log($("p:has( > label[for=id_f1-value])").html())
//		$("#testing").append("<p><font color='green'>OK</font></p>");
		$("#pass_fail").empty()
		$("#pass_fail").append("<font color='green'>OK</font>")
	}
	else{
/*		$("p:has( > label[for=id_f1-value])").append("<p><font color='red'>Outside of test bounds (" + daily_photon_test_lower_bound + 
	"," + daily_photon_test_upper_bound + ")</font></p>"); */
		$("#pass_fail").empty()
		$("#pass_fail").append("<font color='red'>Outside of test bounds (" + daily_photon_test_lower_bound + 
	"," + daily_photon_test_upper_bound + ")</font>")
	}
	
	});
//some code to test drop down menu:
	$("select").change(function(){
		console.log($("select").html())
		console.log($("form").html())

});


});

