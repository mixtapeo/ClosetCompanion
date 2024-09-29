// Get all image elements
let images = document.getElementsByTagName('img');

// Check if there are any image elements on the page
if (images.length > 0) {
  // Send a message to the background script to trigger the popup
  console.log("Images found! Sending message...");
  chrome.runtime.sendMessage({ action: "trigger_popup" });
}

// This function makes a request to the Flask server running on localhost:5000
function callFlaskCompare() {
  fetch('http://127.0.0.1:5000/compare/', {
    method: 'GET'
  })
    .then(response => response.json())
    .then(data => {
      console.log('Response from Flask:', data);
      alert('WARDROBE ALERT: ' + JSON.stringify(data)); // Alert for demonstration
    })
    .catch(error => {
      console.error('Error calling Flask:', error);
    });
}

// Example of how to trigger this function (e.g., after detecting images)
callFlaskCompare();

//doc listener dom content loaded
document.addEventListener("DOMContentLoaded", (event) => {
  a = document.querySelectorAll(".favorite.large");
  console.log(a);
  // chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  //   if (request.action === "getDataUrl") {
  //     document.getElementById("capturedImage").src = request.dataUrl;
  //   }
  // });
});
