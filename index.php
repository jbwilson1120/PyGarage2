<?php
/** Garage Door Status Page
 * Displays the status of garage doors using GPIO pins
 *
 * @version 1.0
 * @author jbwil
 */

// Initialize the doors
require_once dirname(__FILE__) . '/InitDoors.php';

$tags['doorstatussize'] = '50';

$tags['D1Name'] = $door1->name;
$tags['door1visable'] = 'inline';
$tags['door1status'] = $door1->GetStateImage();

$tags['D2Name'] = $door2->name;
$tags['door2visable'] = 'inline';
$tags['door2status'] = $door2->GetStateImage();

$htmlbody = $u->HTMLTemplate("doorstatus.txt", $tags);
echo($htmlbody);