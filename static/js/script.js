document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const status = document.getElementById("status");

    form.addEventListener("submit", function () {
        status.textContent = "Uploading and generating report... Please wait.";
    });
});
