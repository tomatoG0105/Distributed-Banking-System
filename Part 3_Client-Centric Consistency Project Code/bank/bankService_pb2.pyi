from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CustomerRequest(_message.Message):
    __slots__ = ["customer_id", "event", "amount"]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    customer_id: int
    event: str
    amount: int
    def __init__(self, customer_id: _Optional[int] = ..., event: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...

class BranchRequest(_message.Message):
    __slots__ = ["branch_id", "amount"]
    BRANCH_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    branch_id: int
    amount: int
    def __init__(self, branch_id: _Optional[int] = ..., amount: _Optional[int] = ...) -> None: ...

class ResponseMessage(_message.Message):
    __slots__ = ["message", "success"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    message: str
    success: bool
    def __init__(self, message: _Optional[str] = ..., success: bool = ...) -> None: ...

class BalanceQuery(_message.Message):
    __slots__ = ["branch_id"]
    BRANCH_ID_FIELD_NUMBER: _ClassVar[int]
    branch_id: int
    def __init__(self, branch_id: _Optional[int] = ...) -> None: ...
