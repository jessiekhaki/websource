from hyde.plugin import Plugin
from jinja2 import environmentfilter, Environment

from datetime import datetime

@environmentfilter
def todateformat(env, value, verbose=False):
    return value.strftime("%d %B %Y %H:%M")

def todatetime(value):
    try:
        when = datetime.strptime(value,"%Y-%m-%d %H:%M")
    except:
        try:
            when = datetime.strptime(value,"%Y-%m-%d")
        except:
            raise ValueError
   
    return when
    

filters={
    'todateformat': todateformat
}

class DepartmentPlugin(Plugin):
    
    def __init__(self,site):
        super(DepartmentPlugin, self).__init__(site)
    
    def template_loaded(self, template):
        super(DepartmentPlugin, self).template_loaded(template)
        self.template.env.filters.update(filters)

    def begin_site(self):
        pass

    def site_complete(self):
        pass

    def begin_node(self, node):
        pass

    def node_complete(self, node):
        pass
    
    def begin_text_resource(self, resource, text):
        if hasattr(resource.meta,"start"):
            resource.meta.startdate=todatetime(resource.meta.start)
        if hasattr(resource.meta,"end"):
            resource.meta.enddate=todatetime(resource.meta.end)


    # def text_resource_complete(self, resource, text):
    #     print "complete ",resource, text)

    # @property
    # def plugin_name(self):
    #     """The name of the plugin, obivously."""
    #     return "department"

