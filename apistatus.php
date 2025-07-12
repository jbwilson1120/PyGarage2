<?php
/** API endpoint for GarageDoor status checking
 *
 * Returns the status of garage doors using GPIO pins
 * 
 * @version 1.0
 * @author jbwil
 */

// Initialize the doors
require_once dirname(__FILE__) . '/InitDoors.php';

$door = $_GET["door"];
switch ($door) {
    case 'door1':
        $targetdoor = $door1;
    case 'door2':
        $targetdoor = $door2;
    default:

}


// Set the content type to JSON
header('Content-Type: application/json');
// Initialize the response array
$response = [];
// Check the state of the target door and add it to the response
$response['doors'] = ['status' => $targetdoor->GetState()];
// return the response as JSON
echo json_encode($response, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);