# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bmeg/pathway.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bmeg/pathway.proto',
  package='bmeg',
  syntax='proto3',
  serialized_pb=_b('\n\x12\x62meg/pathway.proto\x12\x04\x62meg\"C\n\x12ProteinInteraction\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x0b\n\x03\x64st\x18\x02 \x01(\t\x12\x13\n\x0binteraction\x18\x03 \x01(\t\"\x15\n\x07Pathway\x12\n\n\x02id\x18\x01 \x01(\t\".\n\x0fProteinInstance\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07protein\x18\x02 \x01(\t\")\n\x07\x43omplex\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncomponents\x18\x02 \x03(\t\"E\n\x08Reaction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0binteraction\x18\x02 \x01(\t\x12\n\n\x02to\x18\x03 \x03(\t\x12\x0c\n\x04\x66rom\x18\x04 \x03(\t\"\x0b\n\tCatalysisb\x06proto3')
)




_PROTEININTERACTION = _descriptor.Descriptor(
  name='ProteinInteraction',
  full_name='bmeg.ProteinInteraction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='bmeg.ProteinInteraction.src', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst', full_name='bmeg.ProteinInteraction.dst', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interaction', full_name='bmeg.ProteinInteraction.interaction', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=95,
)


_PATHWAY = _descriptor.Descriptor(
  name='Pathway',
  full_name='bmeg.Pathway',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Pathway.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=118,
)


_PROTEININSTANCE = _descriptor.Descriptor(
  name='ProteinInstance',
  full_name='bmeg.ProteinInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.ProteinInstance.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protein', full_name='bmeg.ProteinInstance.protein', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=166,
)


_COMPLEX = _descriptor.Descriptor(
  name='Complex',
  full_name='bmeg.Complex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Complex.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='components', full_name='bmeg.Complex.components', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=209,
)


_REACTION = _descriptor.Descriptor(
  name='Reaction',
  full_name='bmeg.Reaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Reaction.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interaction', full_name='bmeg.Reaction.interaction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='bmeg.Reaction.to', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from', full_name='bmeg.Reaction.from', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=280,
)


_CATALYSIS = _descriptor.Descriptor(
  name='Catalysis',
  full_name='bmeg.Catalysis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=293,
)

DESCRIPTOR.message_types_by_name['ProteinInteraction'] = _PROTEININTERACTION
DESCRIPTOR.message_types_by_name['Pathway'] = _PATHWAY
DESCRIPTOR.message_types_by_name['ProteinInstance'] = _PROTEININSTANCE
DESCRIPTOR.message_types_by_name['Complex'] = _COMPLEX
DESCRIPTOR.message_types_by_name['Reaction'] = _REACTION
DESCRIPTOR.message_types_by_name['Catalysis'] = _CATALYSIS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProteinInteraction = _reflection.GeneratedProtocolMessageType('ProteinInteraction', (_message.Message,), dict(
  DESCRIPTOR = _PROTEININTERACTION,
  __module__ = 'bmeg.pathway_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.ProteinInteraction)
  ))
_sym_db.RegisterMessage(ProteinInteraction)

Pathway = _reflection.GeneratedProtocolMessageType('Pathway', (_message.Message,), dict(
  DESCRIPTOR = _PATHWAY,
  __module__ = 'bmeg.pathway_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Pathway)
  ))
_sym_db.RegisterMessage(Pathway)

ProteinInstance = _reflection.GeneratedProtocolMessageType('ProteinInstance', (_message.Message,), dict(
  DESCRIPTOR = _PROTEININSTANCE,
  __module__ = 'bmeg.pathway_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.ProteinInstance)
  ))
_sym_db.RegisterMessage(ProteinInstance)

Complex = _reflection.GeneratedProtocolMessageType('Complex', (_message.Message,), dict(
  DESCRIPTOR = _COMPLEX,
  __module__ = 'bmeg.pathway_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Complex)
  ))
_sym_db.RegisterMessage(Complex)

Reaction = _reflection.GeneratedProtocolMessageType('Reaction', (_message.Message,), dict(
  DESCRIPTOR = _REACTION,
  __module__ = 'bmeg.pathway_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Reaction)
  ))
_sym_db.RegisterMessage(Reaction)

Catalysis = _reflection.GeneratedProtocolMessageType('Catalysis', (_message.Message,), dict(
  DESCRIPTOR = _CATALYSIS,
  __module__ = 'bmeg.pathway_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Catalysis)
  ))
_sym_db.RegisterMessage(Catalysis)


# @@protoc_insertion_point(module_scope)
