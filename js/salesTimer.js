// Set the end date and time of the sale (adjust as needed)
const saleEndDateTime = new Date('2023-07-31T23:59:59');

function updateTimer() {
  const now = new Date();
  const timeLeft = saleEndDateTime - now;

  if (timeLeft <= 0) {
    // Sale has ended
    document.getElementById('timer').innerHTML = 'Sale has ended!';
    return;
  }

  // Calculate the remaining days, hours, minutes, and seconds
  const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

  // Format the time and update the timer display
  const timerDisplay = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  document.getElementById('timer').innerHTML = timerDisplay;

  // Update the timer every second
  setTimeout(updateTimer, 1000);
}

// Start the timer
updateTimer();
