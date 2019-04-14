#! /usr/bin/python3.6
from classes.Commands import Commands
from classes.Comodo import Comodo
#from classes.Dom import Domain
#from classes.Log import Log
#from classes.whm import WHM

#Test Commands class
input_args = Commands()
com = Comodo(input_args.input_args['testssl'])
print('DCV Method before Comodo.setDcvMethod: ' + com.args['dcvMethod'])
com.setDcvMethod('HTTPS_CSR_HASH')
print('DCV Method after Comodo.setDcvMethod: ' + com.args['dcvMethod'])
#test