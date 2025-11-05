from datetime import datetime

from pysnowfall import (
    Snowfall,
    SnowfallConfig,
    toSnowflake,
    toSnowflakeCustom,
)

sf_string: str = "62937765418893312"
snowflake: int = int(sf_string)
timestamp: int = 1_736_352_732_603

config: SnowfallConfig = SnowfallConfig(1_721_347_200_000, 0)
dateString: str = "2025-01-08T16:12:12.603Z"

Snowfall.Configuration = config


def test_validSnowflake():
    date: datetime = datetime.fromisoformat(dateString)
    print(Snowfall.Configuration.Epoch)

    assert Snowfall.generateSnowflake(date) == snowflake


def test_parseTimestamp():
    assert toSnowflakeCustom(sf_string, config).Timestamp == timestamp


def test_parseTimestampGlobalConfig():
    assert toSnowflake(sf_string).Timestamp == timestamp


def test_parseTime():
    assert toSnowflakeCustom(sf_string, config).Time == datetime.fromisoformat(
        dateString
    )


def test_parseMachineID():
    assert toSnowflakeCustom(sf_string, config).MachineID == 0
