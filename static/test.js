function testConfig() {

	fetch("http://127.0.0.1:5000/test_config", {
	    method: "POST",
	    body: JSON.stringify({
	        to_transform: document.getElementById("to_transform").value
        }),
        headers: new Headers({
      		"content-type": "application/json"
    	})
    }).then(function(response) {
	    if (response.status !== 200) {
	      console.log("Could not transform text!");
	      return;
	    }
	    response.json().then(function(data) {
	      document.getElementById('transformed_text').value = data['transformed_text'];
	    });
  	}).catch(error => {
		console.log("Could not update settings!");
	});

}