

def file_type_handler(filename):
    
    if "일별" in filename:
        return "type_1"
    
    elif "월별" in filename:
        return "type_2"
    
    elif "서비스 현황" in filename:
        return "type_3"
    else:
        e = "No file type found in file_type_handler"
        return e
