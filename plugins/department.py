from hyde.plugin import Plugin
from hyde.ext.plugins.meta import Metadata, MetaPlugin
from jinja2 import environmentfilter, Environment

from datetime import datetime

import sys

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
    

filters={
    'todateformat': todateformat
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
                    print "setting start for ",str(resource)
                    resource.meta.startdate=todatetime(resource.meta.start)
                if hasattr(resource.meta,"end"):
                    resource.meta.enddate=todatetime(resource.meta.end)
                if hasattr(resource.meta,"release"):
                    print resource.meta.release
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

