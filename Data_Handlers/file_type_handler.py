

def file_type_handler(filename):
    
    if "일별" in filename.lower():
        return "type_1"
    
    elif "월별" in filename.lower():
        return "type_2"
    
    else:
        e = "No file type found in file_type_handler"
        return e
