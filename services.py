

def allowed_file(filename):
    ALLOWED_EXTS = ['txt', 'doc', 'docx', 'pdf']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTS
