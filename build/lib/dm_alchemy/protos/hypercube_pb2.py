# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dm_alchemy/protos/hypercube.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!dm_alchemy/protos/hypercube.proto\x12\"deepmind.dmworlds.events.hypercube\"5\n\x0fHypercubeVertex\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x13\n\x0b\x63oordinates\x18\x02 \x03(\x05\"\xb1\x01\n\tEdgeLabel\x12\x17\n\x0f\x64imension_index\x18\x01 \x01(\x05\x12J\n\tdirection\x18\x02 \x01(\x0e\x32\x37.deepmind.dmworlds.events.hypercube.EdgeLabel.Direction\"?\n\tDirection\x12\r\n\tUNDEFINED\x10\x00\x12\x15\n\x08NEGATIVE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0c\n\x08POSITIVE\x10\x01\x42\x19\xaa\x02\x16\x44\x65\x65pMind.Alchemy.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dm_alchemy.protos.hypercube_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\026DeepMind.Alchemy.Proto'
  _globals['_HYPERCUBEVERTEX']._serialized_start=73
  _globals['_HYPERCUBEVERTEX']._serialized_end=126
  _globals['_EDGELABEL']._serialized_start=129
  _globals['_EDGELABEL']._serialized_end=306
  _globals['_EDGELABEL_DIRECTION']._serialized_start=243
  _globals['_EDGELABEL_DIRECTION']._serialized_end=306
# @@protoc_insertion_point(module_scope)
