from hyde.plugin import Plugin
from hyde.ext.plugins.meta import Metadata, MetaPlugin
from jinja2 import environmentfilter, Environment

from datetime import datetime

import sys
import urllib
import hashlib

def vEvent(resource):
    template = """
BEGIN:VEVENT
UID:{uid}
DTSTART:{dtstart}
DTEND:{dtend}
SUMMARY:{summary}
DESCRIPTION:{description}
END:VEVENT
"""
    vtext = template.format(
        dtstart = resource.meta.startdate.strftime("%Y%m%dT%H%M%S"),
        dtend =  resource.meta.enddate.strftime("%Y%m%dT%H%M%S"),
        uid = hashlib.md5(resource.url).hexdigest()+"@chicas",
        summary = resource.meta.title,
        description = resource.meta.description
        )
    
    return vtext


@environmentfilter
def todateformat(env, value, verbose=False):
    return value.strftime("%d %B %Y %H:%M")

def todatetime(value):
    try:
        when = datetime.strptime(str(value),"%Y-%m-%d %H:%M")
    except:
        try:
            when = datetime.strptime(str(value),"%Y-%m-%d")
        except:
            raise ValueError
   
    return when
    
@environmentfilter
def tovevent(env, value, verbose=False):
    return vEvent(value)

@environmentfilter
def datacalendar(env, value, verbose=False):
    """ return a data-url for the icalendar representation of this resource 
    needs a start and end time """
    template = """
BEGIN VCALENDAR
{0}
END VCALENDAR
"""
    vev = vEvent(value)
    cal_text = template.format(vev)
    base64_data = cal_text.encode("base64").replace("\n", "")
    cal_url = 'data:text/calendar;base64,{0}'.format(base64_data) 
    return cal_url
    
@environmentfilter
def googlecalendar(env, value, verbose=False):
    URL_template="https://www.google.com/calendar/render?action=TEMPLATE&text={0}&details={1}&dates={2}/{3}&location={4}&sf=true&output=xml"
    URL = URL_template.format(urllib.quote_plus(value.meta.title), 
                              urllib.quote_plus(value.meta.description),
                              value.meta.startdate.strftime("%Y%m%dT%H%M%S"),
                              value.meta.enddate.strftime("%Y%m%dT%H%M%S"),
                              urllib.quote_plus(value.meta.location))
    return URL
    
@environmentfilter
def surnamesort(env, value, verbose=False):
    """ sort on last name. Possibly sorting on second name is better 
    when people present with three names but I'm not sure..."""
    def getsur(x):
        return x.meta.title.split()[-1]
    return sorted(value, key=getsur)
@environmentfilter
def lastname(env, value, verbose=False):
    return value.meta.title.split()[-1]
@environmentfilter
def firstnames(env, value, verbose=False):
    return " ".join(value.meta.title.split()[:-1])

filters={
    'todateformat': todateformat,
    'calurl': datacalendar,
    'googleurl': googlecalendar,
    'vevent': tovevent,
    'surnamesort': surnamesort,
    'lastname': lastname,
    'firstnames': firstnames
}

class DepartmentPlugin(MetaPlugin):
    
    def __init__(self,site):
        super(DepartmentPlugin, self).__init__(site)
    
    def template_loaded(self, template):
        super(DepartmentPlugin, self).template_loaded(template)
        self.template.env.filters.update(filters)

    def begin_site(self):
        config = self.site.config
        metadata = config.meta if hasattr(config, 'meta') else {}
        self.site.meta = Metadata(metadata)
        self.nodemeta = 'nodemeta.yaml'
        if hasattr(self.site.meta, 'nodemeta'):
            self.nodemeta = self.site.meta.nodemeta
        for node in self.site.content.walk():
            self.__read_node__(node)
            for resource in node.resources:
                if not hasattr(resource, 'meta'):
                    resource.meta = Metadata({}, node.meta)
                if resource.source_file.is_text and not resource.simple_copy:
                    self.__read_resource__(resource, resource.source_file.read_all())
                if hasattr(resource.meta,"start"):
                    #print "setting start for ",str(resource)
                    resource.meta.startdate=todatetime(resource.meta.start)
                if hasattr(resource.meta,"end"):
                    resource.meta.enddate=todatetime(resource.meta.end)
                if hasattr(resource.meta,"release"):
                    #print "release",resource.meta.release
                    resource.meta.releasedate=todatetime(resource.meta.release)

    def site_complete(self):
        pass

    def begin_node(self, node):
        pass

    def node_complete(self, node):
        pass
    
    def begin_text_resource(self, resource, text):
        pass


    # def text_resource_complete(self, resource, text):
    #     print "complete ",resource, text)

    # @property
    # def plugin_name(self):
    #     """The name of the plugin, obivously."""
    #     return "department"

