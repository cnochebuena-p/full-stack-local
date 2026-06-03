async function loadCount() {
    const response = await fetch("/api/count");
    const data = await response.json();

    document.getElementById("counter").textContent = data.count;
}

document.getElementById("btn").addEventListener("click", async () => {
    const response = await fetch("/api/increment", {
        method: "POST"
    });

    const data = await response.json();

    document.getElementById("counter").textContent = data.count;
});

loadCount();