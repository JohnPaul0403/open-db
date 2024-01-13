class Data:
    def __init__(self, *args, **kwargs) -> None:
        for key, valure in kwargs.items():
            setattr(self, key, valure)

    def to_json(self):
        return self.__dict__
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
    
    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value
    
    def __hash__(self) -> int:
        return hash(tuple(self.__dict__.values()))
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __iter__(self):
        return iter(self.__dict__)
    
    def __len__(self):
        return len(self.__dict__)
    
    def __getitem__(self, key):
        return self.__dict__[key]
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value

def from_json(data:dict):
    return Data(**data)