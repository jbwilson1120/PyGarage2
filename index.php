<?php
ini_set('display_errors', '1');
echo 'Hello World!';
echo '</br>';
echo 'current user: '.get_current_user();
echo '</br>';
require_once dirname(__FILE__) . '/config.php';      //Main settings
require_once dirname(__FILE__) . '/pinconfig.php';   //Pin mapping
require_once dirname(__FILE__) . '/GarageDoor.php';  //Main Garage Door class
require_once dirname(__FILE__) . '/Util.php';
require_once dirname(__FILE__) . '/piPHP_GPIO/GPIO.php';
require_once dirname(__FILE__) . '/piPHP_GPIO/Pin/PinInterface.php';

// Initialize the doors
echo 'initializing garage doors...';
try {
    $door1 = new GarageDoor(1, 'Left Door', $DOOR1_OPEN_SENSOR, $DOOR1_CLOSED_SENSOR, $DOOR1_BUTTON);
    $door2 = new GarageDoor(2, 'Right Door', $DOOR2_OPEN_SENSOR, $DOOR2_CLOSED_SENSOR, $DOOR2_BUTTON);
} catch (Exception $e) {
    echo 'Oops! We had a problem initializing the garage doors: </br></br>' . $e->getMessage() . "</br>";
    $u = new Util();

    echo 'STACK TRACE: </br></br>' . $u->HTMLFormatTrace($e->getTrace());
    phpinfo();
    exit;
}

echo '</br>';
echo $door1->name . ': [' . $door1->GetState() . ']';
echo '</br>';
echo $door2->name . ': [' . $door2->GetState() . ']';