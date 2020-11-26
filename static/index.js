// Fetch the current settings
fetch('http://128.213.60.117:5000/get_config')
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

	// Set Lemmatization toggle	
	let lemmatization_toggle = document.getElementById("lemmatization_toggle");
	let label = document.createElement('label');
	label.setAttribute('class', 'switch');

	let input = document.createElement('input');
	input.type = 'checkbox';
	input.id = 'lemmatization_input';
	input.name = 'lemmatization_input';

	if (config["lemmatization"] == 1) {
		input.checked = true;
	} else {
		input.checked = false;
	}

	let span = document.createElement('span');
	span.setAttribute('class', 'slider round');

    label.appendChild(input);
    label.appendChild(span);
    lemmatization_toggle.appendChild(label);

    // Set Stemming toggle	
	let stemming_toggle = document.getElementById("stemming_toggle");
	label = document.createElement('label');
	label.setAttribute('class', 'switch');

	input = document.createElement('input');
	input.type = 'checkbox';
	input.id = 'stemming_input';
	input.name = 'stemming_input';

	if (config["stemming"] == 1) {
		input.checked = true;
	} else {
		input.checked = false;
	}

	span = document.createElement('span');
	span.setAttribute('class', 'slider round');

    label.appendChild(input);
    label.appendChild(span);
    stemming_toggle.appendChild(label);

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

    // Set stop words
    let stop_words = document.getElementById('stop_words');
    stop_words.value = config['stop_words'];

    // Set update interval dropdown
    let select = document.createElement('select');
    select.setAttribute('class', 'px-2 py-2');
    select.setAttribute('id', 'update_interval_dropdown');
    select.setAttribute('style', 'width: 100%; border-style: solid; border-radius: 4px;');

    let option;

    let options = ["Once a day", "Twice a day", "Thrice a day", "Four times a day", "Five times a day"];
    for (let i=1; i<=5; i++) {
    	option = document.createElement('option');
    	option.value = i;
    	option.innerHTML = options[i-1];
    	option.selected = config['update_interval'] == i ? true : false;
    	select.appendChild(option);
    }

    let dropdown = document.getElementById('update_dropdown');
    dropdown.appendChild(select);
}

// Save configuration on click of `Save Settings` button
function saveConfig() {

	// Send a POST API call to save the new settings
	fetch("http://128.213.60.117:5000/save_config", {
	    method: "POST",
	    body: JSON.stringify({
	        lemmatization: document.getElementById("lemmatization_input").checked ? 1 : 0,
	        stemming: document.getElementById("stemming_input").checked ? 1 : 0,
	        bi_gram: document.getElementById("bi_gram_input").checked ? 1 : 0,
	        tri_gram: document.getElementById("tri_gram_input").checked ? 1 : 0,
	        stop_words: document.getElementById("stop_words").value,
	        update_interval: parseInt(document.getElementById("update_interval_dropdown").value)
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
