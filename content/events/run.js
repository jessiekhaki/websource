$(document).ready(function() {

  function jQuery21101801362546152825_1417645059321(){
  var x=1;
  };

    var now = new Date().toISOString();
    
    var api="AIzaSyAB1Jd-Jf3U-R84BJzJAPTIYZZmM1sqtjs";
    var getOne = "https://www.googleapis.com/calendar/v3/calendars/e8j7bjqajiblsstfcc59iimss0%40group.calendar.google.com/events?callback=?&maxResults=1&timeMin="+now+"&orderBy=startTime&singleEvents=true&key="+api;

  var url="https://www.googleapis.com/calendar/v3/calendars/e8j7bjqajiblsstfcc59iimss0@group.calendar.google.com/events?callback=?&key=AIzaSyAB1Jd-Jf3U-R84BJzJAPTIYZZmM1sqtjs&timeMin=2014-11-29T00%3A00%3A00%2B00%3A00&timeMax=2015-01-12T00%3A00%3A00%2B00%3A00&singleEvents=true&maxResults=9999&_=1417645059322";


    $.getJSON(getOne , function(json) {
	var event = json.items[0];
        }
	     );
});
