document.getElementById("internshipForm").addEventListener("submit", function(event) {
    let fullName = document.getElementById("full_name").value;
    let email = document.getElementById("email").value;
    let resume = document.getElementById("resume").files[0];

    if (!fullName || !email || !resume) {
        alert("All fields are required!");
        event.preventDefault();
    }
});
