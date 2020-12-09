// Fetch the current settings
fetch('http://127.0.0.1:5000/get_config')
.then(response => {
	if (!response.ok) {
		// Show error if unable to fetch configurations
		createModal("ERROR", "Cannot modify settings right now...", true);
		document.getElementById("save").disabled = true;
		return Promise.reject('Could not load application!');
    } else {
    	return response.json();
    }
}).then(config => {
	// Update settings on HTML if successfully received
	showSettings(config);
}).catch(error => {
	console.log(error);
});

function showSettings(config) {

    // Set Bi-gram toggle	
	let bi_gram_toggle = document.getElementById("bi_gram_toggle");
	label = document.createElement('label');
	label.setAttribute('class', 'switch');

	input = document.createElement('input');
	input.type = 'checkbox';
	input.id = 'bi_gram_input';
	input.name = 'bi_gram_input';

	if (config["bi_gram"] == 1) {
		input.checked = true;
	} else {
		input.checked = false;
	}

	span = document.createElement('span');
	span.setAttribute('class', 'slider round');

    label.appendChild(input);
    label.appendChild(span);
    bi_gram_toggle.appendChild(label);

    // Set Tri-gram toggle	
	let tri_gram_toggle = document.getElementById("tri_gram_toggle");
	label = document.createElement('label');
	label.setAttribute('class', 'switch');

	input = document.createElement('input');
	input.type = 'checkbox';
	input.id = 'tri_gram_input';
	input.name = 'tri_gram_input';

	if (config["tri_gram"] == 1) {
		input.checked = true;
	} else {
		input.checked = false;
	}

	span = document.createElement('span');
	span.setAttribute('class', 'slider round');

    label.appendChild(input);
    label.appendChild(span);
    tri_gram_toggle.appendChild(label);

    // Set All Links toggle
	let all_links_toggle = document.getElementById("all_links");
	label = document.createElement('label');
	label.setAttribute('class', 'switch');

	input = document.createElement('input');
	input.type = 'checkbox';
	input.id = 'all_links_input';
	input.name = 'all_links_input';

	if (config["links"] == 1) {
		input.checked = true;
	} else {
		input.checked = false;
	}

	span = document.createElement('span');
	span.setAttribute('class', 'slider round');

    label.appendChild(input);
    label.appendChild(span);
    all_links_toggle.appendChild(label);

    // Set stop words
    let stop_words = document.getElementById('stop_words');
    stop_words.value = config['stop_words'];
}

// Save configuration on click of `Save Settings` button
function saveConfig() {

	// Send a POST API call to save the new settings
	fetch("http://127.0.0.1:5000/save_config", {
	    method: "POST",
	    body: JSON.stringify({
	        lemmatization: 0, // Future support
	        stemming: 0, // Future support
	        bi_gram: document.getElementById("bi_gram_input").checked ? 1 : 0,
	        tri_gram: document.getElementById("tri_gram_input").checked ? 1 : 0,
	        links: document.getElementById("all_links_input").checked ? 1 : 0,
	        stop_words: document.getElementById("stop_words").value,
	        update_interval: 1
        }),
        headers: new Headers({
      		"content-type": "application/json"
    	})
    }).then(function(response) {
		if (!response.ok) {
			// Popup error is not updated
			createModal("ERROR", "Cannot modify settings right now...", true);
			document.getElementById("save").disabled = true;
			return Promise.reject('Could not load application!');
	    } else {
	    	// Popup to show the settings were successfully updated
			createModal("SUCCESS", "Settings saved successfully!!!", true);
	    	return response.json();
	    }
  	}).catch(error => {
		console.log("Could not update settings!");
	});

}
