# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: websockets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10websockets.proto\x12\nwebsockets\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\t2A\n\x06Sender\x12\x37\n\x0bSendMessage\x12\x13.websockets.Message\x1a\x11.websockets.Reply\"\x00\x62\x06proto3')



_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_REPLY = DESCRIPTOR.message_types_by_name['Reply']
Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'websockets_pb2'
  # @@protoc_insertion_point(class_scope:websockets.Message)
  })
_sym_db.RegisterMessage(Message)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'websockets_pb2'
  # @@protoc_insertion_point(class_scope:websockets.Reply)
  })
_sym_db.RegisterMessage(Reply)

_SENDER = DESCRIPTOR.services_by_name['Sender']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=32
  _MESSAGE._serialized_end=58
  _REPLY._serialized_start=60
  _REPLY._serialized_end=84
  _SENDER._serialized_start=86
  _SENDER._serialized_end=151
# @@protoc_insertion_point(module_scope)
