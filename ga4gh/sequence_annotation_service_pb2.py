# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/sequence_annotation_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh import sequence_annotations_pb2 as ga4gh_dot_sequence__annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/sequence_annotation_service.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n\'ga4gh/sequence_annotation_service.proto\x12\x05ga4gh\x1a ga4gh/sequence_annotations.proto\"U\n\x18SearchFeatureSetsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"]\n\x19SearchFeatureSetsResponse\x12\'\n\x0c\x66\x65\x61ture_sets\x18\x01 \x03(\x0b\x32\x11.ga4gh.FeatureSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\".\n\x14GetFeatureSetRequest\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\"\xd7\x01\n\x15SearchFeaturesRequest\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bgene_symbol\x18\x03 \x01(\t\x12\x11\n\tparent_id\x18\x04 \x01(\t\x12\x16\n\x0ereference_name\x18\x05 \x01(\t\x12\r\n\x05start\x18\x06 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x07 \x01(\x03\x12\x15\n\rfeature_types\x18\x08 \x03(\t\x12\x11\n\tpage_size\x18\t \x01(\x05\x12\x12\n\npage_token\x18\n \x01(\t\"S\n\x16SearchFeaturesResponse\x12 \n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x0e.ga4gh.Feature\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\'\n\x11GetFeatureRequest\x12\x12\n\nfeature_id\x18\x01 \x01(\t2\xbb\x02\n\x19SequenceAnnotationService\x12V\n\x11SearchFeatureSets\x12\x1f.ga4gh.SearchFeatureSetsRequest\x1a .ga4gh.SearchFeatureSetsResponse\x12?\n\rGetFeatureSet\x12\x1b.ga4gh.GetFeatureSetRequest\x1a\x11.ga4gh.FeatureSet\x12M\n\x0eSearchFeatures\x12\x1c.ga4gh.SearchFeaturesRequest\x1a\x1d.ga4gh.SearchFeaturesResponse\x12\x36\n\nGetFeature\x12\x18.ga4gh.GetFeatureRequest\x1a\x0e.ga4gh.Featureb\x06proto3')
  ,
  dependencies=[ga4gh_dot_sequence__annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHFEATURESETSREQUEST = _descriptor.Descriptor(
  name='SearchFeatureSetsRequest',
  full_name='ga4gh.SearchFeatureSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.SearchFeatureSetsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchFeatureSetsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchFeatureSetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=84,
  serialized_end=169,
)


_SEARCHFEATURESETSRESPONSE = _descriptor.Descriptor(
  name='SearchFeatureSetsResponse',
  full_name='ga4gh.SearchFeatureSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_sets', full_name='ga4gh.SearchFeatureSetsResponse.feature_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchFeatureSetsResponse.next_page_token', index=1,
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
  serialized_start=171,
  serialized_end=264,
)


_GETFEATURESETREQUEST = _descriptor.Descriptor(
  name='GetFeatureSetRequest',
  full_name='ga4gh.GetFeatureSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_set_id', full_name='ga4gh.GetFeatureSetRequest.feature_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=266,
  serialized_end=312,
)


_SEARCHFEATURESREQUEST = _descriptor.Descriptor(
  name='SearchFeaturesRequest',
  full_name='ga4gh.SearchFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_set_id', full_name='ga4gh.SearchFeaturesRequest.feature_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.SearchFeaturesRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gene_symbol', full_name='ga4gh.SearchFeaturesRequest.gene_symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='ga4gh.SearchFeaturesRequest.parent_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='ga4gh.SearchFeaturesRequest.reference_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh.SearchFeaturesRequest.start', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh.SearchFeaturesRequest.end', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_types', full_name='ga4gh.SearchFeaturesRequest.feature_types', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchFeaturesRequest.page_size', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchFeaturesRequest.page_token', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=315,
  serialized_end=530,
)


_SEARCHFEATURESRESPONSE = _descriptor.Descriptor(
  name='SearchFeaturesResponse',
  full_name='ga4gh.SearchFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='ga4gh.SearchFeaturesResponse.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchFeaturesResponse.next_page_token', index=1,
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
  serialized_start=532,
  serialized_end=615,
)


_GETFEATUREREQUEST = _descriptor.Descriptor(
  name='GetFeatureRequest',
  full_name='ga4gh.GetFeatureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_id', full_name='ga4gh.GetFeatureRequest.feature_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=617,
  serialized_end=656,
)

_SEARCHFEATURESETSRESPONSE.fields_by_name['feature_sets'].message_type = ga4gh_dot_sequence__annotations__pb2._FEATURESET
_SEARCHFEATURESRESPONSE.fields_by_name['features'].message_type = ga4gh_dot_sequence__annotations__pb2._FEATURE
DESCRIPTOR.message_types_by_name['SearchFeatureSetsRequest'] = _SEARCHFEATURESETSREQUEST
DESCRIPTOR.message_types_by_name['SearchFeatureSetsResponse'] = _SEARCHFEATURESETSRESPONSE
DESCRIPTOR.message_types_by_name['GetFeatureSetRequest'] = _GETFEATURESETREQUEST
DESCRIPTOR.message_types_by_name['SearchFeaturesRequest'] = _SEARCHFEATURESREQUEST
DESCRIPTOR.message_types_by_name['SearchFeaturesResponse'] = _SEARCHFEATURESRESPONSE
DESCRIPTOR.message_types_by_name['GetFeatureRequest'] = _GETFEATUREREQUEST

SearchFeatureSetsRequest = _reflection.GeneratedProtocolMessageType('SearchFeatureSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESETSREQUEST,
  __module__ = 'ga4gh.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchFeatureSetsRequest)
  ))
_sym_db.RegisterMessage(SearchFeatureSetsRequest)

SearchFeatureSetsResponse = _reflection.GeneratedProtocolMessageType('SearchFeatureSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESETSRESPONSE,
  __module__ = 'ga4gh.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchFeatureSetsResponse)
  ))
_sym_db.RegisterMessage(SearchFeatureSetsResponse)

GetFeatureSetRequest = _reflection.GeneratedProtocolMessageType('GetFeatureSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEATURESETREQUEST,
  __module__ = 'ga4gh.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetFeatureSetRequest)
  ))
_sym_db.RegisterMessage(GetFeatureSetRequest)

SearchFeaturesRequest = _reflection.GeneratedProtocolMessageType('SearchFeaturesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESREQUEST,
  __module__ = 'ga4gh.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchFeaturesRequest)
  ))
_sym_db.RegisterMessage(SearchFeaturesRequest)

SearchFeaturesResponse = _reflection.GeneratedProtocolMessageType('SearchFeaturesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESRESPONSE,
  __module__ = 'ga4gh.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchFeaturesResponse)
  ))
_sym_db.RegisterMessage(SearchFeaturesResponse)

GetFeatureRequest = _reflection.GeneratedProtocolMessageType('GetFeatureRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEATUREREQUEST,
  __module__ = 'ga4gh.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetFeatureRequest)
  ))
_sym_db.RegisterMessage(GetFeatureRequest)


# @@protoc_insertion_point(module_scope)
