from hyde.plugin import Plugin

print "imported"

class DepartmentPlugin(Plugin):
    
    def __init__(self,site):
        super(DepartmentPlugin, self).__init__(site)
        #print "Dept init"
    
    def begin_site(self):
         self.logger.info( "Department plugin" )

    def site_complete(self):
        self.logger.info("dept site complete")

    def begin_node(self, node):
        self.logger.info("dept begin node %s"  % str(node))

    def node_complete(self, node):
        pass
    
    def begin_text_resource(self, resource, text):
         print "begin %s %s " % (resource, text)

    # def text_resource_complete(self, resource, text):
    #     print "complete ",resource, text)

    # @property
    # def plugin_name(self):
    #     """The name of the plugin, obivously."""
    #     return "department"

