import sys

class Const:
    class ConstError(TypeException):pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError("Can't rebind const instance attribute (%s)" % name)
        
        self.__dict__[name]=value

sys.modules[__name__]= Const()