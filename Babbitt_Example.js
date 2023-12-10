<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    #imageContainer {
      position: relative;
      width: 800px; /* Set the width of your image container */
      height: 600px; /* Set the height of your image container */
      overflow: hidden;
    }

    #backgroundImage {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      transition: opacity 0.3s ease-in-out;
    }

    .hotspot {
      position: absolute;
      cursor: pointer;
    }
  </style>
</head>
<body>

<div id="imageContainer">
  <img id="backgroundImage" src="default.jpg" alt="Background Image">

  <!-- Hotspot 1 -->
  <div class="hotspot" style="top: 100px; left: 200px; width: 50px; height: 50px; background-color: red;"></div>

  <!-- Hotspot 2 -->
  <div class="hotspot" style="top: 300px; left: 400px; width: 50px; height: 50px; background-color: blue;"></div>

  <!-- Add more hotspots as needed -->

</div>

<script>
  const backgroundImage = document.getElementById('backgroundImage');
  const hotspots = document.querySelectorAll('.hotspot');

  hotspots.forEach((hotspot, index) => {
    hotspot.addEventListener('mouseover', () => {
      // Change the background image based on the hotspot index
      backgroundImage.src = `image_${index + 1}.jpg`; // Adjust the image filenames accordingly
    });

    hotspot.addEventListener('mouseout', () => {
      // Reset the background image on mouse out
      backgroundImage.src = 'default.jpg';
    });
  });
</script>

</body>
</html>
