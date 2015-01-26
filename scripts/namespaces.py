from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, ClosedNamespace

#data
D = Namespace('http://vivo.brown.edu/individual/')

#standard
OWL = Namespace('http://www.w3.org/2002/07/owl#')
RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')

#VIVO
FOAF = Namespace('http://xmlns.com/foaf/0.1/')
SKOS = Namespace('http://www.w3.org/2004/02/skos/core#')
VIVO = Namespace('http://vivoweb.org/ontology/core#')
VITRO = Namespace('http://vitro.mannlib.cornell.edu/ns/vitro/0.7#')
#Not sure how this is different.
VITROROLE = Namespace('http://vitro.mannlib.cornell.edu/ns/vitro/role#')

#Local
BCITE = Namespace('http://vivo.brown.edu/ontology/citation#')
BDISPLAY = Namespace('http://vivo.brown.edu/ontology/display#')
BLOCAL = Namespace('http://vivo.brown.edu/ontology/vivo-brown/')


namespaces = {}
for k, o in vars().items():
    if isinstance(o, (Namespace, ClosedNamespace)):
        namespaces[k] = o

ns_mgr = NamespaceManager(Graph())
for k, v in namespaces.items():
    ns_mgr.bind(k.lower(), v)

rq_prefixes = u"\n".join("prefix %s: <%s>" % (k.lower(), v)
                         for k, v in namespaces.items())

prefixes = u"\n    ".join("%s: %s" % (k.lower(), v)
                          for k, v in namespaces.items()
                          if k not in u'RDF RDFS OWL XSD')