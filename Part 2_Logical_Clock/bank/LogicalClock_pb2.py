# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LogicalClock.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12LogicalClock.proto\x12\x0cLogicalClock\"x\n\x07Request\x12\x11\n\tsender_id\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x1b\n\x13\x63ustomer_request_id\x18\x03 \x01(\x05\x12\x11\n\tinterface\x18\x04 \x01(\t\x12\r\n\x05money\x18\x05 \x01(\x05\x12\r\n\x05\x63lock\x18\x06 \x01(\x05\"y\n\x08Response\x12\x11\n\tsender_id\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x1b\n\x13\x63ustomer_request_id\x18\x03 \x01(\x05\x12\x11\n\tinterface\x18\x04 \x01(\t\x12\r\n\x05money\x18\x05 \x01(\x05\x12\r\n\x05\x63lock\x18\x06 \x01(\x05\x32\xd0\x01\n\x0cLogicalClock\x12<\n\x0bMsgDelivery\x12\x15.LogicalClock.Request\x1a\x16.LogicalClock.Response\x12<\n\x0bRecvRequest\x12\x15.LogicalClock.Request\x1a\x16.LogicalClock.Response\x12\x44\n\x13PropagateToBranches\x12\x15.LogicalClock.Request\x1a\x16.LogicalClock.ResponseB\x02P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'LogicalClock_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _globals['_REQUEST']._serialized_start=36
  _globals['_REQUEST']._serialized_end=156
  _globals['_RESPONSE']._serialized_start=158
  _globals['_RESPONSE']._serialized_end=279
  _globals['_LOGICALCLOCK']._serialized_start=282
  _globals['_LOGICALCLOCK']._serialized_end=490
# @@protoc_insertion_point(module_scope)
