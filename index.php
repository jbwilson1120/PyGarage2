<?php
echo 'Hello World!';
echo '</br>';
echo '</br>Loading config...';
require_once 'config.php';      //Main settings
echo '</br>' + $NUMBER_OF_DOORS;
echo '</br>Loading pinconfig...';
require_once 'pinconfig.php';   //Pin mapping
echo '</br>Loading class GarageDoor...';
require_once 'GarageDoor.php';  //Main Garage Door class

// Initialize the doors
echo 'initializing garage doors...';
$door1 = new GarageDoor(1, 'Left Door', $DOOR1_OPEN_SENSOR, $DOOR1_CLOSED_SENSOR, $DOOR1_BUTTON);
$door2 = new GarageDoor(2, 'Right Door', $DOOR2_OPEN_SENSOR, $DOOR2_CLOSED_SENSOR, $DOOR2_BUTTON);
echo '</br>';
echo $door1->name + ': [STATUS TBD]';
echo '</br>';
echo $door2->name + ': [STATUS TBD]';