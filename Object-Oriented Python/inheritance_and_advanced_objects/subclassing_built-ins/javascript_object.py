class JavaScriptObject(dict):
    def __getattr__(self, item): # used whenever we ask for an attribute using dot notation
        try:
            return self[item] # if key exists we'll get it from the dict
            # class version
        except KeyError:
            return super().__getattribute__(item) # if it doesn't exist we fall back to the dict version of get
            # attribute which looks for an attribute with that name.  Python version of dict.  In traceback throws
            # AttributeError