import phonenumbers as phonenumbers
from phonenumbers.phonenumber import PhoneNumber as BasePhoneNumber
from phonenumbers.phonenumberutil import NumberParseException
from sqlalchemy import exc
from sqlalchemy import types

from ..exceptions import ImproperlyConfigured as ImproperlyConfigured
from ..utils import str_coercible as str_coercible

class PhoneNumberParseException(NumberParseException, exc.DontWrapMixin): ...

class PhoneNumber(BasePhoneNumber):
    region: str
    national: str
    international: str
    e164: str
    def __init__(self, raw_number: str, region: str | None = None, check_region: bool = True) -> None: ...
    def is_valid_number(self) -> bool: ...

class PhoneNumberType(types.TypeDecorator[PhoneNumber]):
    STORE_FORMAT: str
    impl: types.Unicode
    python_type: type[PhoneNumber]
    def __init__(self, region: str = "US", max_length: int = 20, *args, **kwargs) -> None: ...
