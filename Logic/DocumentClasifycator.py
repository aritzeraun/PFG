
def selectedDocuments(documentList, typology):

    selected_Documents = []
    if typology == 1:
        for document in documentList:
            if document[2] != 'nan':
                selected_Documents.append(document)
    else:
        for document in documentList:
            if document[2] == 'nan':
                selected_Documents.append(document)
    return selected_Documents
