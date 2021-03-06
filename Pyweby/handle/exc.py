class MethodNotAllowedException(Exception):
    def __init__(self,msg=None,method=None):
        super(MethodNotAllowedException,self).__init__(msg or '{} method is not allowed!'.format(method))


class NoRouterHandlers(Exception):
    def __init__(self,msg=None):
        super(NoRouterHandlers,self).__init__(msg or 'No handler to deal with request')


class FormatterError(Exception):
    def __init__(self,msg=None,uri=None,obj=None):
        super(FormatterError,self).__init__(msg
                                            or 'handlers formatter error,({uri},{obj})'.format(uri=uri,obj=obj))

class StatusError(Exception):
    def __init__(self,msg=None,status=None):
        super(StatusError,self).__init__(msg or 'status {} is not allowed, must be int and 200=<x<=500'.format(status))


class NoPackageFound(Exception):
    def __init__(self, msg=None, pkname=None):
        super(NoPackageFound, self).__init__(msg or 'package {} is not found, try `pip install {}` '.format(pkname,pkname))
