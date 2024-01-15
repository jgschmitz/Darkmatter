<?php
/*
/* SETI REST API
/* Api requests are targeted here
include_once('config/config.php');
//Connect to MapR DB
mysql_select_db($config['databasename'], mysql_connect($config['dbhost'], $config['dbuser'], $config['dbpassword']));
//Validate credentials
if(mysql_num_rows(mysql_query("select `public_key`, `private_key` from user_base where public_key='" . mysql_real_escape_string($_GET['public_key']) . "' and private_key='" . mysql_real_escape_string($_GET['private_key']) . "' limit 0, 1")) == 0) {
	
	header("HTTP/1.1 403 Totally Forbidden");
	echo ' ';
	exit;
pri
}
//Check if session key is blank and a key is not being requested
if(empty($_GET['session_key']) && $_GET['data'] != 'new_session_key') {
	
	header("HTTP/1.1 403 No Access");
	echo ' ';
	exit;
	
}
//Check for GET verb
if(!empty($_GET['data'])) {
	
	//Split the request
	$GET_data = explode('/', $_GET['data']);
	
	//Determine the request
	switch($GET_data[0]) {
		
		# Returns a new session key
		case 'new_session_key':
		
			//Generate new key
			$counter = 1;
			while($counter == 1) {
				
				$session_key = md5(time() . mt_rand(10000, 99999));
				
				//Check if session_key exists
				if(mysql_num_rows(mysql_query("select `session_key` from user_session_key where session_key='" . $session_key . "' limit 0, 1")) == 0) {
					
					//Get the users id
					$res = mysql_query("select `user_id`, `public_key`, `private_key` from user_base where public_key='" . mysql_real_escape_string($_GET['public_key']) . "' and private_key='" . mysql_real_escape_string($_GET['private_key']) . "' limit 0, 1");
					while($row = mysql_fetch_array($res)) {
						
						//Register the key and return it
					mysql_query("insert into user_session_key (`user_id`, `session_key`, `stamp_added`) values ('" . $row['user_id'] . "', '" . $session_key . "', '" . time() . "')");
						echo $session_key;
						
						$counter = 0;
						
					}
					
				}
				
			}
			
		break;
		
		# Returns the server status's in json format
		case 'server_status':
			
			$server_status = array();
			
			//Get stats
			$res = mysql_query("select * from server_status");
			while($row = mysql_fetch_array($res)) {
				
				$server_status[$row['server_name']]['status'] = $row['server_operational'];
				$server_status[$row['server_name']]['comments'] = $row['additional_comments'];
				$server_status[$row['server_name']]['last_updated'] = $row['last_updated'];
				
			}
			
			//Encode to json
			echo json_encode($server_status);
			
		break;
		
		# Returns image and its details in json format
		case 'image':
			
			$image[1]  = array();
			
			for($counter = 1; $counter <= $GET_data[1]; $counter ++) {
		
				if(empty($GET_data[2])) {
					
					//Get a random image which has the lowest display code (highest priority)
					$res = mysql_query("select * from image_base order by display_code");
					while($row = mysql_fetch_array($res)) {
						
						//Check if the end user has viewed this image
                                                $sql = "select `image_id`, `session_key` from image_view where session_key='" . mysql_real_escape_string($_GET['session_key']) . "' and image_id='" . $row['image_id'] . "' limit 0, 1";
						if(mysql_num_rows(mysql_query($sql)) == 0) {
							
							//Set array data
							$image[$counter] = array('image_id' => $row['image_id'], 'url' => $config['server'] . '/data/' . $row['folder_name'] . $row['file_name'], 'frequency' => $row['data_frequency'], 'sample_rate' => $row['data_sample_rate'], 'bandwidth' => $row['data_bandwidth'], 'start_time' => $row['data_start_time'], 'end_time' => $row['data_end_time'], 'antennas' => $row['data_antennas'], 'data_pols' => $row['data_pols']);
							
							//Mark the view
							mysql_query("update image_base set total_views=total_views + 1 where image_id='" . $row['image_id'] . "'");
							
							//Get the users id and mark view
							$res1 = mysql_query("select `user_id`, `public_key`, `private_key` from user_base where public_key='" . mysql_real_escape_string($_GET['public_key']) . "' and private_key='" . mysql_real_escape_string($_GET['private_key']) . "' limit 0, 1");
							while($row1 = mysql_fetch_array($res1)) {
								
								mysql_query("insert into image_view (`image_id`, `user_id`, `session_key`, `stamp_added`) values ('" . $row['image_id'] . "', '" . $row1['user_id'] . "', '" . $_GET['session_key'] . "', '" . time() . "')");
							
							}
							
							break;
							
						}
						
					}
					
				} else {
					
					//Get a specific image
					$res = mysql_query("select * from image_base where image_id='" . $GET_data[2] . "' limit 0, 1");
					while($row = mysql_fetch_array($res)) {
						
						//Set array data
						$image[$counter] = array('image_id' => $row['image_id'], 'url' => $config['server'] . '/data/' . $row['folder_name'] . $row['file_name'], 'frequency' => $row['data_frequency'], 'sample_rate' => $row['data_sample_rate'], 'bandwidth' => $row['data_bandwidth'], 'start_time' => $row['data_start_time'], 'end_time' => $row['data_end_time'], 'antennas' => $row['data_antennas'], 'data_pols' => $row['data_pols']);
						
					}
					
				}
			
			}
			
			//Encode to json
			echo json_encode($image);
			
		break;
		
	}
	
} elseif($_POST['using_post'] == 'true') {
	
	//Determine the request
	switch($_POST['function']) {
		
		# Accepts the users response to an image
		case 'send_image_response':
		
			//Check image_id is associated with an image
			if(mysql_num_rows(mysql_query("select `image_id` from image_base where image_id='" . mysql_real_escape_string($_POST['image_id']) . "' limit 0, 1")) == 0) {
				
				//No image was found, return error
				echo 'false';
				exit;
				
			}
			
			//Update the image database to reflect a response
			mysql_query("update image_base set total_responses=total_responses + 1 where image_id='" . mysql_real_escape_string($_POST['image_id']) . "'");
			
			//Set the display code
			if($_POST['response'] == 1) {
				
				mysql_query("update image_base set display_code=display_code - 1 where image_id='" . mysql_real_escape_string($_POST['image_id']) . "'");
				
			} elseif($_POST['response'] == 0) {
				
				mysql_query("update image_base set display_code=display_code + 1 where image_id='" . mysql_real_escape_string($_POST['image_id']) . "'");
				
			}
			
			
			//Get the user_id for the api user
			$res = mysql_query("select `user_id`, `public_key`, `private_key` from user_base where public_key='" . mysql_real_escape_string($_GET['public_key']) . "' and private_key='" . mysql_real_escape_string($_GET['private_key']) . "' limit 0, 1");
			while($row = mysql_fetch_array($res)) {
				
				//Insert the response into the database
				mysql_query("insert into image_response (`image_id`, `user_id`, `session_key`, `response`, `stamp_added`) values ('" . mysql_real_escape_string($_POST['image_id']) . "', '" . $row['user_id'] . "', '" . mysql_real_escape_string($_GET['session_key']) . "', '" . mysql_real_escape_string($_POST['response']) . "', '" . time() . "')");
			}
			
			echo 'true';
				
		break;
		
	}
	
}
?>
