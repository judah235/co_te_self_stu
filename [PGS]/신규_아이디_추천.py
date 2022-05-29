import re

def solution(new_id):
    new_id=new_id.lower()
    
    new_id=re.sub(r'[^a-z0-9-._]','',new_id)
    
    while '..' in new_id:
        new_id=new_id.replace('..','.')
    
    if new_id.startswith('.'): new_id=new_id[1:]
    if new_id.endswith('.'): new_id=new_id[:-1]
    
    if new_id=='' : new_id='a'
    
    new_id=new_id[:15]
    if new_id.endswith('.'): new_id=new_id[:-1]
    
    if len(new_id)<=2:
        new_id=new_id+new_id[-1]*(3-len(new_id))    
    return new_id