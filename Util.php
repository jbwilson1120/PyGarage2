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
        /**
         * Formats the stack trace into an HTML table.
         * 
         * @param array $trace The stack trace array.
         * @return string The formatted HTML table.
         */
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
    public function HTMLTemplate($template, $tags) {
        /**
         * Loads the given template and replaces the tags with the values provided in the $tags array.
         * 
         * $tags is an associative array of tags pairs to replace in the template. Tag pair should be in the format of
         * (tagname, tagvalue) with both being strings. Tag names should be enclosed in curly braces, e.g. {{ tagname }}.
         * 
         */

        print ($tags);

        $html = file_get_contents(require_once dirname(__FILE__) . '/templates/' . $template);
        foreach ($tags as $tag => $value) {
            $html = str_replace('{{ ' . $tag . ' }}', $value, $html);
        }
        return $html;
    }
}