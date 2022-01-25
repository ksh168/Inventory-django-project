document.getElementById("add-new-btn").addEventListener("click", function() {
	document.querySelector(".bg-modal").style.display = "flex";
	console.log("add-new-btn clicked");
});

document.querySelector(".close").addEventListener("click", function() {
	document.querySelector(".bg-modal").style.display = "none";
	console.log("close clicked");
});