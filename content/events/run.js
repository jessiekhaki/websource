    
pad = function(v){
    if(v<9){
	return "0"+v;
    }else{
	return ""+v;
    };
};

templates = {
    eventList: $('<div class="eventlist">'),
    eventItem: $('<div class="event"><h3 class="summary"><a href=""></a></h3><div class="start"/><div class="description"></div></div>')
};

getWhen = function(v){
    starter=v.start;
    if(starter.date){
	var startString = new Date(starter.date).toDateString();
	var endString = new Date(v.end.date).toDateString();
	if(startString != endString){
	    when = startString + " - " + endString;
	}else{
	    when = startString;
	};
    }else{
	var when = new Date(starter.dateTime);
	when = when.toDateString() + " " + when.getHours() + ":" + pad(when.getMinutes());
    };
    return when;
};

now = new Date().toISOString();

api="AIzaSyAB1Jd-Jf3U-R84BJzJAPTIYZZmM1sqtjs";

getN = function(n, root){
    var r = root;
    var now = new Date().toISOString();
    var URL = "https://www.googleapis.com/calendar/v3/calendars/e8j7bjqajiblsstfcc59iimss0%40group.calendar.google.com/events?callback=?&maxResults="+n+"&timeMin="+now+"&orderBy=startTime&singleEvents=true&key="+api;
    $.getJSON(URL , function(json) {
	var events = json.items;
	var list = templates.eventList.clone();
	$.each(events, function(){
	    var e = templates.eventItem.clone();
	    var when = getWhen(this);
	    var where;
	    if(this.location){
		where = " ("+this.location+")";
	    }else{
		where = "";
	    };
	    e.find("a").text(this.summary).attr("href",this.htmlLink).end()
		.find(".start").text(when+where).end()
		.find(".description").text(this.description);
	    list.append(e);
	});
	$(r).append(list);
	// get event.object[0].summary, htmlLink,start.dateTime
	
    }
	     );
};




