import os
from os.path import join
import shutil

path = "C:/Users/DELL/Desktop"
lst = ["type_doc", "type_pictures", "type_pdf", "type_xls", "other_docs"]
path_dir = []
def make_dir(lst_names:list[str]) -> None:
    for name in lst_names:
        os_path = os.path.join(path,name)
        os.mkdir(os_path)
        path_dir.append(os_path)

def get_name(dir_name:list ) -> list[str]:
    new_lst = []
    for i in dir_name:
        new_lst.append(i.name)
    return new_lst

try:
    make_dir(lst)

except FileExistsError:
    path_lst = os.scandir(path)
    repository = get_name(path_lst)

    for dir_ in lst:
        if dir_ not in repository:
            os.mkdir(os.path.join(path,dir_))
            path_dir.append(os.path.join(path, dir_))
        else:
            if os.path.join(path, dir_) not in path_dir:
                path_dir.append(os.path.join(path, dir_))


with os.scandir(path) as obj:

    for file in obj:

        if not file.is_dir():

            if file.name.endswith("docx") and not os.path.exists(path_dir[0] + "/" + file.name):
                shutil.move(file.path, path_dir[0])

            elif file.name.endswith(("png","jpg",".jpeg")) and \
                    not os.path.exists(path_dir[1] + "/" + file.name):
                shutil.move(file.path,path_dir[1])

            elif file.name.endswith("pdf") and not os.path.exists(path_dir[2] + "/" + file.name):
                shutil.move(file.path, path_dir[2])

            elif file.name.endswith("xls") and not os.path.exists(path_dir[3] + "/" + file.name):
                shutil.move(file.path, path_dir[3])

            else:
                if not os.path.exists(path_dir[4] + "/" + file.name):
                    shutil.move(file.path, path_dir[4])
