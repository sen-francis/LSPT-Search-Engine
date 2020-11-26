function createModal(title, message, canClose) {

	let modal = document.createElement('div');
	modal.setAttribute('class', 'modal');
	modal.setAttribute('id', 'info-modal');
	modal.setAttribute('style', 'display:  block; background-color: rgba(128, 128, 128, 0.5);');
	modal.setAttribute('tabindex', '-1');
	modal.setAttribute('role', 'dialog');
	modal.setAttribute('data-keyboard', 'false');
	modal.setAttribute('data-backdrop', 'static');

	let dialog = document.createElement('div');
	dialog.setAttribute('class', 'modal-dialog');
	dialog.setAttribute('role', 'document');

	let content = document.createElement('div');
	content.setAttribute('class', 'modal-content');

	let header = document.createElement('div');
	header.setAttribute('class', 'modal-header');

	let heading = document.createElement('h5');
	heading.setAttribute('class', 'modal-title');
	heading.innerHTML = title;

	header.appendChild(heading);

	let body = document.createElement('div');
	body.setAttribute('class', 'modal-body');

	let p = document.createElement('p');
	p.innerHTML = message;

	body.appendChild(p);

	content.appendChild(header);
	content.appendChild(body);

	if (canClose == true) {

		let footer = document.createElement('div');
		footer.setAttribute('class', 'modal-footer');

		let button = document.createElement('button');
		button.setAttribute('type', 'button');
		button.setAttribute('class', 'btn btn-secondary');
		button.setAttribute('data-dismiss', 'modal');
		button.setAttribute('onClick', 'closeModal();');
		button.innerHTML = 'Close';

		footer.appendChild(button);

		content.appendChild(footer);
	}

	dialog.appendChild(content);
	modal.appendChild(dialog);

	let main_body = document.getElementById("main");
	main_body.appendChild(modal);
}

function closeModal() {
	document.getElementById('info-modal').remove();
}