    
pad = function(v){
    if(v<9){
	return "0"+v;
    }else{
	return ""+v;
    };
};

templates = {
    eventList: $('<div class="eventlist">'),
    eventItem: $('<div class="event"><h3 class="summary"><a href=""></a></h3><div class="start"><span class="when"/><span class="where"/></div><div class="description"></div></div>'),
    upcomingBox: $('<div class="upcoming"><h4>Coming Next...</h4></div>'),
    upcomingItem: $('<div class="event"><h6 class="when"/><h5 class="summary"><a href=""></a></h5><p class="description"></p><h6 class="where"/></div>')
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

getN = function(n, root, wrapper, item){
    var r = root;
    var now = new Date().toISOString();
    var URL = "https://www.googleapis.com/calendar/v3/calendars/e8j7bjqajiblsstfcc59iimss0%40group.calendar.google.com/events?callback=?&maxResults="+n+"&timeMin="+now+"&orderBy=startTime&singleEvents=true&key="+api;
    $.getJSON(URL , function(json) {
	var events = json.items;
	var list = templates[wrapper].clone();
	$.each(events, function(){
	    var e = templates[item].clone();
	    var when = getWhen(this);
	    var where;
	    if(this.location){
		where = " ("+this.location+")";
	    }else{
		where = "";
	    };
	    e.find("a").text(this.summary).attr("href",this.htmlLink).end()
		.find(".when").text(when).end()
		.find(".where").text(where).end()
		.find(".description").text(this.description);
	    list.append(e);
	});
	$(r).append(list);
	// get event.object[0].summary, htmlLink,start.dateTime
	
    }
	     );
};




