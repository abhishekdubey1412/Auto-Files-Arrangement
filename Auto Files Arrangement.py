import os, shutil

dic_extension = {

'audio_extensions' : ('.mp3','.m4a','.wav','.flac','.m3u'),
'video_extensions' : ('.mp4','.mkv','.MKV','.flv','.mpeg','.webm'),
'image_extensions' : ('.jprg', '.jpg', '.png', '.gif', '.webp' ),
'documents_extensions' : ('.doc','.pdf','.txt','.html','.PDF'),

}

folderpath_input = input('Enter Your Folder Path: ')
os.chdir(folderpath_input)

def file_finder(folder_path, folder_extensions):
    return [file for file in os.listdir(folder_path) for extensions in folder_extensions if file.endswith(extensions)]
    # files = []
    # for file in os.listdir(folder_path):
    #     for extensions in folder_extensions:
    #         if file.endswith(extensions):
    #             files.append(file)
    # return files

for extensions_name, extensions_type in dic_extension.items():
    folder_name = extensions_name.split('_')[0]
    folder_path = os.path.join(folderpath_input,folder_name)
    for item in (file_finder(folderpath_input, extensions_type)):
        item_path = os.path.join(folderpath_input,item)
        item_new_path = os.path.join(folder_path,item) 
        if os.path.exists(folder_name):
            shutil.move(item, item_new_path)
        else:
            os.mkdir(folder_path)
            shutil.move(item, item_new_path)
    # print(file_finder(folderpath_input, extensions_type))