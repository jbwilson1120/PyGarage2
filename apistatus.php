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

// Initialize the response array
$response = [];

// Check the state of the target door and add it to the response
$door = $_GET["door"];
switch ($door) {
    case 'door1':
        $response['doors'] = ['door' => $door1->name, 'status' => $door1->GetState()];
        break;
    case 'door2':
        $response['doors'] = ['door' => $door2->name, 'status' => $door2->GetState()];
        break;
    default:
        $response['doors'] = [['door' => $door1->name, 'status' => $door1->GetState()], ['door' => $door2->name, 'status' => $door2->GetState()]];
}


// Set the content type to JSON
header('Content-Type: application/json');

// return the response as JSON
echo json_encode($response, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);