# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Environment.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x45nvironment.proto\x12\x0b\x45nvironment\"=\n\x10HandshakeRequest\x12\x16\n\x0en_observations\x18\x01 \x01(\x05\x12\x11\n\tn_actions\x18\x02 \x01(\x05\"/\n\x11HandshakeResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\x05\"\x1b\n\rSampleRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"}\n\x0eSampleResponse\x12\x13\n\x0bobservation\x18\x01 \x01(\x0c\x12\x0e\n\x06reward\x18\x02 \x01(\x02\x12\x12\n\nterminated\x18\x03 \x01(\x08\x12\x11\n\ttruncated\x18\x04 \x01(\x08\x12\x0f\n\x07\x65pisode\x18\x05 \x01(\x05\x12\x0e\n\x06status\x18\x06 \x01(\x05\"+\n\rActionRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x0c\" \n\x0e\x41\x63tionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x32\xef\x01\n\x0b\x45nvironment\x12Y\n\x16handshake_and_validate\x12\x1d.Environment.HandshakeRequest\x1a\x1e.Environment.HandshakeResponse\"\x00\x12\x43\n\x06sample\x12\x1a.Environment.SampleRequest\x1a\x1b.Environment.SampleResponse\"\x00\x12@\n\x03\x61\x63t\x12\x1a.Environment.ActionRequest\x1a\x1b.Environment.ActionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Environment_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HANDSHAKEREQUEST']._serialized_start=34
  _globals['_HANDSHAKEREQUEST']._serialized_end=95
  _globals['_HANDSHAKERESPONSE']._serialized_start=97
  _globals['_HANDSHAKERESPONSE']._serialized_end=144
  _globals['_SAMPLEREQUEST']._serialized_start=146
  _globals['_SAMPLEREQUEST']._serialized_end=173
  _globals['_SAMPLERESPONSE']._serialized_start=175
  _globals['_SAMPLERESPONSE']._serialized_end=300
  _globals['_ACTIONREQUEST']._serialized_start=302
  _globals['_ACTIONREQUEST']._serialized_end=345
  _globals['_ACTIONRESPONSE']._serialized_start=347
  _globals['_ACTIONRESPONSE']._serialized_end=379
  _globals['_ENVIRONMENT']._serialized_start=382
  _globals['_ENVIRONMENT']._serialized_end=621
# @@protoc_insertion_point(module_scope)
