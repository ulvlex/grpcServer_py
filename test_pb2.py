# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntest.proto\x12\x04test\"h\n\x0fGenerateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x17\n\x0f\x63\x61pibara_format\x18\x02 \x01(\t\x12\x16\n\x0e\x63\x61pibara_slang\x18\x03 \x01(\t\x12\x18\n\x10\x63\x61pibara_phrases\x18\x04 \x03(\t\"#\n\x10GenerateResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1e\n\x10StatementRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"6\n\x11StatementResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x11\n\tfile_data\x18\x02 \x01(\x0c\"/\n\x15StatementSlangRequest\x12\x16\n\x0e\x63\x61pibara_slang\x18\x01 \x01(\t\";\n\x16StatementSlangResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x11\n\tfile_data\x18\x02 \x01(\x0c\x32\xd3\x01\n\x0bTestService\x12\x39\n\x08generate\x12\x15.test.GenerateRequest\x1a\x16.test.GenerateResponse\x12<\n\tstatement\x12\x16.test.StatementRequest\x1a\x17.test.StatementResponse\x12K\n\x0estatementSlang\x12\x1b.test.StatementSlangRequest\x1a\x1c.test.StatementSlangResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GENERATEREQUEST']._serialized_start=20
  _globals['_GENERATEREQUEST']._serialized_end=124
  _globals['_GENERATERESPONSE']._serialized_start=126
  _globals['_GENERATERESPONSE']._serialized_end=161
  _globals['_STATEMENTREQUEST']._serialized_start=163
  _globals['_STATEMENTREQUEST']._serialized_end=193
  _globals['_STATEMENTRESPONSE']._serialized_start=195
  _globals['_STATEMENTRESPONSE']._serialized_end=249
  _globals['_STATEMENTSLANGREQUEST']._serialized_start=251
  _globals['_STATEMENTSLANGREQUEST']._serialized_end=298
  _globals['_STATEMENTSLANGRESPONSE']._serialized_start=300
  _globals['_STATEMENTSLANGRESPONSE']._serialized_end=359
  _globals['_TESTSERVICE']._serialized_start=362
  _globals['_TESTSERVICE']._serialized_end=573
# @@protoc_insertion_point(module_scope)
