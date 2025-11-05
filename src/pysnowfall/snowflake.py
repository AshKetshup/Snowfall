from datetime import datetime, timezone

from .helpers import getMask
from .snowfallConfig import SnowfallConfig


class Snowflake:
    """Snowflake assembler class"""

    _maskGenerator: int = getMask(10)
    _maskSequence: int = getMask(12)
    _shiftTime: int = 22

    def __init__(
        self, snowflakeID: int | str, configuration: SnowfallConfig = SnowfallConfig()
    ) -> None:
        """
        Initializes a new instance using a snowflake ID and an optional configuration.

        Args:
            snowflakeID (int | str): The snowflake ID as a `integer` or `string`.
            configuration (SnowfallConfig, optional): The configuration to use for creating the instance. Defaults to SnowfallConfig().
        """
        self.SnowflakeID: int = int(snowflakeID)
        self.Timestamp: int = 0
        self.MachineID: int = 0
        self.Sequence: int = 0
        self._configuration: SnowfallConfig = configuration
        self._decodeSnowflake(self.SnowflakeID)

    @property
    def Time(self) -> datetime:
        """
        A computed property that returns the timestamp as a `datetime` object.

        Returns:
            datetime: a `datetime` object representing the timestamp.
        """
        return self._timestampToDatetime()

    def updateConfiguration(self, configuration: SnowfallConfig) -> None:
        """
        Updates the configuration and decodes the snowflake ID.

        Args:
            configuration (SnowfallConfig): The new configuration to set.
        """
        self._configuration = configuration
        self._decodeSnowflake(self.SnowflakeID)

    def _decodeSnowflake(self, snowflake: int) -> None:
        """
        Decodes the Snowflake ID into its components.

        Args:
            snowflake (int): The Snowflake ID to decode.
        """
        self.Timestamp = (snowflake >> self._shiftTime) + self._configuration.Epoch
        self.MachineID = (
            snowflake >> SnowfallConfig.MACHINE_SEQUENCE_BITS
        ) & self._maskGenerator
        self.Sequence = snowflake & self._maskSequence

    def _timestampToDatetime(self) -> datetime:
        """
        Converts current timestamp into a `datetime` object.

        Returns:
            datetime: a `datetime` object representing the timestamp.
        """
        return datetime.fromtimestamp(self.Timestamp / (10**3), tz=timezone.utc)
