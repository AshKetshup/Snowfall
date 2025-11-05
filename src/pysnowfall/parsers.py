from .snowfall import Snowfall
from .snowfallConfig import SnowfallConfig
from .snowflake import Snowflake


def toSnowflakeCustom(
    snowflakeID: str | int, configuration: SnowfallConfig
) -> Snowflake:
    """
    Converts the provided `snowflakeID` to a `Snowflake` instance using the specified `configuration`.

    Args:
        snowflakeID (str | int): The snowflake ID as a `string` or `integer`.
        configuration (SnowfallConfig): The configuration to use for creating the `Snowflake` instance.

    Returns:
        Snowflake: A `Snowflake` instance configured with the specified `configuration`.
    """
    return Snowflake(snowflakeID, configuration)


def toSnowflake(
    snowflakeID: str | int, useGlobalConfiguration: bool = True
) -> Snowflake:
    """
    Converts the provided `snowflakeID` to a `Snowflake` instance using either the global configuration or a new instance of `SnowfallConfig`.

    Args:
        snowflakeID (str | int): The snowflake ID as a `string` or `integer`.
        useGlobalConfiguration (bool, optional): A boolean value indicating whether to use the global configuration.
            Defaults to True.

    Returns:
        Snowflake: A `Snowflake` instance configured based on the `useGlobalConfiguration` parameter.
    """
    return Snowflake(
        snowflakeID,
        Snowfall.Configuration if useGlobalConfiguration else SnowfallConfig(),
    )
