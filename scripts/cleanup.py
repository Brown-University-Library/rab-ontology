"""
Read in an ontology file and reserialize only with relevant
namespaces.
"""


import glob
import os
import sys

from rdflib import ConjunctiveGraph, Graph
from rdflib.namespace import Namespace, NamespaceManager

namespace_rq = """
ASK
{
    { ?ns ?p ?o }
    UNION
    { ?s ?ns ?o }
    UNION
    { ?s ?p ?ns }
    FILTER(STRSTARTS(STR(?ns), "--ns--"))
}
"""

def get_file_list(path, extension='ttl'):
    out = []
    pattern = os.path.join(path, '*{}'.format(extension))
    for ofile in glob.glob(pattern):
        out.append(ofile)
    return out

def get_prefix(graph, uri):
    prefix, uri, prop = graph.compute_qname(uri)
    return (prefix, uri)


def new_namespace_manager(g):
    """
    Return a new namespace manager based
    on the namespaces actually used in the ontology
    file.
    """
    new_ns_mgr = NamespaceManager(Graph())
    for pre, ns in g.namespaces():
        q = namespace_rq.replace('--ns--', ns.toPython())
        used = g.query(q).askAnswer
        if used is True:
            new_ns_mgr.bind(pre, Namespace(ns))
    return new_ns_mgr


def list_used_namespaces():
    """
    Print Python code as strings
    that can be used to setup namespaces.
    """
    g = ConjunctiveGraph()
    flist = get_file_list(sys.argv[1])
    for full in flist:
        g.parse(source=full, format='turtle')
    ns_mgr = NamespaceManager(Graph())
    for pre, ns in g.namespaces():
        q = namespace_rq.replace('--ns--', ns.toPython())
        used = g.query(q).askAnswer
        if used is True:
            #print pre, ns
            print "{} = Namespace('{}')".format(pre.upper(), ns)
            ns_mgr.bind(pre, Namespace(ns))
    return ns_mgr


def base_file_name(full):
    """
    Return the base filename with prefix.
    """
    return full.split(os.sep)[-1]


def reserialize():
    """
    Reserialize as turtle with only applicable
    namespace declarations.
    """
    from namespaces import ns_mgr
    for ont_file in get_file_list(sys.argv[1]):
        print>>sys.stderr, "Processing:", ont_file
        g = Graph()
        g.parse(location=ont_file, format='turtle')
        #Use the standard set of ontologies.
        g.namespace_manager = ns_mgr
        nns = new_namespace_manager(g)
        g.namespace_manager = nns
        new_filename = base_file_name(ont_file)
        g.serialize(destination=sys.argv[2].strip('/') + '/' + new_filename, format='turtle')

if __name__ == "__main__":
    reserialize()

