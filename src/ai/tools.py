from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig #To pass the user as an argument because it is not a good practice to do it normally so we'll use config.
from documents.models import Document

@tool
def list_documents(config:RunnableConfig):
    """ GET DOCUMENTS FOR THE CURRENT USER."""
    print(config)
    configurable =config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    qs = Document.objects.filter(active =True)
    response_data=[]
    # serialize our django data into python dicts
    for obj in qs:
        response_data.append(
            {
                "id":obj.id ,
                "title":obj.title
            }
        )
    return response_data

@tool
def get_document(document_id:int, config:RunnableConfig):
    """ GET THE DETAILS OF A DOCUMENT FOR THE CURRENT USER."""
    configurable =config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    try:
        obj = Document.objects.get(id=document_id, owner_id=user_id ,active=True)
    except Document.DoesNotExist:
        raise Exception("Document not found, try again!")
    response_data={
        "id":obj.id,
        "title":obj.title,
        "content":obj.content,
        "created_at":obj.created_at,
    }
    return response_data


@tool
def create_document(title:str,content:str,config:RunnableConfig):
    """ 
    Create a new document to store for the user.

    Arguments are:
    title: string max characters of 120
    content: long form text in many paragraphs or pages
    """
    configurable =config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    obj = Document.objects.create(title=title,content=content, owner_id=user_id ,active=True)
    response_data={
        "id":obj.id,
        "title":obj.title,
        "content":obj.content,
        "created_at":obj.created_at,
    }
    return response_data

@tool
def update_document(document_id:int,title:str=None,content:str=None, config:RunnableConfig=None):
    """ 
    
    Update a document for the user by the document id and related arguments.

    Arguments are:
    document_id:id of the document(required)
    title: string max characters of 120(optional)
    content: long form text in many paragraphs or pages(optional)
    """
    configurable = config.get("configurable") or config.get("metadata")
    user_id = configurable.get("user_id")

    try:
        obj = Document.objects.get(
            id=document_id,
            owner_id=user_id,
            active=True
        )
    except Document.DoesNotExist:
        raise Exception("Document not found, try again!")

    if title is not None:
        obj.title = title
    if content is not None:
        obj.content = content
    

    obj.save()

    return {
        "id": obj.id,
        "title": obj.title,
        "content": obj.content,
        "created_at": obj.created_at,
    }


@tool
def delete_document(document_id:int, config:RunnableConfig):
    """
    Delete the document for the current user by document_id
    """
    configurable = config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    # if user_id is None:
        # raise Exception("Invalid request for user.")
    # has_perms = async_to_sync(permit.check)(f"{user_id}", "delete", "document")
    # if not has_perms:
        # raise Exception("You do not have permission to delete individual documents.")
    try:
        obj = Document.objects.get(id=document_id, active=True)
    except Document.DoesNotExist:
        raise Exception("Document not found, try again")
    except:
        raise Exception("Invalid request for a document detail, try again")
    
    # has_object_perms = async_to_sync(permit.check)(f"{user_id}", "delete", f"document:{obj.id}")
    # if not has_object_perms:
    #     raise Exception("You do not have permission to delete individual documents.")
    obj.delete()
    response_data =  {"message": "success"}
    return response_data

document_tools =[      #Tools ki list
    list_documents,
    get_document,
    create_document,
    delete_document,
    update_document,
]