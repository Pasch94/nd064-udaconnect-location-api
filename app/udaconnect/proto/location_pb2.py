# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='location.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0elocation.proto\"e\n\x08Location\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x11\n\tlongitude\x18\x03 \x01(\x02\x12\x10\n\x08latitude\x18\x04 \x01(\x02\x12\x15\n\rcreation_time\x18\x05 \x01(\x02\"\x1d\n\x0fLocationRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32U\n\x0fLocationService\x12\x1e\n\x06\x43reate\x12\t.Location\x1a\t.Location\x12\"\n\x03Get\x12\x10.LocationRequest\x1a\t.Locationb\x06proto3'
)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Location.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='Location.person_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Location.longitude', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Location.latitude', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='Location.creation_time', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=119,
)


_LOCATIONREQUEST = _descriptor.Descriptor(
  name='LocationRequest',
  full_name='LocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='LocationRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['LocationRequest'] = _LOCATIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  })
_sym_db.RegisterMessage(Location)

LocationRequest = _reflection.GeneratedProtocolMessageType('LocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONREQUEST,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:LocationRequest)
  })
_sym_db.RegisterMessage(LocationRequest)



_LOCATIONSERVICE = _descriptor.ServiceDescriptor(
  name='LocationService',
  full_name='LocationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=152,
  serialized_end=237,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='LocationService.Create',
    index=0,
    containing_service=None,
    input_type=_LOCATION,
    output_type=_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='LocationService.Get',
    index=1,
    containing_service=None,
    input_type=_LOCATIONREQUEST,
    output_type=_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATIONSERVICE)

DESCRIPTOR.services_by_name['LocationService'] = _LOCATIONSERVICE

# @@protoc_insertion_point(module_scope)
