# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from arrakisapi.api.core_pb2 import (
    ObjectAndRelation as arrakisapi___api___core_pb2___ObjectAndRelation,
    RelationTuple as arrakisapi___api___core_pb2___RelationTuple,
    RelationTupleTreeNode as arrakisapi___api___core_pb2___RelationTupleTreeNode,
    RelationTupleUpdate as arrakisapi___api___core_pb2___RelationTupleUpdate,
    User as arrakisapi___api___core_pb2___User,
    Zookie as arrakisapi___api___core_pb2___Zookie,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class RelationTupleFilter(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FilterValue = typing___NewType('FilterValue', builtin___int)
    type___FilterValue = FilterValue
    Filter: _Filter
    class _Filter(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[RelationTupleFilter.FilterValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNKNOWN = typing___cast(RelationTupleFilter.FilterValue, 0)
        OBJECT_ID = typing___cast(RelationTupleFilter.FilterValue, 1)
        RELATION = typing___cast(RelationTupleFilter.FilterValue, 2)
        USER_ID = typing___cast(RelationTupleFilter.FilterValue, 3)
        USERSET = typing___cast(RelationTupleFilter.FilterValue, 4)
    UNKNOWN = typing___cast(RelationTupleFilter.FilterValue, 0)
    OBJECT_ID = typing___cast(RelationTupleFilter.FilterValue, 1)
    RELATION = typing___cast(RelationTupleFilter.FilterValue, 2)
    USER_ID = typing___cast(RelationTupleFilter.FilterValue, 3)
    USERSET = typing___cast(RelationTupleFilter.FilterValue, 4)
    type___Filter = Filter

    namespace: typing___Text = ...
    object_id: typing___Text = ...
    relation: typing___Text = ...
    user_id: typing___Text = ...
    filters: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___RelationTupleFilter.FilterValue] = ...

    @property
    def userset(self) -> arrakisapi___api___core_pb2___ObjectAndRelation: ...

    def __init__(self,
        *,
        namespace : typing___Optional[typing___Text] = None,
        object_id : typing___Optional[typing___Text] = None,
        relation : typing___Optional[typing___Text] = None,
        user_id : typing___Optional[typing___Text] = None,
        userset : typing___Optional[arrakisapi___api___core_pb2___ObjectAndRelation] = None,
        filters : typing___Optional[typing___Iterable[type___RelationTupleFilter.FilterValue]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"userset",b"userset"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"filters",b"filters",u"namespace",b"namespace",u"object_id",b"object_id",u"relation",b"relation",u"user_id",b"user_id",u"userset",b"userset"]) -> None: ...
type___RelationTupleFilter = RelationTupleFilter

class ReadRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def tuplesets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___RelationTupleFilter]: ...

    @property
    def at_revision(self) -> arrakisapi___api___core_pb2___Zookie: ...

    def __init__(self,
        *,
        tuplesets : typing___Optional[typing___Iterable[type___RelationTupleFilter]] = None,
        at_revision : typing___Optional[arrakisapi___api___core_pb2___Zookie] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"at_revision",b"at_revision"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"at_revision",b"at_revision",u"tuplesets",b"tuplesets"]) -> None: ...
type___ReadRequest = ReadRequest

class ReadResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Tupleset(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def tuples(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[arrakisapi___api___core_pb2___RelationTuple]: ...

        def __init__(self,
            *,
            tuples : typing___Optional[typing___Iterable[arrakisapi___api___core_pb2___RelationTuple]] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"tuples",b"tuples"]) -> None: ...
    type___Tupleset = Tupleset


    @property
    def tuplesets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ReadResponse.Tupleset]: ...

    @property
    def revision(self) -> arrakisapi___api___core_pb2___Zookie: ...

    def __init__(self,
        *,
        tuplesets : typing___Optional[typing___Iterable[type___ReadResponse.Tupleset]] = None,
        revision : typing___Optional[arrakisapi___api___core_pb2___Zookie] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"revision",b"revision"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"revision",b"revision",u"tuplesets",b"tuplesets"]) -> None: ...
type___ReadResponse = ReadResponse

class WriteRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def write_conditions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[arrakisapi___api___core_pb2___RelationTuple]: ...

    @property
    def updates(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[arrakisapi___api___core_pb2___RelationTupleUpdate]: ...

    def __init__(self,
        *,
        write_conditions : typing___Optional[typing___Iterable[arrakisapi___api___core_pb2___RelationTuple]] = None,
        updates : typing___Optional[typing___Iterable[arrakisapi___api___core_pb2___RelationTupleUpdate]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"updates",b"updates",u"write_conditions",b"write_conditions"]) -> None: ...
type___WriteRequest = WriteRequest

class WriteResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def revision(self) -> arrakisapi___api___core_pb2___Zookie: ...

    def __init__(self,
        *,
        revision : typing___Optional[arrakisapi___api___core_pb2___Zookie] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"revision",b"revision"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"revision",b"revision"]) -> None: ...
type___WriteResponse = WriteResponse

class CheckRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def test_userset(self) -> arrakisapi___api___core_pb2___ObjectAndRelation: ...

    @property
    def user(self) -> arrakisapi___api___core_pb2___User: ...

    @property
    def at_revision(self) -> arrakisapi___api___core_pb2___Zookie: ...

    def __init__(self,
        *,
        test_userset : typing___Optional[arrakisapi___api___core_pb2___ObjectAndRelation] = None,
        user : typing___Optional[arrakisapi___api___core_pb2___User] = None,
        at_revision : typing___Optional[arrakisapi___api___core_pb2___Zookie] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"at_revision",b"at_revision",u"test_userset",b"test_userset",u"user",b"user"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"at_revision",b"at_revision",u"test_userset",b"test_userset",u"user",b"user"]) -> None: ...
type___CheckRequest = CheckRequest

class ContentChangeCheckRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def test_userset(self) -> arrakisapi___api___core_pb2___ObjectAndRelation: ...

    @property
    def user(self) -> arrakisapi___api___core_pb2___User: ...

    def __init__(self,
        *,
        test_userset : typing___Optional[arrakisapi___api___core_pb2___ObjectAndRelation] = None,
        user : typing___Optional[arrakisapi___api___core_pb2___User] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"test_userset",b"test_userset",u"user",b"user"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"test_userset",b"test_userset",u"user",b"user"]) -> None: ...
type___ContentChangeCheckRequest = ContentChangeCheckRequest

class CheckResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_member: builtin___bool = ...

    @property
    def revision(self) -> arrakisapi___api___core_pb2___Zookie: ...

    def __init__(self,
        *,
        is_member : typing___Optional[builtin___bool] = None,
        revision : typing___Optional[arrakisapi___api___core_pb2___Zookie] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"revision",b"revision"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"is_member",b"is_member",u"revision",b"revision"]) -> None: ...
type___CheckResponse = CheckResponse

class ExpandRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def userset(self) -> arrakisapi___api___core_pb2___ObjectAndRelation: ...

    @property
    def at_revision(self) -> arrakisapi___api___core_pb2___Zookie: ...

    def __init__(self,
        *,
        userset : typing___Optional[arrakisapi___api___core_pb2___ObjectAndRelation] = None,
        at_revision : typing___Optional[arrakisapi___api___core_pb2___Zookie] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"at_revision",b"at_revision",u"userset",b"userset"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"at_revision",b"at_revision",u"userset",b"userset"]) -> None: ...
type___ExpandRequest = ExpandRequest

class ExpandResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def tree_node(self) -> arrakisapi___api___core_pb2___RelationTupleTreeNode: ...

    @property
    def revision(self) -> arrakisapi___api___core_pb2___Zookie: ...

    def __init__(self,
        *,
        tree_node : typing___Optional[arrakisapi___api___core_pb2___RelationTupleTreeNode] = None,
        revision : typing___Optional[arrakisapi___api___core_pb2___Zookie] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"revision",b"revision",u"tree_node",b"tree_node"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"revision",b"revision",u"tree_node",b"tree_node"]) -> None: ...
type___ExpandResponse = ExpandResponse