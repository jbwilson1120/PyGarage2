<?php
ini_set('display_errors', '1');
require_once dirname(__FILE__) . '/config.php';      //Main settings
require_once dirname(__FILE__) . '/pinconfig.php';   //Pin mapping
require_once dirname(__FILE__) . '/GarageDoor.php';  //Main Garage Door class
require_once dirname(__FILE__) . '/Util.php';
require_once dirname(__FILE__) . '/piPHP_GPIO/GPIO.php';
require_once dirname(__FILE__) . '/piPHP_GPIO/Pin/PinInterface.php';
// Initialize the doors
$u = new Util();
try {
    $door1 = new GarageDoor(1, 'Left Door', $DOOR1_OPEN_SENSOR, $DOOR1_CLOSED_SENSOR, $DOOR1_BUTTON);
    $door2 = new GarageDoor(2, 'Right Door', $DOOR2_OPEN_SENSOR, $DOOR2_CLOSED_SENSOR, $DOOR2_BUTTON);
} catch (Exception $e) {
    echo '</br></br>Oops! We had a problem initializing the garage doors: </br></br>' . $e->getMessage() . "</br>";
    echo 'STACK TRACE: </br></br>' . $u->HTMLFormatTrace($e->getTrace());
    phpinfo();
    exit;
}