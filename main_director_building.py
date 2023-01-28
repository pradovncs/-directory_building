import os
import shutil

def create_project_dir(directory: str, sub_dirs: list = [], files: list = [[]]) -> None:
    """
    Create a directory for the project.

    Args:
    directory: Directory where the project will be.
    sub_dirs: List containing the sub directories.
    files: List of lists containing the files of your project, with each sublist representing the files in one subdirectory.

    Returns:
        None.
    """
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

    for sub_dir in sub_dirs:
        os.makedirs(os.path.join(directory, sub_dir))
        
    for sub_dir, file_list in zip(sub_dirs, files):
        for file in file_list:
            full_path = os.path.join(directory, sub_dir, file)
            with open(full_path, 'w') as f:
                f.write('')


if __name__ == '__main__':
    BASE_DIR = r"C:\Users\Vinicius\Desktop\RPA\GenericProject"
    create_project_dir(BASE_DIR, ["pages", "locators", "utils"], [["BasePage.py", "LoginPage.py", "HomePage.py"], ["Locators.py"], ["Utils.py"]])