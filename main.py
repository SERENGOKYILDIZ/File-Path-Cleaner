import os
import shutil


def Folder_Cleaning(path: str):
    if os.path.exists(path):
        try:
            files = os.listdir(path)
            if len(files) == 0:
                print("ERROR: The file to be deleted was not found in the folder")
            else:
                for file in files:
                    PATH_file = f"{path}/{file}"
                    if os.path.isfile(PATH_file):
                        os.remove(PATH_file)
                        print(f"Deleted file: {PATH_file}")
                    else:
                        shutil.rmtree(PATH_file)
                        print(f"Deleted file: {PATH_file}")
                print("\nThe file deletion process is completed! :)")
        except:
            print("ERROR: An unknown error appeared!!")
    else:
        print("ERROR: The file was not found")


# yol = "C:/Users/Eren/Desktop/deneme"
PATH = input("Please enter a path:")
print(f"The entered file path: {PATH}")
Folder_Cleaning(PATH)
