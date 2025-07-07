async function fetchEvents() {
    const res = await fetch('/latest-events');
    const data = await res.json();
    const container = document.getElementById('events');
    container.innerHTML = '';
    data.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        container.appendChild(li);
    });
}

fetchEvents();
setInterval(fetchEvents, 15000); // every 15 seconds
