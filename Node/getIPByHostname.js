const os = require('os');

var ut_sec = os.uptime();
var ut_min = ut_sec/60;
var ut_hour = ut_min/60;
var ut_day = ut_hour/24;
   
ut_sec = Math.floor(ut_sec);
ut_min = Math.floor(ut_min);
ut_hour = Math.floor(ut_hour);
ut_day = Math.floor(ut_day);
 
 
ut_day = ut_day%24; 
ut_hour = ut_hour%60;
ut_min = ut_min%60;
ut_sec = ut_sec%60;
  
console.log("Up time: " 
        + ut_day + " Days(s) "
        + ut_hour + " Hour(s) " 
        + ut_min + " minute(s) and " 
        + ut_sec + " second(s)");