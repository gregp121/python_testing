## Interfaces are probably a more robust way to handle classes

# Situation: Data Engineer extracting data
class informalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str: # This is telling (not requiring) the function to return a str
        "Load in file for tracting text"
        pass

    def extract_text(self, full_file_name: str) -> str:
        "Extract text from currently loaded file"
        pass

# We can implement classes with the inteface above
class pdfParser(informalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    def extract_text(self, full_file_name: str) -> str:
        pass

class emailParser(informalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    def extract_text(self, full_file_name: str) -> str:
        pass

# print(issubclass(emailParser, informalParserInterface))
# print(issubclass(pdfParser, informalParserInterface))
# ## Note, the above shows that what we have created are subclasses, which violates our interface definition (hence, the informal)
# ## Below, we can see it checks the subclass, then the super
# print(pdfParser.__mro__)
# print(emailParser.__mro__)

## Ideally, we want issubclass to return FALSE when the implementing class doesn't define all of the interfaces abstract methods

class ParserMeta(type):
    # A parser metaclass that we'll use for parser class creation
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    
    # Creating "meta" attributes/methods requirements. (Needs these to be classed)
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))

class updatedInformalParserIntreface(metaclass=ParserMeta):
    # Created for concrete classes to inherit
    # No need to define parseMeta methods as any class, they are iplicit from subclass check
    pass

class pdfParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_path: str) -> dict:
        pass

class emailParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        pass

print(issubclass(pdfParserNew, updatedInformalParserIntreface))
print(issubclass(emailParserNew, updatedInformalParserIntreface))
print(pdfParserNew.__mro__) # Our superclass is not in method resolution order. That's because it is a virtual base class of it
print(emailParserNew.__mro__)

## So an intormal interface will call a metaclass. These, however, are not good for larger applications