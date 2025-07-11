<?php

/**
 * Util short summary.
 *
 * Util description.
 *
 * @version 1.0
 * @author jbwil
 */
class Util
{
    public function CheckPinState($Pin){
        // Returns the state of a given pin
        if (empty($Pin)) {
            return -1;
        }else{
            
        }
    }
    public function HTMLFormatTrace($trace) {
        $o = '';
        foreach ($trace as $t) {
            $o .= '<b>File:</b> ' . $t['file'] . ' <b>Line:</b> ' . $t['line'] . ' <b>Function:</b> ' . $t['function'] . ' <b>Args:</b> ' . $t['args'] . '<br>';
        }
        return $o;
    }

}