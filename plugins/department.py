from hyde.plugin import Plugin
from jinja2 import environmentfilter, Environment

from datetime import datetime

@environmentfilter
def todateformat(env, value, verbose=False):
    try:
        when = datetime.strptime(value,"%Y-%m-%d %H:%M")
    except:
        try:
            when = datetime.strptime(value,"%Y-%m-%d")
        except:
            raise ValueError
   
    return when.strftime("%d %B %Y")


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
        pass

    # def text_resource_complete(self, resource, text):
    #     print "complete ",resource, text)

    # @property
    # def plugin_name(self):
    #     """The name of the plugin, obivously."""
    #     return "department"

