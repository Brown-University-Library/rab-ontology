header = '@prefix owl:   <http://www.w3.org/2002/07/owl#> .\n\
@prefix bprofile: <http://vivo.brown.edu/ontology/profile#> .\n\
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .\n\
@prefix afn:   <http://jena.hpl.hp.com/ARQ/function#> .\n\
@prefix blocal: <http://vivo.brown.edu/ontology/vivo-brown/> .\n\
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .\n\
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .\n\
@prefix bcite: <http://vivo.brown.edu/ontology/citation#> .\n\
@prefix vitro: <http://vitro.mannlib.cornell.edu/ns/vitro/0.7#> .\n\
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\
@prefix bdisplay: <http://vivo.brown.edu/ontology/display#> .\n\
@prefix bharvest: <http://vivo.brown.edu/ontology/harvest#> .\n\
@prefix vivo:  <http://vivoweb.org/ontology/core#> .\n\
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .\n\
@prefix dc:    <http://purl.org/dc/elements/1.1/>.\n\
\n\
<http://vivo.brown.edu/ontology/harvest>\ta\t\t\t\t\t\towl:Ontology ;\n\
\t\trdfs:label\t\t\t\t\t"Brown Harvest"@en-US ;\n\
\t\tvitro:ontologyPrefixAnnot\t"bharvest"^^xsd:string .\n\n'

class_tmp = 'bharvest:{0}\ta\towl:Class ;\n\
\t\trdfs:label\t\t\t"{1}"@en-US .\n'

sub_tmp = 'bharvest:{0} rdfs:subClassOf bharvest:{1} .\n'

obj_prps = 'bharvest:hasUser\n\
\t\ta\t\t\towl:ObjectProperty ;\n\
\t\trdfs:domain\tbharvest:HarvestProcess ;\n\
\t\trdfs:label\t"has user"@en-US .\n\n\
bharvest:hasHarvestProcess\n\
\t\ta\t\t\towl:ObjectProperty ;\n\
\t\trdfs:domain\tbharvest:HarvestUser ;\n\
\t\trdfs:label\t"uses process"@en-US .\n\n'

dp_temp = 'bharvest:{0}\ta\t\towl:DatatypeProperty ;\n\
\t\trdfs:domain\t\t\t\tbharvest:HarvestProcess ;\n\
\t\trdfs:label\t\t\t\t"{1}"@en-US ;\n\
\t\trdfs:range\t\t\t\txsd:string .\n'

objs = [
	('HarvestProcess','Harvest Process'),
	('HarvestUser','Harvest User'),
]

subs = [
	('PubMedSearch','PubMed Search', 'HarvestProcess'),	
	('WebOfScienceSearch','Web of Science Search', 'HarvestProcess')
]

params = [
	('accessionNumber','accession number'),
	('address','address'),
	('affiliation','affiliation'),
	('allFields','all fields'),
	('author','author'),
	('authorFirstName','author first name'),
	('authorFullName','author full name'),
	('authorIdentifier','author identifier'),
	('authorLastName','author last name'),
	('book','book'),
	('completionDate','completion date'),
	('conference','conference'),
	('corporateAuthor','corporate author'),
	('createDate','create date'),
	('documentType','document type'),
	('doi','doi'),
	('ecrnNumber','EC/RN number'),
	('editor','editor'),
	('entrezDate','entrez date'),
	('filter','filter'),
	('fundingAgency','funding agency'),
	('grantNumber','grant number'),
	('groupAuthor','group author'),
	('isbn','ISBN'),
	('investigator','investigator'),
	('investigatorFullName','investigator full name'),
	('issue','issue'),
	('journal','journal'),
	('language','language'),
	('locationID','location ID'),
	('meshDate','MeSH date'),
	('meshMajorTopic','MeSH major topic'),
	('meshSubHeading','MeSH subheading'),
	('meshTerms','MeSH terms'),
	('modificationDate','modification date'),
	('organization','organization'),
	('otherTerms','other terms'),
	('pagination','pagination'),
	('pharmacologicalAction','pharmacological action'),
	('publication','publication'),
	('publicationDate','publication date'),
	('publicationType','publication type'),
	('publisher','publisher'),
	('pmid','PubMed ID'),
	('secondarySourceID','secondary source ID'),
	('subjectPersonalName','subject personal name'),
	('supplementaryConcept','supplementary concept'),
	('text','text'),
	('title','title'),
	('titleAbstract','title/abstract'),
	('topic','topic'),
	('transliteratedTitle','transliterated title'),
	('type','type'),
	('volume','volume'),
	('year','year')
	]

def main():
	out = ''

	out += header
	for obj in objs:
		tp = class_tmp.format(obj[0],obj[1])
		out += tp + '\n'
	for sub in subs:
		tp = class_tmp.format(sub[0],sub[1])
		sp = sub_tmp.format(sub[0],sub[2])
		out += tp + sp + '\n'
	out += obj_prps
	for pair in params:
		dtp = dp_temp.format(pair[0],pair[1])
		out += dtp + '\n'

	with open('bharvest.ttl', 'w') as f:
		f.write(out)

if __name__ == '__main__':
	main()