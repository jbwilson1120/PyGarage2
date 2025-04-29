<?php
echo 'Hello World!';
require_once 'config.php';      //Main settings
require_once 'pinconfig.php';   //Pin mapping
require_once 'GarageDoor.php';  //Main Garage Door class

// Initialize the doors
$door1 = new GarageDoor(1, 'Left Door', $DOOR1_OPEN_SENSOR, $DOOR1_CLOSED_SENSOR, $DOOR1_BUTTON);
//$door2 = new GarageDoor(2, 'Right Door', $DOOR2_OPEN_SENSOR, $DOOR2_CLOSED_SENSOR, $DOOR2_BUTTON);

echo $door1->name + ': ' + $door1->GetState();