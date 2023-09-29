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
        """Get text data from text file"""

        with open(fp, 'rb') as f:
            try:
                results = f.read()
            except:
                results = "Loading Error."
        
        return results
