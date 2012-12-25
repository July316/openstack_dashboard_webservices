from spyne.application import Application
from spyne.decorator import srpc, rpc
from spyne.protocol.soap import Soap11
from spyne.protocol.http import HttpRpc
from spyne.service import ServiceBase
from spyne.model.complex import Array, Iterable, ComplexModel
from spyne.model.primitive import Integer, Float, Unicode, Boolean, String, AnyDict
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt

from .wic.wic_client import wic_client
c = wic_client()

class WebService(ServiceBase):
    @srpc(String, Unicode, String, String, String, _returns=AnyDict)
    def CreateUser(requestId, userName, phoneNumber, email, timestamp):
        params = {'requestId':requestId}
        params['CreateUser'] = {
		'userName':userName,
		'phoneNumber':phoneNumber,
		'email':email,
		'timestamp':timestamp,
		}
        res = c.wic_add_user(**params)
        return res
        
    @srpc(String, String, String, _returns=AnyDict)
    def DescribeSecurityGroup(requestId, timestamp, groupName):
        params = {'requestId':requestId}
        params['DescribeSecurityGroup'] = {
		'timestamp':timestamp,
		'groupName':groupName,
		}
        res = c.wic_secgroup_show(**params)
        return res
                
    @srpc(String, String, String, String,  _returns=AnyDict)
    def StopHost(requestId, trancetionId, instanceId, timestamp):
        params = {'requestId':requestId}
        params['StopHost'] = {
        	'trancetionId':trancetionId,
		'timestamp':timestamp,
		'groupName':groupName,
		}
        res = c.wic_stop_host(**params)
        return res
        
    @srpc(String, String, String, String, _returns=AnyDict)
    def DelHost(requestId, trancetionId, instanceId, timestamp):
        params = {'requestId':requestId}
        params['DelHost'] = {
        	'trancetionId':trancetionId,
		'instanceId':instanceId,
		'timestamp':timestamp,
		}
        res = c.wic_del_host(**params)
        return res
        
    @srpc(String, String, String, String, String, _returns=AnyDict)
    def CreateDisk(requestId, trancetionId, instanceId, timestamp, disk):
        params = {'requestId':requestId}
        params['CreateDisk'] = {
        	'trancetionId':trancetionId,
		'instanceId':instanceId,
		'timestamp':timestamp,
		'disk':disk,
		}
        res = c.wic_create_disk(**params)
        return res
        
    @srpc(String, String, String, String, String, String,  _returns=AnyDict)
    def BindDisk(requestId, trancetionId, instanceId, volumeId, ostype, timestamp):
        params = {'requestId':requestId}
        params['BindDisk'] = {
        	'trancetionId':trancetionId,
		'instanceId':instanceId,
		'volumeId':volumeId,
		'ostype':ostype,
		'timestamp':timestamp,
		}
        res = c.wic_bind_disk(**params)
        return res
        
    @srpc(String, String, String, String,  _returns=AnyDict)
    def DelDisk(requestId, trancetionId, volumeId, timestamp):
        params = {'requestId':requestId}
        params['DelDisk'] = {
        	'trancetionId':trancetionId,
		'volumeId':volumeId,
		'timestamp':timestamp,
		}
        res = c.wic_del_disk(**params)
        return res
        
    @srpc(String, String, String, String,  _returns=AnyDict)
    def RestartHost(requestId, trancetionId, instanceId, timestamp):
        params = {'requestId':requestId}
        params['DelDisk'] = {
        	'trancetionId':trancetionId,
		'instanceId':instanceId,
		'timestamp':timestamp,
		}
        res = c.wic_restar_host(**params)
        return res
        
    @srpc(String, String, String, String,  _returns=AnyDict)
    def ShutdownHostService(requestId, trancetionId, instanceId, timestamp):
        params = {'requestId':requestId}
        params['DelDisk'] = {
        	'trancetionId':trancetionId,
		'instanceId':instanceId,
		'timestamp':timestamp,
		}
        res = c.wic_shutdown_hostservice(**params)
        return res
        
    @srpc(String, String, String, String, _returns=AnyDict)
    def CreateSecurityGroup(requestId, trancetionId, timestamp, groupSize):
        params = {'requestId':requestId}
        params['CreateSecurityGroup'] = {
                'trancetionId':trancetionId,
                'timestamp':timestamp,
                'groupSize':groupSize,
                }
        res = c.wic_create_securitygroup(**params)
        return res
        
soap_services = csrf_exempt(DjangoApplication(Application([WebService],
        'soap.services',
        in_protocol=Soap11(),
        out_protocol=Soap11(),
    )))
