<?php
//
$currentTime = date('h') * 1;;
$message = "Its" . $currentTime . "oclock";
$say = "/home/pi/Scripts/speech.sh"." ".$message;
exec($say);
?>
