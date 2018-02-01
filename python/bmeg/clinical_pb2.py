# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bmeg/clinical.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bmeg/clinical.proto',
  package='bmeg',
  syntax='proto3',
  serialized_pb=_b('\n\x13\x62meg/clinical.proto\x12\x04\x62meg\x1a\x1cgoogle/protobuf/struct.proto\"-\n\x0cOntologyTerm\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\t\"\xf4\x01\n\nIndividual\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0f\n\x07\x63reated\x18\x05 \x01(\t\x12\x0f\n\x07updated\x18\x06 \x01(\t\x12#\n\x07species\x18\x07 \x01(\x0b\x32\x12.bmeg.OntologyTerm\x12\x1f\n\x03sex\x18\x08 \x01(\x0b\x32\x12.bmeg.OntologyTerm\x12\x0e\n\x06source\x18\t \x01(\t\x12+\n\nattributes\x18\n \x01(\x0b\x32\x17.google.protobuf.Struct\"\x8f\x02\n\tBiosample\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12#\n\x07\x64isease\x18\x05 \x01(\x0b\x32\x12.bmeg.OntologyTerm\x12\x0f\n\x07\x63reated\x18\x06 \x01(\t\x12\x0f\n\x07updated\x18\x07 \x01(\t\x12\x15\n\rindividual_id\x18\x08 \x01(\t\x12\x0e\n\x06source\x18\t \x01(\t\x12+\n\nattributes\x18\n \x01(\x0b\x32\x17.google.protobuf.Struct\x12$\n\x1cindividual_age_at_collection\x18\x0b \x01(\t\"\x8e\x01\n\x0b\x44rugTherapy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rindividual_id\x18\x03 \x01(\t\x12\x11\n\tdrug_name\x18\x04 \x01(\t\x12\x12\n\npubchem_id\x18\x05 \x01(\t\x12\x17\n\x0fprescribed_dose\x18\x06 \x01(\t\x12\x0e\n\x06source\x18\x07 \x01(\t\"g\n\x10RadiationTherapy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rindividual_id\x18\x03 \x01(\t\x12\x12\n\ntotal_dose\x18\x04 \x01(\x02\x12\x0e\n\x06source\x18\x05 \x01(\t\"\x9d\x01\n\x10\x43linicalFollowup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rindividual_id\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\r\n\x05\x65vent\x18\x05 \x01(\t\x12\x15\n\rdays_to_death\x18\x06 \x01(\x05\x12\x14\n\x0cvital_status\x18\x07 \x01(\t\x12\x0e\n\x06source\x18\x08 \x01(\t\"\\\n\x06\x43ohort\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x11\n\thasSample\x18\x07 \x03(\t\"f\n\x10IndividualCohort\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x11\n\thasMember\x18\x07 \x03(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_ONTOLOGYTERM = _descriptor.Descriptor(
  name='OntologyTerm',
  full_name='bmeg.OntologyTerm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term_id', full_name='bmeg.OntologyTerm.term_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='term', full_name='bmeg.OntologyTerm.term', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=104,
)


_INDIVIDUAL = _descriptor.Descriptor(
  name='Individual',
  full_name='bmeg.Individual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Individual.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='bmeg.Individual.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.Individual.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='bmeg.Individual.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='bmeg.Individual.created', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='bmeg.Individual.updated', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='species', full_name='bmeg.Individual.species', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sex', full_name='bmeg.Individual.sex', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.Individual.source', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='bmeg.Individual.attributes', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=107,
  serialized_end=351,
)


_BIOSAMPLE = _descriptor.Descriptor(
  name='Biosample',
  full_name='bmeg.Biosample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Biosample.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='bmeg.Biosample.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.Biosample.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='bmeg.Biosample.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disease', full_name='bmeg.Biosample.disease', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='bmeg.Biosample.created', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='bmeg.Biosample.updated', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='bmeg.Biosample.individual_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.Biosample.source', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='bmeg.Biosample.attributes', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_age_at_collection', full_name='bmeg.Biosample.individual_age_at_collection', index=10,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=354,
  serialized_end=625,
)


_DRUGTHERAPY = _descriptor.Descriptor(
  name='DrugTherapy',
  full_name='bmeg.DrugTherapy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.DrugTherapy.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.DrugTherapy.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='bmeg.DrugTherapy.individual_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drug_name', full_name='bmeg.DrugTherapy.drug_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pubchem_id', full_name='bmeg.DrugTherapy.pubchem_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prescribed_dose', full_name='bmeg.DrugTherapy.prescribed_dose', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.DrugTherapy.source', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=628,
  serialized_end=770,
)


_RADIATIONTHERAPY = _descriptor.Descriptor(
  name='RadiationTherapy',
  full_name='bmeg.RadiationTherapy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.RadiationTherapy.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.RadiationTherapy.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='bmeg.RadiationTherapy.individual_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_dose', full_name='bmeg.RadiationTherapy.total_dose', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.RadiationTherapy.source', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=772,
  serialized_end=875,
)


_CLINICALFOLLOWUP = _descriptor.Descriptor(
  name='ClinicalFollowup',
  full_name='bmeg.ClinicalFollowup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.ClinicalFollowup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.ClinicalFollowup.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='bmeg.ClinicalFollowup.individual_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='bmeg.ClinicalFollowup.date', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='bmeg.ClinicalFollowup.event', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='days_to_death', full_name='bmeg.ClinicalFollowup.days_to_death', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vital_status', full_name='bmeg.ClinicalFollowup.vital_status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.ClinicalFollowup.source', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=878,
  serialized_end=1035,
)


_COHORT = _descriptor.Descriptor(
  name='Cohort',
  full_name='bmeg.Cohort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Cohort.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.Cohort.name', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='bmeg.Cohort.location', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='bmeg.Cohort.description', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasSample', full_name='bmeg.Cohort.hasSample', index=4,
      number=7, type=9, cpp_type=9, label=3,
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
  serialized_start=1037,
  serialized_end=1129,
)


_INDIVIDUALCOHORT = _descriptor.Descriptor(
  name='IndividualCohort',
  full_name='bmeg.IndividualCohort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.IndividualCohort.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.IndividualCohort.name', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='bmeg.IndividualCohort.location', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='bmeg.IndividualCohort.description', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasMember', full_name='bmeg.IndividualCohort.hasMember', index=4,
      number=7, type=9, cpp_type=9, label=3,
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
  serialized_start=1131,
  serialized_end=1233,
)

_INDIVIDUAL.fields_by_name['species'].message_type = _ONTOLOGYTERM
_INDIVIDUAL.fields_by_name['sex'].message_type = _ONTOLOGYTERM
_INDIVIDUAL.fields_by_name['attributes'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BIOSAMPLE.fields_by_name['disease'].message_type = _ONTOLOGYTERM
_BIOSAMPLE.fields_by_name['attributes'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['OntologyTerm'] = _ONTOLOGYTERM
DESCRIPTOR.message_types_by_name['Individual'] = _INDIVIDUAL
DESCRIPTOR.message_types_by_name['Biosample'] = _BIOSAMPLE
DESCRIPTOR.message_types_by_name['DrugTherapy'] = _DRUGTHERAPY
DESCRIPTOR.message_types_by_name['RadiationTherapy'] = _RADIATIONTHERAPY
DESCRIPTOR.message_types_by_name['ClinicalFollowup'] = _CLINICALFOLLOWUP
DESCRIPTOR.message_types_by_name['Cohort'] = _COHORT
DESCRIPTOR.message_types_by_name['IndividualCohort'] = _INDIVIDUALCOHORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OntologyTerm = _reflection.GeneratedProtocolMessageType('OntologyTerm', (_message.Message,), dict(
  DESCRIPTOR = _ONTOLOGYTERM,
  __module__ = 'bmeg.clinical_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.OntologyTerm)
  ))
_sym_db.RegisterMessage(OntologyTerm)

Individual = _reflection.GeneratedProtocolMessageType('Individual', (_message.Message,), dict(
  DESCRIPTOR = _INDIVIDUAL,
  __module__ = 'bmeg.clinical_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Individual)
  ))
_sym_db.RegisterMessage(Individual)

Biosample = _reflection.GeneratedProtocolMessageType('Biosample', (_message.Message,), dict(
  DESCRIPTOR = _BIOSAMPLE,
  __module__ = 'bmeg.clinical_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Biosample)
  ))
_sym_db.RegisterMessage(Biosample)

DrugTherapy = _reflection.GeneratedProtocolMessageType('DrugTherapy', (_message.Message,), dict(
  DESCRIPTOR = _DRUGTHERAPY,
  __module__ = 'bmeg.clinical_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.DrugTherapy)
  ))
_sym_db.RegisterMessage(DrugTherapy)

RadiationTherapy = _reflection.GeneratedProtocolMessageType('RadiationTherapy', (_message.Message,), dict(
  DESCRIPTOR = _RADIATIONTHERAPY,
  __module__ = 'bmeg.clinical_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.RadiationTherapy)
  ))
_sym_db.RegisterMessage(RadiationTherapy)

ClinicalFollowup = _reflection.GeneratedProtocolMessageType('ClinicalFollowup', (_message.Message,), dict(
  DESCRIPTOR = _CLINICALFOLLOWUP,
  __module__ = 'bmeg.clinical_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.ClinicalFollowup)
  ))
_sym_db.RegisterMessage(ClinicalFollowup)

Cohort = _reflection.GeneratedProtocolMessageType('Cohort', (_message.Message,), dict(
  DESCRIPTOR = _COHORT,
  __module__ = 'bmeg.clinical_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Cohort)
  ))
_sym_db.RegisterMessage(Cohort)

IndividualCohort = _reflection.GeneratedProtocolMessageType('IndividualCohort', (_message.Message,), dict(
  DESCRIPTOR = _INDIVIDUALCOHORT,
  __module__ = 'bmeg.clinical_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.IndividualCohort)
  ))
_sym_db.RegisterMessage(IndividualCohort)


# @@protoc_insertion_point(module_scope)