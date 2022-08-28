from os import scandir, path, DirEntry, makedirs, rename, remove
from shutil import move, copy2
from json import load as load_json


class FolderOrganizer:
    def __init__(self, categories_file=r"categories.json") -> None:
        self._path = ""
        self.CATEGORIES_FILE = categories_file
        self._categories = self._load_categories()
        self._dont_touch = ["folder_organizer.py", "categories.json", "main.py"]

    def change_path(self, newPath:str):
        self._path = newPath

    #========== Helpers methods ==========#
    def _scandir(self):
        if self._path: return scandir(self._path)
        #scan working directory
        return scandir()


    def _get_file_extension(self, file:DirEntry) -> str:
        """return the extension of the given file or 'unknown' if the file has no extension"""
        extension = path.splitext(file.name)[1]
        return extension if extension else "Unknown"

    
    def _default_dont_touch(self, output_folder_name) -> list[str]:
        dont_touch = self._dont_touch
        dont_touch.append(output_folder_name)
        return dont_touch
        

    def _safe_move(self, item:DirEntry, destination_path:str) -> tuple:
        """move the item to the destination path if the destination path already exists, 
        else create the destination path and then move the item to it.
        
        return a tuple of two items:
            - 1: the count of total moved items (int)
            - 2: list of errors tuples (if errors occur else empty list), each tuple contains the item name and the error message
        """
        if not path.exists(destination_path):
            makedirs(destination_path)

        try:
            move(item.path, path.join(destination_path, item.name))
            return (True, )
        #expected errors
        except PermissionError as e:
            return (False, "Permission Error! File may be open or incomplete.")
        except FileNotFoundError as e:
            return (False, "File not Found ¯\_(ツ)_/¯")
        #unexpected error
        except Exception as e:
            return (False, str(e))
        

    #---- Helpers to read categories file ----#
    def _get_sub_categories(self, categories:dict) -> list:
        """return a list of all sub-extensions for the given categories dict"""
        sub_categories = []
        for k, v in categories.items():
            if type(v) is list:
                sub_categories.extend(v)
            else:
                sub_categories.extend(self._get_sub_categories(v))

        return sub_categories


    def _set_all_sub_categories(self, categories:dict) -> dict:
        """
        get normal categories dict and return a copy with 'all' key for each category has sub-categories, 
        so it become easy to search for a category to a given file.
        
        e.g: 
        -----
        input:
        ------        
        {
            "cat1": ["ext1", "ext2", "ext3"],
            "cat2": {
                "sub-cat1": ["ext1", "ext2", "ext3"],
                "sub-cat2": ["ext1", "ext2"]
            }
        }

        output:
        -------
            "cat1": ["ext1", "ext2", "ext3"],
            "cat2": {
                "all": ["ext1", "ext2", "ext3", "ext4", "ext5"]
                "sub-cat1": ["ext1", "ext2", "ext3"],
                "sub-cat2": ["ext4", "ext5"]
            }
        }
        
        """
        for k, v in categories.items():
            if type(v) is list:
                continue
            #dict
            categories[k]["all"] = self._get_sub_categories(v)
            categories[k] = self._set_all_sub_categories(v)
        
        return categories

    
    def _load_categories(self) -> dict:
        """Load categories from json file then return a dict with 'all' key for each category has sub-categories"""
        with open(self.CATEGORIES_FILE, "r") as f:
            categories = load_json(f)
        #add 'all' key for each category has sub-categories
        return self._set_all_sub_categories(categories)

    
    def _get_category(self, item:DirEntry, categories:dict=None) -> 'str|list[str]|None':
        """get an os.DirEntry object and search for corresponding category.

        return:
            - str: if a category is found and there is no sub-categories
            - list[str]: if a category is found but it have sub-categories
            - None: in case that no category is found
        
        """
        if not categories: categories = self._categories

        if extension := self._get_file_extension(item)[1: ]: #extension without '.'
            for category, extensions in categories.items():
                #category with no sub-categories
                if type(extensions) is list:
                    if extension in extensions:
                        return category
                    continue
                
                #category with sub-categories
                if type(extensions) is dict:
                    if extension in extensions["all"]:
                        categories_lst = []
                        categories_lst.append(category)
                        #find the sub category
                        sub_cat = self._get_category(item, categories=extensions)
                        #one sub-category
                        if type(sub_cat) is str:
                            categories_lst.append(sub_cat)
                        #multiple sub-categories
                        if type(sub_cat) is list:
                            categories_lst.extend(sub_cat)

                        return categories_lst            
        return None

    #========== methods to scan folder content ==========#
    def get_stats(self) -> dict:
        """return the number of files for each different extension in the folder, as well as the count of fodlers and the unknown files"""
        content = self._scandir()
        stats = {"Total": 0}
        #check each item in folder
        for item in content:
            stats["Total"] += 1

            #-- if Folder --#
            if item.is_dir():
                #add 'folders' to stats if not exist
                if "folders" not in stats.keys():
                    stats["folders"] = 0

                #increment the count of folders
                stats["folders"] += 1
                continue
            
            #-- if File --#
            #get the extension
            extension = path.splitext(item.name)[1]
            
            #if file has an extension
            if extension:
                #add the extension to stats if not exist
                if extension not in stats.keys():
                    stats[extension] = 0

                #increment the count of the extension
                stats[extension] += 1
                continue

            #if file has no extension (unknown file type)
            #add 'unknown' to stats if not exist
            if "unknown" not in stats.keys():
                stats["unknown"] = 0
            
            #increment the count of unknown
            stats["unknown"] += 1

        return stats


    def get_content(self, type:str) -> list[DirEntry]:
        """return a list of all items in the folder of selected type\n
            type can be:
                - 'files' to select all files 
                - 'folders' to select all folders
                - 'all' to select both files and folders
        """
        #return both files and folders
        if type == "all":
            return list(self._scandir())
        #return files
        elif type == "files":
            return [item for item in self._scandir() if item.is_file()]
        #return folders
        elif type == "folders":
            return [item for item in self._scandir() if item.is_dir()]
        #invalid type
        else:
            raise ValueError(f"Type should be 'all', 'files', or 'folders', but '{type}' is given!")


    #========== Methods to organize folder ==========#
    def organize_by_extensions(self, output_folder_name:str, content:list[DirEntry]=None, include_folders:bool=True, include_unknown:bool=True,dont_touch:list[str]=None) -> tuple:
        """organize the folder by extensions.
        all files with the same extension are placed in the same folder

        Args:
            - output_folder_name: string for the name of folder that will contains all organized content
            - include_folders: True to organize folders and place in 'Folders' folder, False to not
            - include_unknown: True to organize unknwon files and place in 'Unknown' folder, False to not
            - dont_touch: list of names of files or folders to do not move, by default it will contains the constant self._dont_touch plus the given output_folder_name
        
        return a tuple of two items:
            - 1: the count of total moved items (int)
            - 2: list of errors tuples (if errors occur else empty list), each tuple contains the item name and the error message
        """
        if content is None: content = self.get_content("all" if include_folders else "files")
        if dont_touch is None: 
            dont_touch = self._default_dont_touch(output_folder_name) 
        else: 
            dont_touch.append(output_folder_name)

        moved = 0
        errors = []

        for item in content:
            if item.name in dont_touch:
                continue

            #-- Folder --#
            if item.is_dir() and include_folders:
                response = self._safe_move(item, path.join(self._path, output_folder_name, "Folders"))
                if response[0]:
                    moved += 1
                else:
                    errors.append((item.path, response[1]))
                continue

            #-- File --#
            extension = self._get_file_extension(item)
            dest = None
            if extension != "Unknown" :
                dest = extension
            elif (extension == "Unknown") and (include_unknown):
                dest = "Unknown"

            if dest:
                response = self._safe_move(item, path.join(self._path, output_folder_name, extension))
                if response[0]:
                    moved += 1
                else:
                    errors.append((item.name, response[1]))

        #finish
        return (moved, errors)

    
    def organize_by_categories(self, output_folder_name, content:list[DirEntry]=None, include_folders:bool=True, include_unknown:bool=True,dont_touch:list[str]=None) -> tuple:
        """organize the folder by pre-defined categories (categories.json).
        all files with the same category are placed in the same folder, files with no category will be placed in 'Other' folder.

        Args:
            - output_folder_name: string for the name of folder that will contains all organized content
            - include_folders: True to organize folders and place in 'Folders' folder, False to not
            - include_unknown: True to organize unknown files and place in 'Other' folder
            - dont_touch: list of names of files or folders to do not move, by default it will contains the constant self._dont_touch plus the given output_folder_name
        
        return a tuple of two items:
            - 1: the count of total moved items (int)
            - 2: list of errors tuples (if errors occur else empty list), each tuple contains the item name and the error message
        """
        if content is None: content = self.get_content("all" if include_folders else "files")
        if dont_touch is None: 
            dont_touch = self._default_dont_touch(output_folder_name) 
        else: 
            dont_touch.append(output_folder_name)

        moved = 0
        errors = []

        for item in content:
            if item.name in dont_touch:
                continue

            #-- Folder --#
            if item.is_dir():
                response = self._safe_move(item, path.join(self._path, output_folder_name, "Folders"))
                if response[0]:
                    moved += 1
                else:
                    errors.append((item.path, response[1]))
                continue

            #-- File --#
            category = self._get_category(item)

            #one category
            if type(category) is str:
                response = self._safe_move(item, path.join(self._path, output_folder_name, category.title()))
                if response[0]:
                    moved += 1
                else:
                    errors.append((item.name, response[1]))
                continue
            
            #many sub-categories
            if type(category) is list:
                response = self._safe_move(item, path.join(self._path, output_folder_name, *list(map(lambda c: c.title(), category))))
                if response[0]:
                    moved += 1
                else:
                    errors.append((item.name, response[1]))
                continue

            #unknown category
            if (category is None) and (include_unknown):
                response = self._safe_move(item, path.join(self._path, output_folder_name, "Other"))
                if response[0]:
                    moved += 1
                else:
                    errors.append((item.name, response[1]))
            
        #finish
        return (moved, errors)


    #========== Modifying folder content ==========#
    def rename_content(self, new_name_pattern:str, content:list[DirEntry]=None, include_folder=True, dont_touch:list[str]=None) -> tuple:
        """Rename folder content to similar names (as the given name pattern)

        Args:
            - new_name_pattern: the pattern string. [special characters: []: an index | {}: the old name]
            - include_folders: True to rename folders as well, False to not
            - dont_touch: list of names of files or folders to do not rename, by default it will contains the constant self._dont_touch

        return a tuple of two items:
            - 1: list of tuples. Each tuple contains the old name and the new name
            - 2: list of errors tuples (if errors occur else empty list), each tuple contains the item name and the error message
        """
        if content is None: content = self.get_content("all" if include_folder else "files")
        if dont_touch is None: dont_touch = self._dont_touch

        #if there is more than one item and the pattern is a static string
        if len(content) > 1 and ("{}" not in new_name_pattern and "[]" not in new_name_pattern):
            #add an index at the end of name
            new_name_pattern += "[]"

        renamed = []
        errors = []

        for index, item in enumerate(content):
            if item.name in dont_touch:
                continue
            
            extension = path.splitext(item.name)[1]
            new_name = new_name_pattern.replace("[]", str(index))
            new_name = new_name.replace("{}", item.name)
            new_name += extension
            try:
                rename(item.path, item.path.replace(item.name, new_name))
                renamed.append((item.name, new_name))
            #expected errors
            except PermissionError as e:
                errors.append((item.name, "Permission Error! File may be open or incomplete."))
            except FileNotFoundError as e:
                errors.append((item.name, "File not Found ¯\_(ツ)_/¯"))
            except Exception as e:
                errors.append((item.name, str(e)))

        return (renamed, errors)

    
    def change_extensions(self, current:str, new:str, content:list[DirEntry]=None, dont_touch:list=None) -> tuple:
        """Change the extension of all files that have [current] extension to the [new] extension

        Args:
            - current: the current extension
            - new: the new extension
            - dont_touch: list of names of files or folders to do not rename, by default it will contains the constant self._dont_touch

        return a tuple of two items:
            - 1: the count of total changed items (int)
            - 2: list of errors tuples (if errors occur else empty list), each tuple contains the item name and the error message
        """

        #make sure that extensions have '.' at the beginning
        if current[0] != ".": current = "." + current
        if new[0] != ".": new = "." + new

        if content is None: content = self.get_content(type="files")
        #filter selected content (remove folders if any)
        content = list(filter(lambda f: f.is_file(), content))

        if dont_touch is None: dont_touch = self._dont_touch

        changed = 0
        errors = []

        #get all files with given extension(s)
        for file in content:
            if file.name in dont_touch:
                continue

            #if file has different extension (not [current] extension)
            if self._get_file_extension(file) != current:
                continue

            try:
                #the name with the new extension
                new_name = path.splitext(file.name)[0] + new
                rename(file.path, file.path.replace(file.name, new_name))
                changed += 1
            #expected errors
            except PermissionError as e:
                errors.append((file.name, "Permission Error! File may be open or incomplete."))
            except FileNotFoundError as e:
                errors.append((file.name, "File not Found ¯\_(ツ)_/¯"))
            except Exception as e:
                errors.append((file.name, str(e)))
        
        return (changed, errors)


    #========== Basic methods ==========#
    def copy_content(self, dest_path:str, content:list[DirEntry]=None, dont_touch:list=None) -> tuple:
        if content is None: content = self.get_content(type="files")
        if dont_touch is None: dont_touch = self._dont_touch

        copied = 0
        errors = []

        for item in content:
            if item.name in dont_touch:
                continue

            try:
                copy2(item.path, path.join(dest_path, item.name))
                copied += 1
            #expected errors
            except PermissionError as e:
                errors.append((item.name, "Permission Error! File may be open or incomplete."))
            except FileNotFoundError as e:
                errors.append((item.name, "File not Found ¯\_(ツ)_/¯"))
            except Exception as e:
                errors.append((item.name, str(e)))

        return (copied, errors)


    def move_content(self, dest_path:str, content:list[DirEntry]=None, dont_touch:list=None) -> tuple:
        if content is None: content = self.get_content(type="files")
        if dont_touch is None: dont_touch = self._dont_touch

        moved = 0
        errors = []

        for item in content:
            if item.name in dont_touch:
                continue
                
            try:
                move(item.path, path.join(dest_path, item.name))
                moved += 1
            #expected errors
            except PermissionError as e:
                errors.append((item.name, "Permission Error! File may be open or incomplete."))
            except FileNotFoundError as e:
                errors.append((item.name, "File not Found ¯\_(ツ)_/¯"))
            #unexpected error
            except Exception as e:
                errors.append((item.name, str(e)))

        return (moved, errors)

    
    def delete_content(self, content:list[DirEntry]=None, dont_touch:list=None) -> tuple:
        if content is None: content = self.get_content(type="files")
        if dont_touch is None: dont_touch = self._dont_touch

        deleted = 0
        errors = []

        for item in content:
            if item.name in dont_touch:
                continue
                
            try:
                remove(item.path)
                deleted += 1
            #expected errors
            except PermissionError as e:
                errors.append((item.name, "Permission Error! File may be open or incomplete."))
            except FileNotFoundError as e:
                errors.append((item.name, "File not Found ¯\_(ツ)_/¯"))
            #unexpected error
            except Exception as e:
                errors.append((item.name, str(e)))

        return (deleted, errors)
