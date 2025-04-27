<?php

/**
 * GarageDoor - Represents a garage door.
 *
 * GarageDoor description.
 *
 * @version 1.0
 * @author jbwil
 */
class GarageDoor
{
    // Prperties
    public $id = '';
    public $name = '';
    public $state = '';
    public $Pin_Open_Sensor = 0;
    public $pin_Closed_Sensor = 0;
    public $pin_Button = 0;
    
    public function __construct($id, $name, $state, $pin_Open_Sensor, $pin_Closed_Sensor,$pin_Button){
        $this->id = $id;
        $this->name = $name;
        $this->state = $state;
        $this->pin_Open_Sensor = $pin_Open_Sensor;
        $this->pin_Closed_Sensor = $pin_Closed_Sensor;
        $this->pin_Button =$pin_Button;
    }

    public function PushButton(){
        
    }

    public function GetState(){
        
        return $this->state;
    }
}