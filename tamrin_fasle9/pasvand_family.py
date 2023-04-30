#name file ro daryaft mikone name ro az family jod amikone 


def get_name_file(file):
    filename = file[:file.index('.')]
    passname = file[file.index('.')+1:]
    print(f"file:{file}\nfilename:{filename}\npassname:{passname}")
 
 
for i in range(4):
    file = input("please enter file nmae:\n")    
    get_name_file(file)

