<?php
/*
/* SETI RESTful Api
/* http://setiquest.org/
*/
include_once('config/config.php');
class SETI {
	
	# Contructor connects user to the REST api
	public function __construct($public_key, $private_key) {
		
		$this->public_key = $public_key;
		$this->private_key = $private_key;
		$this->session_key = $this->get_session_key();
		
		//Check if credentials are not valid
		if(!$this->validate_credentials()) {
			
			$this->throw_error(3, 'Your API or session key is not valid.');
			return false;
			
		} else {
			
			return true;
			
		}
		
	}
	
	# Gets a session key for the api, either from the PHP session or by requesting a new one
	public function get_session_key() {
		
		//Check if the PHP session has a key
		@session_start();
		if(!empty($_SESSION['seti_session_key'])) {
			
			return $_SESSION['seti_session_key'];
			
		} else {
			
			//Request a new session key from the server
			$_SESSION['seti_session_key'] = $this->send_request('get', 'new_session_key', 1);
			return $_SESSION['seti_session_key'];
			
		}
		
	}
	
	# Validates the clients credentials
	public function validate_credentials($public_key = NULL, $private_key = NULL) {
		
		//Check if alternate credentials have been given
		if(isset($public_key, $private_key)) {
			
			$this->public_key = $public_key;
			$this->private_key = $private_key;
			
		}
		
		if(substr($this->send_request(), 0, 22) == 'HTTP/1.1 403 Forbidden') {
			
			return false;
			
		} else {
			
			return true;
			
		}
		
	}
	
	# Get the status of the servers
	public function get_server_status() {
		
		return json_decode($this->send_request('get', 'server_status', 1));
		
	}
	
	# Get images and their details
	public function get_image($number, $image_id = NULL) {
		
		$this->number = $number;
		$this->image_id = $image_id;
		
		if(isset($this->image_id)) {
			
			$this->data = 'image/' . $this->number . '/' . $this->image_id;
			
		} else {
			
			$this->data = 'image/' . $this->number;
			
		}
		
		//Check for errors
		$this->image_data = get_object_vars(json_decode($this->send_request('get', $this->data, 1)));
		if(isset($this->image_data['error'])) {
			
			$this->throw_error(1, $this->image_data['error']);
			return false;
			
		} else {
			
			return $this->image_data;
			
		}
		
	}
	
	# Send a response concerning an image (response should be set to 'true' = the image contains an anomaly or 'false' = nothing of interest
	public function send_image_response($image_ids, $response) {
                $image_id_array = split(":", $image_ids);
		$this->response = $response;
                
                foreach ($image_id_array as $image_id) {
		
		  $this->image_id = $image_id;
		
		  //Build post
		  $this->POST_array = array('using_post' => 'true', 'function' => 'send_image_response', 'image_id' => $this->image_id, 'response' => $this->response);
		
		  //Send request
		  if($this->send_request('post', $this->POST_array, 1) == 'true') {
			
			//return true;
			
		  } else {
			
			return false;
			
		  }
                }
		
	}
	
	# Sends a request to the api. $content selects what data to return: 1 = body only, 2 = headers and body
	public function send_request($verb = 'get', $data = '', $content = 2) {
                global $config;
		
		$this->verb = $verb;
		$this->data = $data;
		$this->content = $content;
		
		$this->curl_handle = curl_init();
		curl_setopt($this->curl_handle, CURLOPT_TIMEOUT, 10);  
		curl_setopt($this->curl_handle, CURLOPT_RETURNTRANSFER, true);
		
		//Check what data should be returned
		if($this->content == 1) {
			
			curl_setopt($this->curl_handle, CURLOPT_HEADER, false);
			
		} elseif($this->content == 2) {
			
			curl_setopt($this->curl_handle, CURLOPT_HEADER, true);
			
		}
		
		//Determine GET verb
		if($this->verb == 'get') {
			
			//Build the get var
			$this->get_var = '&data=' . $this->data;
			
		} else {
			
			$this->get_var = '';
			
		}
		
		//Determine POST verb
		if($this->verb == 'post') {
			
			curl_setopt($this->curl_handle, CURLOPT_POST, true);
			curl_setopt($this->curl_handle, CURLOPT_POSTFIELDS, array_merge($this->data, array('using_post' => 'true')));
			
		}
		
		//Determine if session_key has been set
		if(!empty($this->session_key)) {
			
			$this->session_var = '&session_key=' . $this->session_key;
			
		} else {
			
			$this->session_var = '';
			
		}
		
		curl_setopt($this->curl_handle, CURLOPT_URL,  $config['server'] . '/api.php?public_key=' . $this->public_key . '&private_key=' . $this->private_key . $this->session_var . $this->get_var);
		
		//Send request
		return curl_exec($this->curl_handle);
		curl_close($this->curl_handle);
		
	}
	
	# Displays a notice, warning or error from the SETI API
	public function throw_error($status, $information) {
		
		$this->status = $status;
		$this->information = $information;
		$this->output = '<strong>SETI ';
		
		//Compile status
		if($this->status == 1) {
			
			$this->output.= 'Notice';
			
		} elseif($this->status == 2) {
			
			$this->output.= 'Warning';
			
		} elseif($this->status == 3) {
			
			$this->output.= 'Error';
			
		}
		
		//Compile information
		echo $this->output.= '</strong>: ' . $this->information . '<br />';
		
	}
	
}
?>
