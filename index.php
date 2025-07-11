<?php
ini_set('display_errors', '1');
echo 'Hello World 2!';
echo '</br>';
require_once dirname(__FILE__) . '/config.php';      //Main settings
require_once dirname(__FILE__) . '/pinconfig.php';   //Pin mapping
require_once dirname(__FILE__) . '/GarageDoor.php';  //Main Garage Door class
require_once dirname(__FILE__) . '/piPHP_GPIO/GPIO.php';
require_once dirname(__FILE__) . '/piPHP_GPIO/Pin/PinInterface.php';

// Initialize the doors
echo 'initializing garage doors...';
$door1 = new GarageDoor(1, 'Left Door', $DOOR1_OPEN_SENSOR, $DOOR1_CLOSED_SENSOR, $DOOR1_BUTTON);
$door2 = new GarageDoor(2, 'Right Door', $DOOR2_OPEN_SENSOR, $DOOR2_CLOSED_SENSOR, $DOOR2_BUTTON);
echo '</br>';
echo $door1->name . ': [STATUS TBD]';
echo '</br>';
echo $door2->name . ': [STATUS TBD]';