import os
def rename_files():

    file_list = os.listdir(r"/Users/Apex/Desktop/Udacity/prank")
    print(file_list)
    saved_path =os.getcwd()
    print("Currently working dir " + saved_path)
    os.chdir(r"/Users/Apex/Desktop/Udacity/prank")

    for file_name in file_list:
        print("old name - "+ file_name)
        print("New name - "+ file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)


rename_files()