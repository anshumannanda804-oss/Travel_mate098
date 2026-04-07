
function planTrip() {
    const destinationInput = document.getElementById("destination");
    const daysInput = document.getElementById("days");

    const destination = destinationInput.value.trim();
    const days = parseInt(daysInput.value);

    // Destination validation
    if (destination.length < 3) {
        alert("Please enter a valid destination name");
        destinationInput.focus();
        return;
    }

    // Reject numeric-only destination
    if (!isNaN(destination)) {
        alert("Destination cannot be only numbers");
        destinationInput.focus();
        return;
    }

    // Reject special characters
    if (!/^[a-zA-Z\s]+$/.test(destination)) {
        alert("Destination should contain only letters");
        destinationInput.focus();
        return;
    }

    // Days validation
    if (isNaN(days) || days < 1) {
        alert("Number of days must be at least 1");
        daysInput.focus();
        return;
    }

    // Trip object
    const trip = {
        destination: destination,
        days: days,
        budget: days * 5000
    };

    // Store data
    localStorage.setItem("trip", JSON.stringify(trip));

    // Navigate to results
    window.location.href = "results.html";


    let map;

    function initMapInstant() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 20.5937, lng: 78.9629 }, // India
        zoom: 5
    });
}

}
