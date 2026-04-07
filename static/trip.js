function planTrip() {
    console.log("Plan Trip clicked");

    const destinationInput = document.getElementById("destination");
    const daysInput = document.getElementById("days");

    if (!destinationInput || !daysInput) {
        console.error("Input elements not found");
        return;
    }

    const destination = destinationInput.value.trim();
    const days = parseInt(daysInput.value);

    // -------- VALIDATIONS --------
    if (destination.length < 3) {
        alert("Please enter a valid destination name");
        return;
    }

    if (!isNaN(destination)) {
        alert("Destination cannot be only numbers");
        return;
    }

    if (!/^[a-zA-Z\s]+$/.test(destination)) {
        alert("Destination should contain only letters");
        return;
    }

    if (isNaN(days) || days < 1) {
        alert("Number of days must be at least 1");
        return;
    }

    // -------- SAVE BASIC DATA --------
    localStorage.setItem("trip", JSON.stringify({
        destination,
        days,
        budget: days * 5000
    }));

    // -------- INSTANT REDIRECT --------
    window.location.href = "results.html";
}
