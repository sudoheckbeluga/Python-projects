import os

directory = input()
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]

types = {
    "text_files": ['.txt', '.md', '.rtf', '.tex'],
    "document_files": ['.doc', '.docx', '.pdf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "image_files": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.svg'],
    "audio_files": ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    "video_files": ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv'],
    "compressed_files": ['.zip', '.rar', '.7z', '.tar', '.gz'],
    "executable_files": ['.exe', '.bat', '.sh', '.bin', '.apk'],
    "system_files": ['.dll', '.sys', '.ini', '.log'],
    "programming_files": ['.py', '.java', '.c', '.cpp', '.js', '.html', '.css'],
    "database_files": ['.sql', '.db', '.mdb', '.sqlite']
}

for f in files:
    ext=f.split(".")[-1]
    ext="."+ext
    for type, extn in types.items():
        if(ext in extn):
            new_path = os.path.join(directory,type)+'/'
            os.system("mkdir -p "+new_path+" && mv "+os.path.join(directory,f)+" "+new_path)
