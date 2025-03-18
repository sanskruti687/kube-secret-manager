document.getElementById("internshipForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission
    
    let fullName = document.getElementById("full_name").value;
    let email = document.getElementById("email").value;

    if (!fullName || !email) {
        alert("All fields are required!");
        return;
    }

    // Submit the form
    fetch("/submit", {
        method: "POST",
        body: new FormData(this)
    }).then(response => response.text())
      .then(data => {
        if (data === "success") {
            document.getElementById("successMessage").style.display = "block";
            document.getElementById("internshipForm").reset(); // Reset form
        }
    });
});
