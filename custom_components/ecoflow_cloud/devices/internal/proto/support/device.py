from typing import Any, cast

from homeassistant.util import dt

from .....api.message import JSONDict, JSONMessage, Message
from .....devices.data_holder import DeviceOfflineError
from .const import AddressId, Command
from .message import ProtoMessage


class PrivateAPIProtoDeviceMixin(object):
    def private_api_extract_quota_message(self, message: JSONDict) -> dict[str, Any]:
        if "cmdFunc" in message and "cmdId" in message:
            if (
                message["cmdFunc"] == Command.PRIVATE_API_POWERSTREAM_HEARTBEAT.func
                and message["cmdId"] == Command.PRIVATE_API_POWERSTREAM_HEARTBEAT.id
            ):
                return {"params": message["params"], "time": dt.utcnow()}
            elif (
                message["cmdFunc"] == Command.PRIVATE_API_NULL_COMMAND.func
                and message["cmdId"] == Command.PRIVATE_API_NULL_COMMAND.id
                and message.get("code") == "-2"
            ):
                raise DeviceOfflineError()

        raise ValueError("not a quota message")

    def private_api_get_quota(self) -> Message:
        json_prepared_payload = JSONMessage.prepare_payload({})

        return ProtoMessage(
            src=AddressId.APP,
            dest=AddressId.APP,
            from_=cast(str, json_prepared_payload["from"]),
        )
