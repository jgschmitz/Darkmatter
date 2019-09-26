<?php
/* there is a new version of this
/*
/* Example use of the seti REST Api
/* http://setiquest.org/
*/
//Configuration
include_once("config/config.php");
//Get the seti library
include('seti_api.php');
//Set api credentials, api credentials are unique to each user
$seti = new SETI('aa720d2345c7a8476bd214f13d28025d', '92170641d84aae9b7353a20fb2832118');
//Check if user is trying to skip or report an image
if(!empty($_GET['skip'])) {
	
	$seti->send_image_response($_GET['skip'], false);
	header('Location: example.php');
	exit;
	
} elseif(isset($_GET['report']) and $_GET['report']) {
        $response = $_POST['scale'];	
	$seti->send_image_response($_GET['report'], $response);
	header('Location: example.php');
	exit;
	
}
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>SETI RESTful API</title>
<style type="text/css">
<!--
#header_contain {
	position:absolute;
	width:98%;
        height: 45px;
	z-index:1;
	left: 0px;
	top: 0px;
	padding:1%;
	background-color: #F4F4F4;
	border-bottom:solid 1px #CCC;
	font-family:Tahoma, Geneva, sans-serif;
	font-size:12px;
	color:#666;
	font-weight:bold;
}
#details_contain1 {
	position:absolute;
	width:44%;
	padding:1%;
	z-index:2;
	left: 5%;
	top: 75px;
	font-family:Tahoma, Geneva, sans-serif;
	font-size:13px;
	background-color: #F4F5FB;
}
#details_contain2 {
	position:absolute;
	width:44%;
	padding:1%;
	z-index:2;
	right: 5%;
	top: 75px;
	font-family:Tahoma, Geneva, sans-serif;
	font-size:13px;
	background-color: #F4F5FB;
}
#image_contain1 {
	position:absolute;
	width:45%;
	z-index:3;
	left: 5%;
	top: 123px;
	text-align:center;
}
#image_contain2 {
	position:absolute;
	width:45%;
	z-index:3;
	left: 50%;
	top: 123px;
	text-align:center;
}
-->
</style>
</head>
<body>
<div id="header_contain">SETI RESTful API<br/>
  <center>
    <?php
      //Get the array for a image from the cloud
      $image_array = $seti->get_image($config['image_count']);
      if (count($image_array) < $config['image_count']) {
        print "No images to process";
      } else {
    ?>
    Please select a scale of how different these two images are 
    <form name="cform" action="<?php echo $_SERVER['PHP_SELF'] . '?report='.$image_array[1]->image_id.':'.$image_array[2]->image_id ; ?>" method="POST">
      Very similar &nbsp;
      <?php
        for ($i = 0; $i <= $config['max_compare_scale']; $i++) {
          $enabled = $i == $config['max_compare_scale'] ? "checked": "";
          print '<input type="radio" '.$enabled.' name="scale" value="'.$i.'">'.$i;
        }
      ?>
      &nbsp;
      Very different
      &nbsp;
      <input type="submit" name="submit" value="Submit"/>
    </form>
  </center>
</div>
<div id="details_contain1">Image taken between <?php echo $image_array[1]->start_time; ?> and <?php echo $image_array[1]->end_time; ?> on the frequency <?php echo $image_array[1]->frequency; ?></div>
<div id="image_contain1"><img src="<?php echo $image_array[1]->url; ?>" /></div>
<div id="details_contain2">Image taken between <?php echo $image_array[2]->start_time; ?> and <?php echo $image_array[2]->end_time; ?> on the frequency <?php echo $image_array[2]->frequency; ?></div>
<div id="image_contain2"><img src="<?php echo $image_array[2]->url; ?>" /></div>
<?php
  } // end if
?>
</body>
</html>
