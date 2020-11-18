console.log('Webicians');

let form = document.querySelector('form');

form.addEventListener('submit', (event)=>{
	event.preventDefault();
	let first_name=form.fname.value;
	let last_name=form.lname.value;
	let email=form.email.value;
	let phone=form.phone.value;
	let data={first_name:first_name,last_name:last_name,email:email,phone:phone};	
	fetch('/register',{ method:'POST', headers:{ 'Content-Type': 'application/json'}, body:JSON.stringify(data)})
	.then(response => response.json())
	.then((data)=>{
		let name=document.createTextNode(`Hello, ${first_name.toUpperCase()}`);
		let text=document.createTextNode(`Your information has been received. We will send you an email in a few seconds. Kindly check your email for more information.`);
		let p_name=document.createElement('p');
		p_name.appendChild(name);
		let p_text=document.createElement('p');
		p_text.appendChild(text);
		document.querySelector('#content').style.display="none";
		let alert_div=document.createElement('article');
		alert_div.appendChild(p_name);
		alert_div.appendChild(p_text);
		document.body.appendChild(alert_div);			
	});
});
