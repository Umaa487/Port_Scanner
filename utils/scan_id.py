import uuid

def generate_uoid():
    
    uoid = uuid.uuid4()
    return str(uoid)


''' unique_id = generate_uoid()
print("Generated UOID:", unique_id) '''
