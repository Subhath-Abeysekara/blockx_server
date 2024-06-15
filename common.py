def format_doc(document):
    id_ = document['_id']
    del document['_id']
    document['id'] = str(id_)
    return document

def format_docs(documents):
    return list(map(lambda document: format_doc(document), documents))