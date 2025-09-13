// App.jsx
import { useEffect, useState } from "react";

function App() {
  const [images, setImages] = useState([]);
  const [scale, setScale] = useState(5);
  const maxScale = 5;

  useEffect(() => {
    fetch("/api/images")
      .then((res) => res.json())
      .then(setImages)
      .catch(() => alert("Failed to load images"));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (images.length < 2) return;

    const ids = `${images[0].image_id}:${images[1].image_id}`;
    const res = await fetch("/api/report", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ids, scale }),
    });
    if (res.ok) alert("Report submitted!");
    else alert("Failed to submit report");
  };

  if (images.length < 2) return <p className="p-4">Loading images...</p>;

  return (
    <div className="flex flex-col items-center p-6">
      <h2 className="text-xl font-bold mb-2">SETI RESTful API - Image Comparison</h2>
      <p className="mb-4">Please select a scale of how different these two images are.</p>

      <form onSubmit={handleSubmit} className="mb-6">
        <div className="flex items-center gap-2">
          <span>Very Similar</span>
          {Array.from({ length: maxScale + 1 }, (_, i) => (
            <label key={i} className="flex flex-col items-center">
              <input
                type="radio"
                name="scale"
                value={i}
                checked={scale === i}
                onChange={() => setScale(i)}
              />
              {i}
            </label>
          ))}
          <span>Very Different</span>
        </div>
        <button
          type="submit"
          className="mt-4 px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600"
        >
          Submit
        </button>
      </form>

      <div className="flex gap-4 w-full max-w-4xl">
        {images.slice(0, 2).map((img, idx) => (
          <div key={idx} className="w-1/2 p-4 bg-gray-100 rounded shadow text-center">
            <p>
              Image from {img.start_time} to {img.end_time} <br />
              Frequency: {img.frequency}
            </p>
            <img src={img.url} alt={`Image ${idx + 1}`} className="mt-2 mx-auto max-h-80" />
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
