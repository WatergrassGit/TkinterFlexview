class DataModel:
    """Model which manages how program interacts with data."""

    def __init__(self):
        self.long_text = self.get_text("longtext.txt")

    @property
    def long_text(self):
        return self._long_text
    
    @long_text.setter
    def long_text(self, new_data):
        self._long_text = new_data

    def get_text(self, fp):
        """
        Get text data from text file
        
        :arguments
        ----------
        fp: str
            file path of file being loaded
        """

        try:
            with open(fp, 'rb') as f:
                results = f.read()
        except FileNotFoundError:
                results = "Loading Error - Text File Not Found."
        return results
