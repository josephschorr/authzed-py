# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v1/core.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61uthzed/api/v1/core.proto\x12\x0e\x61uthzed.api.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17validate/validate.proto\"\xb9\x02\n\x0cRelationship\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x08resource\x12\x43\n\x08relation\x18\x02 \x01(\tB\'\xfa\x42$r\"(@2\x1e^[a-z][a-z0-9_]{1,62}[a-z0-9]$R\x08relation\x12\x44\n\x07subject\x18\x03 \x01(\x0b\x32 .authzed.api.v1.SubjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\x12W\n\x0foptional_caveat\x18\x04 \x01(\x0b\x32$.authzed.api.v1.ContextualizedCaveatB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x0eoptionalCaveat\"\xa6\x01\n\x14\x43ontextualizedCaveat\x12Q\n\x0b\x63\x61veat_name\x18\x01 \x01(\tB0\xfa\x42-r+(\x80\x01\x32&^([a-zA-Z0-9_][a-zA-Z0-9/_|-]{0,127})$R\ncaveatName\x12;\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x07\x63ontext\"\xae\x01\n\x10SubjectReference\x12\x41\n\x06object\x18\x01 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x06object\x12W\n\x11optional_relation\x18\x02 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\x10optionalRelation\"\xc4\x01\n\x0fObjectReference\x12i\n\x0bobject_type\x18\x01 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$R\nobjectType\x12\x46\n\tobject_id\x18\x02 \x01(\tB)\xfa\x42&r$(\x80\x08\x32\x1f^(([a-zA-Z0-9/_|\\-=+]{1,})|\\*)$R\x08objectId\")\n\x08ZedToken\x12\x1d\n\x05token\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x01R\x05token\"+\n\x06\x43ursor\x12!\n\x05token\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06 \x01(\x80\xa0\x06R\x05token\"\xa1\x02\n\x12RelationshipUpdate\x12V\n\toperation\x18\x01 \x01(\x0e\x32,.authzed.api.v1.RelationshipUpdate.OperationB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\toperation\x12J\n\x0crelationship\x18\x02 \x01(\x0b\x32\x1c.authzed.api.v1.RelationshipB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x0crelationship\"g\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x14\n\x10OPERATION_CREATE\x10\x01\x12\x13\n\x0fOPERATION_TOUCH\x10\x02\x12\x14\n\x10OPERATION_DELETE\x10\x03\"\xa8\x02\n\x1aPermissionRelationshipTree\x12I\n\x0cintermediate\x18\x01 \x01(\x0b\x32#.authzed.api.v1.AlgebraicSubjectSetH\x00R\x0cintermediate\x12\x36\n\x04leaf\x18\x02 \x01(\x0b\x32 .authzed.api.v1.DirectSubjectSetH\x00R\x04leaf\x12H\n\x0f\x65xpanded_object\x18\x03 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceR\x0e\x65xpandedObject\x12+\n\x11\x65xpanded_relation\x18\x04 \x01(\tR\x10\x65xpandedRelationB\x10\n\ttree_type\x12\x03\xf8\x42\x01\"\xb7\x02\n\x13\x41lgebraicSubjectSet\x12W\n\toperation\x18\x01 \x01(\x0e\x32-.authzed.api.v1.AlgebraicSubjectSet.OperationB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\toperation\x12U\n\x08\x63hildren\x18\x02 \x03(\x0b\x32*.authzed.api.v1.PermissionRelationshipTreeB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x08\x63hildren\"p\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x13\n\x0fOPERATION_UNION\x10\x01\x12\x1a\n\x16OPERATION_INTERSECTION\x10\x02\x12\x17\n\x13OPERATION_EXCLUSION\x10\x03\"P\n\x10\x44irectSubjectSet\x12<\n\x08subjects\x18\x01 \x03(\x0b\x32 .authzed.api.v1.SubjectReferenceR\x08subjects\"W\n\x11PartialCaveatInfo\x12\x42\n\x18missing_required_context\x18\x01 \x03(\tB\x08\xfa\x42\x05\x92\x01\x02\x08\x01R\x16missingRequiredContextBH\n\x12\x63om.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1.core_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1'
  _RELATIONSHIP.fields_by_name['resource']._options = None
  _RELATIONSHIP.fields_by_name['resource']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RELATIONSHIP.fields_by_name['relation']._options = None
  _RELATIONSHIP.fields_by_name['relation']._serialized_options = b'\372B$r\"(@2\036^[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _RELATIONSHIP.fields_by_name['subject']._options = None
  _RELATIONSHIP.fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RELATIONSHIP.fields_by_name['optional_caveat']._options = None
  _RELATIONSHIP.fields_by_name['optional_caveat']._serialized_options = b'\372B\005\212\001\002\020\000'
  _CONTEXTUALIZEDCAVEAT.fields_by_name['caveat_name']._options = None
  _CONTEXTUALIZEDCAVEAT.fields_by_name['caveat_name']._serialized_options = b'\372B-r+(\200\0012&^([a-zA-Z0-9_][a-zA-Z0-9/_|-]{0,127})$'
  _CONTEXTUALIZEDCAVEAT.fields_by_name['context']._options = None
  _CONTEXTUALIZEDCAVEAT.fields_by_name['context']._serialized_options = b'\372B\005\212\001\002\020\000'
  _SUBJECTREFERENCE.fields_by_name['object']._options = None
  _SUBJECTREFERENCE.fields_by_name['object']._serialized_options = b'\372B\005\212\001\002\020\001'
  _SUBJECTREFERENCE.fields_by_name['optional_relation']._options = None
  _SUBJECTREFERENCE.fields_by_name['optional_relation']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _OBJECTREFERENCE.fields_by_name['object_type']._options = None
  _OBJECTREFERENCE.fields_by_name['object_type']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _OBJECTREFERENCE.fields_by_name['object_id']._options = None
  _OBJECTREFERENCE.fields_by_name['object_id']._serialized_options = b'\372B&r$(\200\0102\037^(([a-zA-Z0-9/_|\\-=+]{1,})|\\*)$'
  _ZEDTOKEN.fields_by_name['token']._options = None
  _ZEDTOKEN.fields_by_name['token']._serialized_options = b'\372B\004r\002 \001'
  _CURSOR.fields_by_name['token']._options = None
  _CURSOR.fields_by_name['token']._serialized_options = b'\372B\010r\006 \001(\200\240\006'
  _RELATIONSHIPUPDATE.fields_by_name['operation']._options = None
  _RELATIONSHIPUPDATE.fields_by_name['operation']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _RELATIONSHIPUPDATE.fields_by_name['relationship']._options = None
  _RELATIONSHIPUPDATE.fields_by_name['relationship']._serialized_options = b'\372B\005\212\001\002\020\001'
  _PERMISSIONRELATIONSHIPTREE.oneofs_by_name['tree_type']._options = None
  _PERMISSIONRELATIONSHIPTREE.oneofs_by_name['tree_type']._serialized_options = b'\370B\001'
  _ALGEBRAICSUBJECTSET.fields_by_name['operation']._options = None
  _ALGEBRAICSUBJECTSET.fields_by_name['operation']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _ALGEBRAICSUBJECTSET.fields_by_name['children']._options = None
  _ALGEBRAICSUBJECTSET.fields_by_name['children']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _PARTIALCAVEATINFO.fields_by_name['missing_required_context']._options = None
  _PARTIALCAVEATINFO.fields_by_name['missing_required_context']._serialized_options = b'\372B\005\222\001\002\010\001'
  _globals['_RELATIONSHIP']._serialized_start=101
  _globals['_RELATIONSHIP']._serialized_end=414
  _globals['_CONTEXTUALIZEDCAVEAT']._serialized_start=417
  _globals['_CONTEXTUALIZEDCAVEAT']._serialized_end=583
  _globals['_SUBJECTREFERENCE']._serialized_start=586
  _globals['_SUBJECTREFERENCE']._serialized_end=760
  _globals['_OBJECTREFERENCE']._serialized_start=763
  _globals['_OBJECTREFERENCE']._serialized_end=959
  _globals['_ZEDTOKEN']._serialized_start=961
  _globals['_ZEDTOKEN']._serialized_end=1002
  _globals['_CURSOR']._serialized_start=1004
  _globals['_CURSOR']._serialized_end=1047
  _globals['_RELATIONSHIPUPDATE']._serialized_start=1050
  _globals['_RELATIONSHIPUPDATE']._serialized_end=1339
  _globals['_RELATIONSHIPUPDATE_OPERATION']._serialized_start=1236
  _globals['_RELATIONSHIPUPDATE_OPERATION']._serialized_end=1339
  _globals['_PERMISSIONRELATIONSHIPTREE']._serialized_start=1342
  _globals['_PERMISSIONRELATIONSHIPTREE']._serialized_end=1638
  _globals['_ALGEBRAICSUBJECTSET']._serialized_start=1641
  _globals['_ALGEBRAICSUBJECTSET']._serialized_end=1952
  _globals['_ALGEBRAICSUBJECTSET_OPERATION']._serialized_start=1840
  _globals['_ALGEBRAICSUBJECTSET_OPERATION']._serialized_end=1952
  _globals['_DIRECTSUBJECTSET']._serialized_start=1954
  _globals['_DIRECTSUBJECTSET']._serialized_end=2034
  _globals['_PARTIALCAVEATINFO']._serialized_start=2036
  _globals['_PARTIALCAVEATINFO']._serialized_end=2123
# @@protoc_insertion_point(module_scope)
