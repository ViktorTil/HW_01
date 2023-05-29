import pathlib
from pathlib import Path


from modul_func import delete_empty, parsing, sort_list_files, transfer, unpack
import sys
try:
    if pathlib.Path(sys.argv[1]).exists():
        parce_folder=sys.argv[1]
    
    else:
        print('!!!!No such folder!!!!')
        exit()
except IndexError:
    print("Please, add folder!!!!!")  
    exit()  



sorted = parce_folder # можно отдельно указать,например: +/sorted


def main(folder):
    
    list_files, list_dir_del = parsing(parce_folder) # распарcинг папки

    sort_files=sort_list_files(list_files) # сортировка файлов по типам

    transfer(sort_files, parce_folder) # сортировка файлов по новым папкам

    arc=Path(sorted).joinpath('archives')
    unpack(arc) #  обработка архивов-разархивирование
    
    delete_empty(list_dir_del) # удаление пустых папок
  
if __name__== '__main__':
    main(parce_folder)











    
    
    
    
    

    

    

    