function getFormattedDate() {
    const now = new Date();
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    };
    return now.toLocaleDateString('en-US', options);
}

function getFormattedTime() {
    const now = new Date();
    const options = {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
    };
    return now.toLocaleTimeString('en-US', options);
}

function updateDateTime() {
    const dateString = getFormattedDate();
    const timeString = getFormattedTime();
    document.getElementById('date').textContent = dateString;
    document.getElementById('time').textContent = timeString;
}
function setTheme(themeName) {
    document.documentElement.setAttribute('data-theme', themeName);
    localStorage.setItem('theme', themeName);
}

function toggleTheme() {
    if (localStorage.getItem('theme') === 'dark') {
        setTheme('light');
         document.getElementById('theme-toggle').checked = true;
    } else {
        setTheme('dark');
        document.getElementById('theme-toggle').checked = false;
    }
}
// Immediately invoked function to set the initial theme and toggle state
function initializeTheme() {
    const theme = localStorage.getItem('theme');
    const toggleSwitch = document.getElementById('theme-toggle');
    if (theme === 'dark') {
        setTheme('dark');
        toggleSwitch.checked = false;
    } else {
        setTheme('light');
        toggleSwitch.checked = true;
    }
}

initializeTheme();
document.getElementById('theme-toggle').addEventListener('click', toggleTheme);



updateDateTime();

// Update the date and time every second
setInterval(updateDateTime, 1000);

// Ensure the date and time is updated when the page loads
window.onload = function() {
    updateDateTime();
};
