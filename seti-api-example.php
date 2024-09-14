<?php
// Load Config and Seti API
include_once("config/config.php");
include('seti_api.php');

// Set API credentials
$seti = new SETI($config['api_key'], $config['api_secret']);

// Image Response Handling
if (!empty($_GET['skip'])) {
    $seti->send_image_response($_GET['skip'], false);
    header('Location: example.php');
    exit;
} elseif (isset($_GET['report']) && $_GET['report']) {
    $response = $_POST['scale'];
    $seti->send_image_response($_GET['report'], $response);
    header('Location: example.php');
    exit;
}

// Fetch image from the API
$image_array = $seti->get_image($config['image_count']);
if (count($image_array) < $config['image_count']) {
    echo "No images to process.";
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SETI RESTful API</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { display: flex; flex-direction: column; align-items: center; margin: 20px; }
        .images { display: flex; justify-content: space-between; width: 100%; max-width: 900px; }
        .image-box { padding: 20px; background-color: #f5f5f5; text-align: center; width: 45%; }
        .header { padding: 10px; background-color: #eaeaea; font-weight: bold; text-align: center; width: 100%; }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h2>SETI RESTful API - Image Comparison</h2>
        <p>Please select a scale of how different these two images are.</p>
    </div>
    
    <form action="<?php echo $_SERVER['PHP_SELF'] . '?report=' . $image_array[1]->image_id . ':' . $image_array[2]->image_id; ?>" method="POST">
        <div style="text-align: center;">
            Very Similar &nbsp;
            <?php for ($i = 0; $i <= $config['max_compare_scale']; $i++): ?>
                <input type="radio" name="scale" value="<?php echo $i; ?>" <?php echo $i == $config['max_compare_scale'] ? 'checked' : ''; ?> />
                <?php echo $i; ?>
            <?php endfor; ?>
            &nbsp; Very Different
        </div>
        <br>
        <input type="submit" name="submit" value="Submit">
    </form>
    
    <div class="images">
        <div class="image-box">
            <p>Image from <?php echo $image_array[1]->start_time; ?> to <?php echo $image_array[1]->end_time; ?> <br> Frequency: <?php echo $image_array[1]->frequency; ?></p>
            <img src="<?php echo $image_array[1]->url; ?>" alt="Image 1" />
        </div>
        <div class="image-box">
            <p>Image from <?php echo $image_array[2]->start_time; ?> to <?php echo $image_array[2]->end_time; ?> <br> Frequency: <?php echo $image_array[2]->frequency; ?></p>
            <img src="<?php echo $image_array[2]->url; ?>" alt="Image 2" />
        </div>
    </div>
</div>
</body>
</html>
