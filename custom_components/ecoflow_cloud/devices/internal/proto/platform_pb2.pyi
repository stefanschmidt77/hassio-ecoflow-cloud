"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PlCmdSets:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PlCmdSetsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PlCmdSets.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PL_NONE_CMD_SETS: _PlCmdSets.ValueType  # 0
    PL_BASIC_CMD_SETS: _PlCmdSets.ValueType  # 1
    PL_EXT_CMD_SETS: _PlCmdSets.ValueType  # 254

class PlCmdSets(_PlCmdSets, metaclass=_PlCmdSetsEnumTypeWrapper): ...

PL_NONE_CMD_SETS: PlCmdSets.ValueType  # 0
PL_BASIC_CMD_SETS: PlCmdSets.ValueType  # 1
PL_EXT_CMD_SETS: PlCmdSets.ValueType  # 254
global___PlCmdSets = PlCmdSets

class _PlCmdId:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PlCmdIdEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PlCmdId.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PL_CMD_ID_NONE: _PlCmdId.ValueType  # 0
    PL_CMD_ID_XLOG: _PlCmdId.ValueType  # 16
    PL_CMD_ID_WATTH: _PlCmdId.ValueType  # 32

class PlCmdId(_PlCmdId, metaclass=_PlCmdIdEnumTypeWrapper): ...

PL_CMD_ID_NONE: PlCmdId.ValueType  # 0
PL_CMD_ID_XLOG: PlCmdId.ValueType  # 16
PL_CMD_ID_WATTH: PlCmdId.ValueType  # 32
global___PlCmdId = PlCmdId

@typing.final
class EnergyItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    WATTH_TYPE_FIELD_NUMBER: builtins.int
    WATTH_FIELD_NUMBER: builtins.int
    timestamp: builtins.int
    watth_type: builtins.int
    @property
    def watth(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        timestamp: builtins.int | None = ...,
        watth_type: builtins.int | None = ...,
        watth: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_timestamp", b"_timestamp", "_watth_type", b"_watth_type", "timestamp", b"timestamp", "watth_type", b"watth_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_timestamp", b"_timestamp", "_watth_type", b"_watth_type", "timestamp", b"timestamp", "watth", b"watth", "watth_type", b"watth_type"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_timestamp", b"_timestamp"]) -> typing.Literal["timestamp"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_watth_type", b"_watth_type"]) -> typing.Literal["watth_type"] | None: ...

global___EnergyItem = EnergyItem

@typing.final
class EnergyTotalReport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WATTH_SEQ_FIELD_NUMBER: builtins.int
    WATTH_ITEM_FIELD_NUMBER: builtins.int
    watth_seq: builtins.int
    @property
    def watth_item(self) -> global___EnergyItem: ...
    def __init__(
        self,
        *,
        watth_seq: builtins.int | None = ...,
        watth_item: global___EnergyItem | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_watth_item", b"_watth_item", "_watth_seq", b"_watth_seq", "watth_item", b"watth_item", "watth_seq", b"watth_seq"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_watth_item", b"_watth_item", "_watth_seq", b"_watth_seq", "watth_item", b"watth_item", "watth_seq", b"watth_seq"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_watth_item", b"_watth_item"]) -> typing.Literal["watth_item"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_watth_seq", b"_watth_seq"]) -> typing.Literal["watth_seq"] | None: ...

global___EnergyTotalReport = EnergyTotalReport

@typing.final
class BatchEnergyTotalReport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WATTH_SEQ_FIELD_NUMBER: builtins.int
    WATTH_ITEM_FIELD_NUMBER: builtins.int
    watth_seq: builtins.int
    @property
    def watth_item(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EnergyItem]: ...
    def __init__(
        self,
        *,
        watth_seq: builtins.int | None = ...,
        watth_item: collections.abc.Iterable[global___EnergyItem] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_watth_seq", b"_watth_seq", "watth_seq", b"watth_seq"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_watth_seq", b"_watth_seq", "watth_item", b"watth_item", "watth_seq", b"watth_seq"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_watth_seq", b"_watth_seq"]) -> typing.Literal["watth_seq"] | None: ...

global___BatchEnergyTotalReport = BatchEnergyTotalReport

@typing.final
class EnergyTotalReportAck(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    WATTH_SEQ_FIELD_NUMBER: builtins.int
    WATTH_TYPE_FIELD_NUMBER: builtins.int
    result: builtins.int
    watth_seq: builtins.int
    watth_type: builtins.int
    def __init__(
        self,
        *,
        result: builtins.int | None = ...,
        watth_seq: builtins.int | None = ...,
        watth_type: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_result", b"_result", "_watth_seq", b"_watth_seq", "_watth_type", b"_watth_type", "result", b"result", "watth_seq", b"watth_seq", "watth_type", b"watth_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_result", b"_result", "_watth_seq", b"_watth_seq", "_watth_type", b"_watth_type", "result", b"result", "watth_seq", b"watth_seq", "watth_type", b"watth_type"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_result", b"_result"]) -> typing.Literal["result"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_watth_seq", b"_watth_seq"]) -> typing.Literal["watth_seq"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_watth_type", b"_watth_type"]) -> typing.Literal["watth_type"] | None: ...

global___EnergyTotalReportAck = EnergyTotalReportAck

@typing.final
class EventRecordItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    SYS_MS_FIELD_NUMBER: builtins.int
    EVENT_NO_FIELD_NUMBER: builtins.int
    EVENT_DETAIL_FIELD_NUMBER: builtins.int
    timestamp: builtins.int
    sys_ms: builtins.int
    event_no: builtins.int
    @property
    def event_detail(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        timestamp: builtins.int | None = ...,
        sys_ms: builtins.int | None = ...,
        event_no: builtins.int | None = ...,
        event_detail: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_event_no", b"_event_no", "_sys_ms", b"_sys_ms", "_timestamp", b"_timestamp", "event_no", b"event_no", "sys_ms", b"sys_ms", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_event_no", b"_event_no", "_sys_ms", b"_sys_ms", "_timestamp", b"_timestamp", "event_detail", b"event_detail", "event_no", b"event_no", "sys_ms", b"sys_ms", "timestamp", b"timestamp"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_event_no", b"_event_no"]) -> typing.Literal["event_no"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_sys_ms", b"_sys_ms"]) -> typing.Literal["sys_ms"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_timestamp", b"_timestamp"]) -> typing.Literal["timestamp"] | None: ...

global___EventRecordItem = EventRecordItem

@typing.final
class EventRecordReport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EVENT_VER_FIELD_NUMBER: builtins.int
    EVENT_SEQ_FIELD_NUMBER: builtins.int
    EVENT_ITEM_FIELD_NUMBER: builtins.int
    event_ver: builtins.int
    event_seq: builtins.int
    @property
    def event_item(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EventRecordItem]: ...
    def __init__(
        self,
        *,
        event_ver: builtins.int | None = ...,
        event_seq: builtins.int | None = ...,
        event_item: collections.abc.Iterable[global___EventRecordItem] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_event_seq", b"_event_seq", "_event_ver", b"_event_ver", "event_seq", b"event_seq", "event_ver", b"event_ver"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_event_seq", b"_event_seq", "_event_ver", b"_event_ver", "event_item", b"event_item", "event_seq", b"event_seq", "event_ver", b"event_ver"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_event_seq", b"_event_seq"]) -> typing.Literal["event_seq"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_event_ver", b"_event_ver"]) -> typing.Literal["event_ver"] | None: ...

global___EventRecordReport = EventRecordReport

@typing.final
class EventInfoReportAck(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    EVENT_SEQ_FIELD_NUMBER: builtins.int
    EVENT_ITEM_NUM_FIELD_NUMBER: builtins.int
    result: builtins.int
    event_seq: builtins.int
    event_item_num: builtins.int
    def __init__(
        self,
        *,
        result: builtins.int | None = ...,
        event_seq: builtins.int | None = ...,
        event_item_num: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_event_item_num", b"_event_item_num", "_event_seq", b"_event_seq", "_result", b"_result", "event_item_num", b"event_item_num", "event_seq", b"event_seq", "result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_event_item_num", b"_event_item_num", "_event_seq", b"_event_seq", "_result", b"_result", "event_item_num", b"event_item_num", "event_seq", b"event_seq", "result", b"result"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_event_item_num", b"_event_item_num"]) -> typing.Literal["event_item_num"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_event_seq", b"_event_seq"]) -> typing.Literal["event_seq"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_result", b"_result"]) -> typing.Literal["result"] | None: ...

global___EventInfoReportAck = EventInfoReportAck

@typing.final
class ProductNameSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_name", b"_name", "name", b"name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_name", b"_name", "name", b"name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_name", b"_name"]) -> typing.Literal["name"] | None: ...

global___ProductNameSet = ProductNameSet

@typing.final
class ProductNameSetAck(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    result: builtins.int
    def __init__(
        self,
        *,
        result: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_result", b"_result", "result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_result", b"_result", "result", b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_result", b"_result"]) -> typing.Literal["result"] | None: ...

global___ProductNameSetAck = ProductNameSetAck

@typing.final
class ProductNameGet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ProductNameGet = ProductNameGet

@typing.final
class ProductNameGetAck(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_name", b"_name", "name", b"name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_name", b"_name", "name", b"name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_name", b"_name"]) -> typing.Literal["name"] | None: ...

global___ProductNameGetAck = ProductNameGetAck

@typing.final
class RTCTimeGet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RTCTimeGet = RTCTimeGet

@typing.final
class RTCTimeGetAck(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    TIMEZONE_FIELD_NUMBER: builtins.int
    timestamp: builtins.int
    timezone: builtins.int
    def __init__(
        self,
        *,
        timestamp: builtins.int | None = ...,
        timezone: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_timestamp", b"_timestamp", "_timezone", b"_timezone", "timestamp", b"timestamp", "timezone", b"timezone"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_timestamp", b"_timestamp", "_timezone", b"_timezone", "timestamp", b"timestamp", "timezone", b"timezone"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_timestamp", b"_timestamp"]) -> typing.Literal["timestamp"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_timezone", b"_timezone"]) -> typing.Literal["timezone"] | None: ...

global___RTCTimeGetAck = RTCTimeGetAck

@typing.final
class RTCTimeSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    TIMEZONE_FIELD_NUMBER: builtins.int
    timestamp: builtins.int
    timezone: builtins.int
    def __init__(
        self,
        *,
        timestamp: builtins.int | None = ...,
        timezone: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_timestamp", b"_timestamp", "_timezone", b"_timezone", "timestamp", b"timestamp", "timezone", b"timezone"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_timestamp", b"_timestamp", "_timezone", b"_timezone", "timestamp", b"timestamp", "timezone", b"timezone"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_timestamp", b"_timestamp"]) -> typing.Literal["timestamp"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_timezone", b"_timezone"]) -> typing.Literal["timezone"] | None: ...

global___RTCTimeSet = RTCTimeSet

@typing.final
class RTCTimeSetAck(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    result: builtins.int
    def __init__(
        self,
        *,
        result: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_result", b"_result", "result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_result", b"_result", "result", b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_result", b"_result"]) -> typing.Literal["result"] | None: ...

global___RTCTimeSetAck = RTCTimeSetAck

@typing.final
class country_town_message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COUNTRY_FIELD_NUMBER: builtins.int
    TOWN_FIELD_NUMBER: builtins.int
    country: builtins.int
    town: builtins.int
    def __init__(
        self,
        *,
        country: builtins.int | None = ...,
        town: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_country", b"_country", "_town", b"_town", "country", b"country", "town", b"town"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_country", b"_country", "_town", b"_town", "country", b"country", "town", b"town"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_country", b"_country"]) -> typing.Literal["country"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_town", b"_town"]) -> typing.Literal["town"] | None: ...

global___country_town_message = country_town_message
