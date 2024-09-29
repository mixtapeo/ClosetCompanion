// Get all image elements
let images = document.getElementsByTagName('img');

// Check if there are any image elements on the page
if (images.length > 0) {
  // Send a message to the background script to trigger the popup
  console.log("Images found! Sending message...");
  chrome.runtime.sendMessage({ action: "trigger_popup" });
}

// This function makes a request to the Flask server running on localhost:5000
function callFlaskCompare(link) {
  return fetch('http://127.0.0.1:5000/api/compare', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ link: link })
  })
    .then(response => response.json())
    .then(data => {
      console.log('Response from Flask:', data);
      return data.message; // Return the message from the response
    })
    .catch(error => {
      console.error('Error calling Flask:', error);
      return null; // Return null in case of error
    });
}

function compareProduct() {
  // Find the div with the class 'swiper-slide swiper-slide-active'
  let imageDiv = document.getElementsByClassName("swiper-slide swiper-slide-active")[0];
  if (imageDiv) {
    // Find the <img> tag inside that div 
    let imageElement = imageDiv.querySelector('img');
    
    if (imageElement) {
      // Get the image URL from the src attribute
      let imageUrl = imageElement.src;
      console.log("Product Image URL: ", imageUrl);
      
      // Call the function to send the image URL to the Flask server
      callFlaskCompare(imageUrl).then(decision => {
        if (decision === 1) {
          alert('WARDROBE ALERT: You have a similar item in your closet already!');
        }
      });
      
      return imageUrl;
    } else {
      console.error("Image tag not found in the div.");
      console.log(imageDiv);
      return null;
    }
  } else {
    console.error("div not found.");
    return null;
  }
}

// Run the function when the page loads
document.addEventListener("DOMContentLoaded", compareProduct);
// Also run the function after a certain delay (e.g., 5 seconds)
setTimeout(compareProduct, 3200); // milliseconds = 3.2 seconds


// Check if the current URL matches the desired pattern
function shouldRun() {
  return location.href.startsWith('https://www.uniqlo.com/ca/en/products/');
}

// Run the function when the page loads if the URL matches
document.addEventListener("DOMContentLoaded", () => {
  if (shouldRun()) {
    compareProduct();
  }
});

let currentUrl = location.href;
const observer = new MutationObserver(() => {
  if (location.href !== currentUrl) {
    console.log('URL changed to: ' + location.href);
    currentUrl = location.href;
    if (shouldRun()) {
      console.log('Running compareProduct()...');
      setTimeout(compareProduct, 2200); // milliseconds = 2.2 seconds
    }
  }
});

observer.observe(document, { subtree: true, childList: true });