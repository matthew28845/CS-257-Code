function changeColor() {
  the_heading = document.getElementById("hello");
  the_heading.style.color = "red";
}

function displayTime() {
	const my_date = new Date();
  let the_hour = my_date.getHours().toString();
  let the_minutes = my_date.getMinutes().toString();
	time.innerHTML = the_hour + ":" + the_minutes;
}

