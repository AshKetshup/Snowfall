from datetime import datetime, timezone

from .helpers import generateTimestamp, waitUntilNextTimestamp
from .snowfallConfig import SnowfallConfig


class ErrorSettingTimestampException(Exception):
    """Exception describing an error while setting a timestamp."""

    EXCEPTION_MESSAGE: str = "CLOCK IS RUNNING BACKWARDS"

    def __init__(self, message: str = EXCEPTION_MESSAGE) -> None:
        self.message = message


class Snowfall:
    """
    class Snowfall for generation of snowflakes

    Raises:
        ErrorSettingTimestampException: If the system clock is moving backwards.
    """

    SHIFT_TIME: int = 10 + 12
    SHIFT_GENERATOR: int = 10

    Configuration: SnowfallConfig = SnowfallConfig()

    _lastTimestamp: int | None = None
    _maxSequence: int = (1 << Configuration.MACHINE_SEQUENCE_BITS) - 1
    _sequence: int = 0

    @classmethod
    def generateSnowflake(cls, date: datetime = datetime.now(timezone.utc)) -> int:
        """
        Generates a unique snowflake ID.

        This method generates a unique snowflake ID based on the current timestamp,
        sequence number, and configuration settings. It ensures that the generated
        ID is unique by incrementing the sequence number if the timestamp is the same
        as the last generated timestamp. If the sequence number exceeds the maximum
        allowed value, it waits until the next timestamp.

        Args:
            date (datetime, optional): The date to use for generating the timestamp. Defaults to the current date.

        Raises:
            ErrorSettingTimestampException: If the system clock is moving backwards.

        Returns:
            int: The generated snowflake ID.
        """
        currentConfig: SnowfallConfig = cls.Configuration
        timestamp: int = generateTimestamp(date)

        if cls._lastTimestamp and timestamp < cls._lastTimestamp:
            raise ErrorSettingTimestampException()

        if timestamp == cls._lastTimestamp:
            cls._sequence = (cls._sequence + 1) & cls._maxSequence
            if not cls._sequence:
                timestamp = waitUntilNextTimestamp(timestamp)
        else:
            cls._sequence = 0

        cls._lastTimestamp = timestamp

        return (
            ((timestamp - currentConfig.Epoch) << cls.SHIFT_TIME)
            | (currentConfig.WorkedID << cls.SHIFT_GENERATOR)
            | cls._sequence
        )
