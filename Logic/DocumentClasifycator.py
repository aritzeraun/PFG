
def selectedDocuments(documentList):

    selected_Documents = []

    for document in documentList:
        if document[2] != 'nan':
            selected_Documents.append(document)

    return selected_Documents
