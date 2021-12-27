from typing import Any, Union

import orjson
from dataclasses_json import DataClassJsonMixin

def dataclass_json(cls: type):
    """
    A decorator to convert dataclasses to and from JSON. Provides the functions
    to_json() and from_json(json).
    Args:
        cls: The dataclass to decorate.
    """
    cls.to_json = _DataclassJson._to_json
    cls.from_json = classmethod(_DataclassJson._from_json.__func__)
    cls.from_dict = classmethod(DataClassJsonMixin.from_dict.__func__)

    return cls

class _DataclassJson:
    """
    A class to hold all the methods for properly decorating a class.
    """
    @staticmethod
    def _to_json(obj: Any) -> bytes:
        """
        Converts the dataclass to a JSON byte array.

        Args:
            obj: The instance of the dataclass to convert to JSON.

        Returns:
            The serialized form of the dataclass.
        """
        return orjson.dumps(
            obj,
            option=orjson.OPT_SERIALIZE_DATACLASS | orjson.OPT_SERIALIZE_NUMPY
        )

    @classmethod
    def _from_json(cls: type, obj: Union[bytes, str]) -> Any:
        """
        Converts serialized dataclass into the dataclass.

        Args:
            obj: The serialized dataclass to reform.

        Returns:
            The dataclass from the serialized data.
        """
        return cls.from_dict(orjson.loads(obj))
