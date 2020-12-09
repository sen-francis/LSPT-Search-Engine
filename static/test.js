// Test transformation of text based on latest settings
function testConfig() {

	// Send a POST request with the uploaded content
	fetch("http://127.0.0.1:5000/test_config", {
	    method: "POST",
	    body: JSON.stringify({
	        to_transform: document.getElementById("to_transform").value
        }),
        headers: new Headers({
      		"content-type": "application/json"
    	})
    }).then(function(response) {
		if (!response.ok) {
			// Popup if the transformation could not be done
			createModal("ERROR", "Cannot do transformations right now...", true);
			document.getElementById("transform_button").disabled = true;
			return Promise.reject('Could not load application!');
	    } else {
	    	// Update the right text area with transformation if it was
	    	// successfully completed
			response.json().then(function(data) {
		      document.getElementById('transformed_text').value = JSON.stringify(data["transformed_text"], undefined, 4);
		    });
	    }
  	}).catch(error => {
		console.log("Could not test transformation...");
	});

}
