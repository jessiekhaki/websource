from hyde.plugin import Plugin
from hyde.ext.plugins.meta import Metadata, MetaPlugin
from jinja2 import environmentfilter, Environment
import math
    

def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__)

def classify(vector,n=5):
    """rank vector and then return n-tiles"""
    ranks = rank_simple(rank_simple(vector))
    nr = len(vector)
    return [(x,int(math.floor(x / (nr/float(n))))) for x in ranks]


class SupertagsPlugin(MetaPlugin):
    
    def __init__(self,site):
        super(SupertagsPlugin, self).__init__(site)
    
    def template_loaded(self, template):
        super(SupertagsPlugin, self).template_loaded(template)
        # self.template.env.filters.update(filters)

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
                if hasattr(resource.meta,"tags"):
                    pass
                    #print "got tags ",str(resource)
        counts = []
        for k,v in self.site.tagger.tags:
            v.set_expando("count", len(v.resources))
            counts.append(len(v.resources))
        classes = classify(counts)
        for i,kv in enumerate(self.site.tagger.tags):
            v = kv[1]
            # print "%12s\t%d\t%d\t%d" % (kv[0],classes[i][0],classes[i][1], counts[i])
            v.set_expando("klass",classes[i][1])
            v.set_expando("rank",classes[i][0])
        self.site.tagger.tagdict = self.site.tagger.tags.to_dict()
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

