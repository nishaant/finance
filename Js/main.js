var getStock = function(){
	var stockName = $("#sname").val();
	if(!stockName)
	{
		alert("Please Enter Stock Name Correctly");
	}
	else
	{
	    var url = "http://localhost:9001/stock/" + stockName;
		jQuery.ajax({
			url: url,
			method: "get",
			dataType: "text",
			crossDomain: true,
            success: function(data) {
                var jsonData = JSON.parse(data);
                appendData(jsonData);
            },
            error : function(jqXHR, textStatus, errorThrown) {
     		alert(textStatus);
            },

		});
	}
}

var appendData = function(jsonData)
    {

        var resultDiv = $("#result");
        for( index in jsonData)
        {
            resultDiv.append("<span>" + jsonData[index] + "</span><br>");
        }
    }