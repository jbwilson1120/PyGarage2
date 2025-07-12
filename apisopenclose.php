<?php
/** API endpoint for GarageDoor opening or closing
 *
 * Opens/closes the specified door and returns the status afterward
 * 
 * @version 1.0
 * @author jbwil
 */

// Initialize the doors
require_once dirname(__FILE__) . '/InitDoors.php';

// Initialize the response array
$response = [];

// Check the state of the target door and add it to the response
if(isset($_GET['door'])) {
    $door = $_GET['door'];
} else {
    $response['error'] = 'No door specified - use parameter \'door\'';
}

switch ($door) {
    case 'door1':
        $door1->PushButton(); // Open/close door1
        $response['doors'] = ['door' => $door1->name, 'status' => $door1->GetState()];
        break;
    case 'door2':
        $door2->PushButton(); // Open/close door2
        $response['doors'] = ['door' => $door2->name, 'status' => $door2->GetState()];
        break;
}


// Set the content type to JSON
header('Content-Type: application/json');

// return the response as JSON
echo json_encode($response, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);