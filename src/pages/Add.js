import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';

const Add = () => {
  const webcamRef = useRef(null);
  const [capturedImage, setCapturedImage] = useState(null);
  const [uploadedImages, setUploadedImages] = useState([]);

  // Capture a photo from the webcam
  const capturePhoto = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    setCapturedImage(imageSrc);

    // Save the captured image to localStorage
    let storedImages = JSON.parse(localStorage.getItem('capturedImages')) || [];
    storedImages.push(imageSrc);
    localStorage.setItem('capturedImages', JSON.stringify(storedImages));
  };

  // Handle file upload
  const handleFileUpload = (event) => {
    const files = Array.from(event.target.files);
    const newImages = files.map((file) => URL.createObjectURL(file));
    setUploadedImages((prevImages) => [...prevImages, ...newImages]);

    // Save uploaded images to localStorage
    let storedImages = JSON.parse(localStorage.getItem('capturedImages')) || [];
    storedImages.push(...newImages);
    localStorage.setItem('capturedImages', JSON.stringify(storedImages));
  };

  const clearLocalStorage = () => {
    localStorage.removeItem('capturedImages');
    setCapturedImage(null);
    setUploadedImages([]);
    alert('All images have been cleared from localStorage.');
  };

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Add to your Closet</h1>
      <p className="mb-4">Use your webcam to add a photo:</p>

      {!capturedImage ? (
        <>
          <Webcam
            audio={false}
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            className="rounded-md mb-4"
            videoConstraints={{
              width: 300,
              height: 300,
              facingMode: 'user',
            }}
          />
          <button
            className="bg-blue-500 text-white px-4 py-2 rounded-md"
            onClick={capturePhoto}
          >
            Capture Photo
          </button>
        </>
      ) : (
        <div>
          <img src={capturedImage} alt="Captured" className="rounded-md mb-4" />
          <button
            className="bg-gray-500 text-white px-4 py-2 rounded-md ml-4"
            onClick={() => setCapturedImage(null)}
          >
            Next Photo
          </button>
        </div>
      )}

      <div className="mt-4">
        <h2 className="text-lg font-semibold">Upload Images:</h2>
        <input
          type="file"
          accept="image/*"
          multiple
          onChange={handleFileUpload}
          className="mt-2"
        />
      </div>

      {/* Display uploaded images */}
      <div className="mt-4 flex flex-wrap justify-center gap-4">
        {uploadedImages.map((image, index) => (
          <img key={index} src={image} alt={`Uploaded ${index}`} className="rounded-md w-32 h-32 object-cover" />
        ))}
      </div>

      <div className="mt-4">
        <button
          className="bg-red-500 text-white px-4 py-2 rounded-md"
          onClick={clearLocalStorage}
        >
          Clear All Photos
        </button>
      </div>
    </div>
  );
};

export default Add;
