# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dm_alchemy/protos/color_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dm_alchemy.protos import unity_types_pb2 as dm__alchemy_dot_protos_dot_unity__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"dm_alchemy/protos/color_info.proto\x12#deepmind.dmworlds.events.color_info\x1a#dm_alchemy/protos/unity_types.proto\"9\n\tColorInfo\x12\x1e\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x0f.deepmind.Color\x12\x0c\n\x04name\x18\x02 \x01(\tB\x18\xaa\x02\x15\x44\x65\x65pMind.Proto.Eventsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dm_alchemy.protos.color_info_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\025DeepMind.Proto.Events'
  _globals['_COLORINFO']._serialized_start=112
  _globals['_COLORINFO']._serialized_end=169
# @@protoc_insertion_point(module_scope)