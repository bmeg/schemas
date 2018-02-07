# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bmeg/variants.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bmeg import clinical_pb2 as bmeg_dot_clinical__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bmeg/variants.proto',
  package='bmeg',
  syntax='proto3',
  serialized_pb=_b('\n\x13\x62meg/variants.proto\x12\x04\x62meg\x1a\x13\x62meg/clinical.proto\"\xe0\x01\n\x12VariantSetMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0e\n\x06number\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12<\n\nattributes\x18\x08 \x03(\x0b\x32(.bmeg.VariantSetMetadata.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x80\x01\n\nVariantSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ndataset_id\x18\x03 \x01(\t\x12\x18\n\x10reference_set_id\x18\x04 \x01(\t\x12*\n\x08metadata\x18\x05 \x03(\x0b\x32\x18.bmeg.VariantSetMetadata\"\x94\x01\n\x07\x43\x61llSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\x03 \x01(\t\x12\x17\n\x0fvariant_set_ids\x18\x04 \x03(\t\x12\x0f\n\x07\x63reated\x18\x05 \x01(\x03\x12\x0f\n\x07updated\x18\x06 \x01(\x03\x12\x0e\n\x06method\x18\x07 \x01(\t\x12\x0e\n\x06source\x18\t \x01(\t\"\x97\x01\n\x04\x43\x61ll\x12\x15\n\rcall_set_name\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61ll_set_id\x18\x02 \x01(\t\x12\x0e\n\x06method\x18\x06 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\t \x01(\t\x12\x10\n\x08phaseset\x18\x04 \x01(\t\x12\x1b\n\x13genotype_likelihood\x18\x05 \x03(\x01\"\xfb\x02\n\x07Variant\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0evariant_set_id\x18\x02 \x01(\t\x12\r\n\x05names\x18\x03 \x03(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\x03\x12\x0f\n\x07updated\x18\x05 \x01(\x03\x12\x16\n\x0ereference_name\x18\x06 \x01(\t\x12\r\n\x05start\x18\x07 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x08 \x01(\x03\x12\x17\n\x0freference_bases\x18\t \x01(\t\x12\x17\n\x0f\x61lternate_bases\x18\n \x03(\t\x12\x19\n\x05\x63\x61lls\x18\x0c \x03(\x0b\x32\n.bmeg.Call\x12\x14\n\x0cvariant_type\x18\x11 \x01(\t\x12\r\n\x05svlen\x18\x12 \x01(\x03\x12\r\n\x05\x63ipos\x18\x13 \x03(\x11\x12\r\n\x05\x63iend\x18\x14 \x03(\x11\x12\x17\n\x0f\x66ilters_applied\x18\x0e \x01(\x08\x12\x16\n\x0e\x66ilters_passed\x18\x0f \x01(\x08\x12\x16\n\x0e\x66ilters_failed\x18\x10 \x03(\t\x12\x0e\n\x06source\x18\x15 \x01(\t\"p\n\x10TranscriptEffect\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nfeature_id\x18\x02 \x01(\t\x12\x17\n\x0f\x61lternate_bases\x18\x03 \x01(\t\x12#\n\x07\x65\x66\x66\x65\x63ts\x18\x04 \x03(\x0b\x32\x12.bmeg.OntologyTerm\"\x9b\x01\n\x11VariantAnnotation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nvariant_id\x18\x02 \x01(\t\x12!\n\x19variant_annotation_set_id\x18\x03 \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\t\x12\x32\n\x12transcript_effects\x18\x05 \x03(\x0b\x32\x16.bmeg.TranscriptEffectb\x06proto3')
  ,
  dependencies=[bmeg_dot_clinical__pb2.DESCRIPTOR,])




_VARIANTSETMETADATA_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='bmeg.VariantSetMetadata.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.VariantSetMetadata.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.VariantSetMetadata.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=275,
)

_VARIANTSETMETADATA = _descriptor.Descriptor(
  name='VariantSetMetadata',
  full_name='bmeg.VariantSetMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.VariantSetMetadata.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.VariantSetMetadata.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.VariantSetMetadata.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.VariantSetMetadata.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number', full_name='bmeg.VariantSetMetadata.number', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='bmeg.VariantSetMetadata.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='bmeg.VariantSetMetadata.attributes', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VARIANTSETMETADATA_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=275,
)


_VARIANTSET = _descriptor.Descriptor(
  name='VariantSet',
  full_name='bmeg.VariantSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.VariantSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.VariantSet.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='bmeg.VariantSet.dataset_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='bmeg.VariantSet.reference_set_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='bmeg.VariantSet.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=278,
  serialized_end=406,
)


_CALLSET = _descriptor.Descriptor(
  name='CallSet',
  full_name='bmeg.CallSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.CallSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.CallSet.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='bmeg.CallSet.biosample_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_set_ids', full_name='bmeg.CallSet.variant_set_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='bmeg.CallSet.created', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='bmeg.CallSet.updated', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='bmeg.CallSet.method', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.CallSet.source', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=409,
  serialized_end=557,
)


_CALL = _descriptor.Descriptor(
  name='Call',
  full_name='bmeg.Call',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_set_name', full_name='bmeg.Call.call_set_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_set_id', full_name='bmeg.Call.call_set_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='bmeg.Call.method', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.Call.source', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='bmeg.Call.biosample_id', index=4,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phaseset', full_name='bmeg.Call.phaseset', index=5,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genotype_likelihood', full_name='bmeg.Call.genotype_likelihood', index=6,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=560,
  serialized_end=711,
)


_VARIANT = _descriptor.Descriptor(
  name='Variant',
  full_name='bmeg.Variant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Variant.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_set_id', full_name='bmeg.Variant.variant_set_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='names', full_name='bmeg.Variant.names', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='bmeg.Variant.created', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='bmeg.Variant.updated', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='bmeg.Variant.reference_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='bmeg.Variant.start', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='bmeg.Variant.end', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_bases', full_name='bmeg.Variant.reference_bases', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternate_bases', full_name='bmeg.Variant.alternate_bases', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calls', full_name='bmeg.Variant.calls', index=10,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_type', full_name='bmeg.Variant.variant_type', index=11,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svlen', full_name='bmeg.Variant.svlen', index=12,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cipos', full_name='bmeg.Variant.cipos', index=13,
      number=19, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ciend', full_name='bmeg.Variant.ciend', index=14,
      number=20, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters_applied', full_name='bmeg.Variant.filters_applied', index=15,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters_passed', full_name='bmeg.Variant.filters_passed', index=16,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters_failed', full_name='bmeg.Variant.filters_failed', index=17,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.Variant.source', index=18,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=714,
  serialized_end=1093,
)


_TRANSCRIPTEFFECT = _descriptor.Descriptor(
  name='TranscriptEffect',
  full_name='bmeg.TranscriptEffect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.TranscriptEffect.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_id', full_name='bmeg.TranscriptEffect.feature_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternate_bases', full_name='bmeg.TranscriptEffect.alternate_bases', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effects', full_name='bmeg.TranscriptEffect.effects', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1095,
  serialized_end=1207,
)


_VARIANTANNOTATION = _descriptor.Descriptor(
  name='VariantAnnotation',
  full_name='bmeg.VariantAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.VariantAnnotation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_id', full_name='bmeg.VariantAnnotation.variant_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_annotation_set_id', full_name='bmeg.VariantAnnotation.variant_annotation_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='bmeg.VariantAnnotation.created', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transcript_effects', full_name='bmeg.VariantAnnotation.transcript_effects', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1210,
  serialized_end=1365,
)

_VARIANTSETMETADATA_ATTRIBUTESENTRY.containing_type = _VARIANTSETMETADATA
_VARIANTSETMETADATA.fields_by_name['attributes'].message_type = _VARIANTSETMETADATA_ATTRIBUTESENTRY
_VARIANTSET.fields_by_name['metadata'].message_type = _VARIANTSETMETADATA
_VARIANT.fields_by_name['calls'].message_type = _CALL
_TRANSCRIPTEFFECT.fields_by_name['effects'].message_type = bmeg_dot_clinical__pb2._ONTOLOGYTERM
_VARIANTANNOTATION.fields_by_name['transcript_effects'].message_type = _TRANSCRIPTEFFECT
DESCRIPTOR.message_types_by_name['VariantSetMetadata'] = _VARIANTSETMETADATA
DESCRIPTOR.message_types_by_name['VariantSet'] = _VARIANTSET
DESCRIPTOR.message_types_by_name['CallSet'] = _CALLSET
DESCRIPTOR.message_types_by_name['Call'] = _CALL
DESCRIPTOR.message_types_by_name['Variant'] = _VARIANT
DESCRIPTOR.message_types_by_name['TranscriptEffect'] = _TRANSCRIPTEFFECT
DESCRIPTOR.message_types_by_name['VariantAnnotation'] = _VARIANTANNOTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VariantSetMetadata = _reflection.GeneratedProtocolMessageType('VariantSetMetadata', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _VARIANTSETMETADATA_ATTRIBUTESENTRY,
    __module__ = 'bmeg.variants_pb2'
    # @@protoc_insertion_point(class_scope:bmeg.VariantSetMetadata.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _VARIANTSETMETADATA,
  __module__ = 'bmeg.variants_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.VariantSetMetadata)
  ))
_sym_db.RegisterMessage(VariantSetMetadata)
_sym_db.RegisterMessage(VariantSetMetadata.AttributesEntry)

VariantSet = _reflection.GeneratedProtocolMessageType('VariantSet', (_message.Message,), dict(
  DESCRIPTOR = _VARIANTSET,
  __module__ = 'bmeg.variants_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.VariantSet)
  ))
_sym_db.RegisterMessage(VariantSet)

CallSet = _reflection.GeneratedProtocolMessageType('CallSet', (_message.Message,), dict(
  DESCRIPTOR = _CALLSET,
  __module__ = 'bmeg.variants_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.CallSet)
  ))
_sym_db.RegisterMessage(CallSet)

Call = _reflection.GeneratedProtocolMessageType('Call', (_message.Message,), dict(
  DESCRIPTOR = _CALL,
  __module__ = 'bmeg.variants_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Call)
  ))
_sym_db.RegisterMessage(Call)

Variant = _reflection.GeneratedProtocolMessageType('Variant', (_message.Message,), dict(
  DESCRIPTOR = _VARIANT,
  __module__ = 'bmeg.variants_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Variant)
  ))
_sym_db.RegisterMessage(Variant)

TranscriptEffect = _reflection.GeneratedProtocolMessageType('TranscriptEffect', (_message.Message,), dict(
  DESCRIPTOR = _TRANSCRIPTEFFECT,
  __module__ = 'bmeg.variants_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.TranscriptEffect)
  ))
_sym_db.RegisterMessage(TranscriptEffect)

VariantAnnotation = _reflection.GeneratedProtocolMessageType('VariantAnnotation', (_message.Message,), dict(
  DESCRIPTOR = _VARIANTANNOTATION,
  __module__ = 'bmeg.variants_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.VariantAnnotation)
  ))
_sym_db.RegisterMessage(VariantAnnotation)


_VARIANTSETMETADATA_ATTRIBUTESENTRY.has_options = True
_VARIANTSETMETADATA_ATTRIBUTESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
