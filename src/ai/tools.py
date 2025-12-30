from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig #To pass the user as an argument because it is not a good practice to do it normally so we'll use config.
from documents.models import Document

@tool
def list_documents():
    """ GET DOCUMENTS FOR THE CURRENT USER."""

    qs = Document.objects.filter(active =True)
    response_data=[]
    # serialize our django data into python dicts
    for obj in qs:
        response_data.append(
            {
                "id":id ,
                "title":obj.title
            }
        )
    return response_data

@tool
def get_document(document_id:int):
    """ GET THE DETAILS OF A DOCUMENT FOR THE CURRENT USER."""

    obj = Document.objects.get(id=document_id, active=True)
    response_data={
        "id":obj.id,
        "title":obj.title
    }
    return response_data
