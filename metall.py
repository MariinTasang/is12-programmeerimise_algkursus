import soaplib
from soaplib.core.service import rpc, DefinitionBase
from soaplib.core.model.primitive import String, Integer
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array
from soaplib.core.service import soap

class CreateMetall(DefinitionBase):


        @soap(Integer,Integer,Integer,Integer,_returns=Array(Integer))
        def add(self, height, width, depth, weight):
            global result
            result=[height, width, depth, weight]
            
        @soap(_returns=Array(Integer))
        def view(self):
            return result


        @soap(_returns=Integer)
        def density(self):
                density = result[3]/(result[0]*result[1]*result[2])
                return density
                
        def cubage(self):
                cubage = result[0]*result[1]*result[2]
                return cubage


if __name__=='__main__':
     try:
        from wsgiref.simple_server import make_server
        soap_application = soaplib.core.Application([CreateMetall], 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 7789, wsgi_application)
        server.serve_forever()
     except ImportError:
        print "Error: example server code requires Python >= 2.5"
