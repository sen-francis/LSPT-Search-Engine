fetch('http://127.0.0.1:5000/get_config')
.then(response => {
	if (!response.ok) {
       return Promise.reject('Could not fetch configuration information from GitHub');
    }
    return response.json();
}).then(config => {
	showSettings(config);
}).catch(error => {
	console.log(error);
});

function showSettings(config) {
	
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
}

function saveConfig() {

	fetch("http://127.0.0.1:5000/save_config", {
	    method: "POST",
	    body: JSON.stringify({
	        lemmatization: document.getElementById("lemmatization_input").checked ? 1 : 0,
	        lemmatization: document.getElementById("lemmatization_input").checked ? 1 : 0
        }),
        headers: new Headers({
      		"content-type": "application/json"
    	})
    }).then(response => {
	  console.log("Settings updated!");
	}).catch(error => {
		console.log("Could not update settings!");
	});

}