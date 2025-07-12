<?php
ini_set('display_errors', '1');
require_once dirname(__FILE__) . '/config.php';      //Main settings
require_once dirname(__FILE__) . '/pinconfig.php';   //Pin mapping
require_once dirname(__FILE__) . '/GarageDoor.php';  //Main Garage Door class
require_once dirname(__FILE__) . '/Util.php';
require_once dirname(__FILE__) . '/piPHP_GPIO/GPIO.php';
require_once dirname(__FILE__) . '/piPHP_GPIO/Pin/PinInterface.php';

// Initialize the doors
require_once dirname(__FILE__) . '/InitDoors.php';

$tags['doorstatussize'] = '50';

$tags['D1Name'] = $door1->name;
$tags['door1visable'] = 'block';
$tags['door1status'] = $door1->GetStateImage();

$tags['D2Name'] = $door2->name;
$tags['door2visable'] = 'block';
$tags['door2status'] = $door2->GetStateImage();

$htmlbody = $u->HTMLTemplate("doorstatus.txt", $tags);
echo($htmlbody);