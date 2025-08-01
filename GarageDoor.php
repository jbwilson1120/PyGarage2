<?php
use PiPHP\GPIO\GPIO;

/**
 * GarageDoor - Represents a garage door.
 *
 * GarageDoor description.
 *
 * @version 1.0
 * @author jbwil
 */
require_once dirname(__FILE__) . '/piPHP_GPIO/GPIO.php';
require_once dirname(__FILE__) . '/piPHP_GPIO/Pin/PinInterface.php';

class GarageDoor
{
    // Prperties
    public $id = '';
    public $name = '';
    public $pin_Open_Sensor = 0;
    public $pin_Closed_Sensor = 0;
    public $pin_Button = 0;

    // GPIO Interface
    private $gpio;
    private $OpenSensor;
    private $ClosedSensor;
    private $Button;
    
    public function __construct($id, $name, $pin_Open_Sensor, $pin_Closed_Sensor,$pin_Button){
        $this->gpio = new GPIO;
        $this->id = $id;
        $this->name = $name;
        $this->pin_Open_Sensor = $pin_Open_Sensor;
        $this->pin_Closed_Sensor = $pin_Closed_Sensor;
        $this->pin_Button =$pin_Button;
        // Bind GPIO pins to objects
        $this->OpenSensor = $this->gpio->getInputPin($this->pin_Open_Sensor);
        $this->ClosedSensor = $this->gpio->getInputPin($this->pin_Closed_Sensor);
        $this->Button = $this->gpio->getOutputPin($this->pin_Button);
    }

    public function PushButton(){
        $this->Button->setValue(1);
        sleep(0.5); // Wait for 1/2 second
        $this->Button->setValue(0);
    }

    public function GetState(){
        if ($this->OpenSensor->getValue() == 1){
            return 'Open';
        } elseif ($this->ClosedSensor->getValue() == 1){
            return 'Closed';
        } else {
            return 'Unknown';
        }
    }
    public function GetStateImage()
    {
        $state = $this->GetState();
        switch ($state) {
            case 'Open':
                return 'GarageRed.gif';
            case 'Closed':
                return 'GarageGreen.gif';
            default:
                return 'GarageQuestion.gif';
        }
    }
}