def validateFile(filename:str, filesize: int):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {"jpg", "jpeg", "png"} and filesize<10_485_760