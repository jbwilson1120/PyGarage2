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
        $o .= '<table><tr><th>File</th><th>Line</th><th>Class</th><th>Function</th></tr>';
        foreach ($trace as $t) {
            $o .= '<tr>';
            $o .= '<td>' . $t['file'] . '</td>';
            $o .= '<td>' . $t['line'] . '</td>';
            $o .= '<td>' . $t['class'] . '</td>';
            $o .= '<td>' . $t['function'] . '</td>';
            //$o .= '<b>Args:</b> ' . $t['args'];
            $o .= '</tr>';
        }
        $o .= '</table>';
        return $o;
    }

}