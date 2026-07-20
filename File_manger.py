import os
import shutil as sh
class File:


    @staticmethod
    def rename()-> None:

        old = input("Enter file/folder/path  ")
        new = input("new name/path ")

        
        if not old or not new:
            print("File/Folder name cannot be Empty")
            return

        if os.path.exists(new):
            print(f"{new} exists already")
            return
        try:
            os.rename(old,new)
        except FileNotFoundError:
            print("destination not found")
        except OSError:
            print("OS Error")
        except Exception:
            print("Unknown Error")


    @staticmethod
    def move() -> None:

        file_name = input("Enter file/folder name ")
        destination = input("new path ")

        if not file_name or not destination:
            print("File/Folder name cannot be Empty")
            return

        if os.path.exists(destination):
            print(f"{destination} exists already")
            return

        try:
            os.rename(file_name,destination)
        except FileNotFoundError:
            print("destination not found")
        except OSError:
            print("OS Error")
        except Exception:
            print("Unknown Error")

    @staticmethod
    def copy():

        source = input("Enter file/folder path ")
        destination = input("new path ")

        if not source or not destination:
            print("File/Folder name/path cannot be Empty")
            return

        if os.path.exists(destination):
            print(f"{destination} exists already")
            return

        try:
            sh.copy(source,destination)
        except FileNotFoundError:
            print("destination not found")
        except OSError:
            print("OS Error")
        except Exception:
            print("Unknown Error")





    @staticmethod
    def name_path()-> tuple:
        name = input("Enter file/folder name")
        path = input("Enter path (optional)\nDefault is current path")

        if not name:
            print("Folder name cannot be Empty")
            return
        if not path:
            path = os.getcwd()
        return name,path





    @staticmethod
    def flist() -> None:
        current_dir = os.listdir()
        for file in current_dir:
            print(file,end=" ")




    @staticmethod
    def cfolder(name,path) -> None:
        f_path = os.path.join(path,name)
        try:
            os.mkdir(f_path)
        except FileExistsError:
            print("Folder exists!")
        except FileNotFoundError:
            print("Not Found!")
        except Exception:
            print("UnknownError")
    




    @staticmethod
    def del_folder(name,path = os.getcwd()) -> None:
        f_path = os.path.join(path,name)
        try:

            sh.rmtree(f_path)

        except FileNotFoundError:
            print(f"Folder not found at path {f_path}")
        except PermissionError:
            print(f" permmission error at path {f_path}")
        except OSError:
            print("OS ERROR")
        except Exception:
            print("Unknown Error")
        

    @staticmethod
    def del_file(name,path = os.getcwd()) -> None:
        f_path = os.path.join(path,name)
        try:
            os.remove(f_path)
        except FileNotFoundError:
            print(f"File not found at path {f_path}")
        except Exception:
            print("Unknown Error")


    @staticmethod
    def search():
        target = input("Enter file name to search")
        path = input("Enter path (optional)")

        if not path:
            path = os.getcwd()


        if not target:
            print("Empty search target")
            return

        
        try:
            os.listdir(path)
        except FileNotFoundError:
            print(f"{path} does not exist")
        except PermissionError:
            print("permission error")
        except OSError:
            print("OS ERROR")
        except Exception:
            print("Unknown Error")
            
        else:
            if target in os.listdir(path):
                print(f"exists at {path}")
                return
            else:
                print("File Not Found")



    @staticmethod
    def get_file_info():
        target = input("name the file ")
        if not target:
            print("name cannot be empty")
            return
        i = target.rfind(".")
        if i == -1:
            print("invalid target")
            return
        ext = target[i+1:]
        name = target[:i]

        print(f"file name is {name}, file extention is {ext}")




    @staticmethod
    def write_file():

        filename = input("Enter file name ")
        content = input("What do you want to write")

        if not filename or not content:
            print("inputs cannot be Empty")
            return
        try:
            with open(filename,"w") as f:
                f.write(content)
            print("Done")
        except FileNotFoundError:
            print(f"{filename} does not exist")
        except PermissionError:
            print("permission error")
        except OSError:
            print("OS ERROR")
        except Exception:
            print("Unknown Error")
    
    @staticmethod
    def read_file():

        name_path = File.name_path()
        if name_path is None:
            return
        name,path = name_path
        f_path = os.path.join(path,name)
        try:
            with open(f_path,"r",encoding = "utf-8")as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print(f"{f_path} does not exist")
        except PermissionError:
            print("permission error")
        except OSError:
            print("OS ERROR")
        except Exception:
            print("Unknown Error")



        

        



        
        
        



                
            


    



        


class user_interface:
    @staticmethod
    def show() -> None:
        print("""========== File Manager ==========

1. List files
2. Create folder
3. Delete folder
4. Delete file
5. Rename
6. Copy
7. Move
8. Search
9. File info
10. Read text file
11. Write text file
12. Exit""")


    @staticmethod
    def Take_input() -> int:
        try:
            user_input = int(input())
        except ValueError:
            print("please enter a number")
            ("input acknowledged\nTake_input status code 2")#2 Invalid data type input
            return
        except KeyboardInterrupt:
            print("Interrupted keyboard")
            ("input acknowledged\nTake_input status code 3") #3 keyboard user interruption
            return
        except Exception:
            print("Invalid input")
            ("input acknowledged\nTake_input status code 4") #4 unknown Exception
            return
        else:
            if user_input not in range(1,12+1):
                print("invalid option please enter numbers from 1-12 only")
                ("input acknowledged\nTake_input status code 1") #1 --> out of range input
                return
            
            return user_input
        finally:
            print("input acknowledged\nTake_input status code 0") #0 means ran


    @staticmethod
    def exit(choice):
        if choice == 12:
            return True
        return False


    
    @staticmethod
    def Invoke_func(choice):

        match choice:
            case 1:
                File.flist()
                return
            case 2:
                name_path = File.name_path()
                if name_path is None:
                    return
                name,path = name_path
                File.cfolder(name,path)
                return
            
            case 3:
                name_path = File.name_path()
                if name_path is None:
                    return
                name,path = name_path
                File.del_folder(name,path)
                return

                
            
            case 4:

                name_path = File.name_path()
                if name_path is None:
                    return
                name,path = name_path
                File.del_file(name,path)
                return

            
            case 5:
                File.rename()
                return


            case 6:
                File.copy()
                return

            case 7:
                File.move()
                return

            case 8: 
                File.search()
                return

            case 9:
                File.get_file_info()
                return

            case 10:
                File.read_file()
                return
            case 11:
                File.write_file()
                return








        

        


def main():
    while True:
        user_interface.show()
        user_choice = user_interface.Take_input()
        if user_interface.exit(user_choice):
            print("Thanks for your time Hope you have a wonderful day")
            break
        else:
            user_interface.Invoke_func(user_choice)


if __name__ == "__main__":
    main()