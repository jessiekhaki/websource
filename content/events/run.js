$(document).ready(function() {

    var templates = {
	eventList: $('<div class="eventlist">'),
	eventItem: $('<div class="event"><div class="summary"><a href=""></a></div><div class="start"/></div>')
    };

    var now = new Date().toISOString();
    
    var api="AIzaSyAB1Jd-Jf3U-R84BJzJAPTIYZZmM1sqtjs";
    var getOne = "https://www.googleapis.com/calendar/v3/calendars/e8j7bjqajiblsstfcc59iimss0%40group.calendar.google.com/events?callback=?&maxResults=4&timeMin="+now+"&orderBy=startTime&singleEvents=true&key="+api;

    $.getJSON(getOne , function(json) {
	var events = json.items;
	var list = templates.eventList.clone();
	$.each(events, function(){
	    var e = templates.eventItem.clone();
	    e.find("a").text(this.summary).attr("href",this.htmlLink);
	    e.find(".start").text(this.start.dateTime).end();
	    list.append(e);
	});
	$("#events").append(list);
	// get event.object[0].summary, htmlLink,start.dateTime
	
    }
	     );
});
