#! /usr/bin/python3.6
from classes.Commands import Commands
from classes.Comodo import Comodo
import json, os

path = os.path.dirname(os.path.realpath(__file__))

#from classes.Dom import Domain
#from classes.Log import Log
#from classes.whm import WHM

"""
Test Commands class
"""

#input_args = Commands()

"""
Test Comodo class
"""

com = Comodo('Y')

"""
    Test Comodo.setDcvMethod
"""

#print('DCV Method before Comodo.setDcvMethod: ' + com.args['dcvMethod'])
#com.setDcvMethod('HTTP_CSR_HASH')
#print('DCV Method after Comodo.setDcvMethod: ' + com.args['dcvMethod'])

"""
    Test Comodo.get_csr_hashes
"""

#with open(path + '/test/testCsrData.json', 'r') as testCsrData:
#    csr_data = json.load(testCsrData)
#print('Test Comodo.get_csr_hashes ::')
#print(com.get_csr_hashes(csr_data['csr']))

"""
    Test Comodo.orderSsl
"""

#with open(path + '/test/testCsrData.json', 'r') as testCsrData:
#    csr_data = json.load(testCsrData)
#print('Test Comodo.orderSsl\n SSL Order No:: ')
#orderSsl = com.orderSsl(csr_data['csr'])
#print(orderSsl[1])

"""
    Test Comodo.collectSsl
"""

with open(path + '/test/testSslOrder.json', 'r') as testSslOrder:
    testSslOrder = json.load(testSslOrder)
print(testSslOrder[1])