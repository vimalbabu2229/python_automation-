import os, re, shutil

class MediaFilter:
    """
    This class contains methods to filter a media folder with the file extensions 
    """
    def __init__(self, path: str, file_types: list[str]) -> None:
        self.path: str = path
        self.file_types: list[str] = file_types
        
        # create the pattern 
        pattern_str = f"{file_types[0]}"
        for i in range(1, len(file_types)):
            pattern_str += f"|{file_types[i]}"

        self.pattern = re.compile(rf"\.({pattern_str})$", re.IGNORECASE)

    # ++++++++++++++++ FILTER METHOD ++++++++++++++++++++
    def filter(self) -> str:
        """
        This method filters the files in the base folder and move them into 
        dedicated folders for each file types .
        """
        try :
            os.chdir(self.path)
            for type in self.file_types:
                # create folders for each file types 
                if not os.path.exists(type):
                    os.mkdir(type)

            # create additional folder for the other files 
            if not os.path.exists('others'):
                os.mkdir('others')

            files = os.listdir(".")

            for file in files:
                if os.path.isfile(file):
                    match = self.pattern.search(file)
                    if match:
                        folder = match.group().removeprefix('.')
                        shutil.move(file, folder)
                    else :
                        shutil.move(file, 'others')

            return 'Successfully filtered .....'
            
        except Exception as e :
            return str(e)
