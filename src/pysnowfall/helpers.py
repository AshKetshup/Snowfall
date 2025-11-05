from datetime import datetime, timezone


def getMask(bits: int) -> int:
    """
    Returns a mask with the specified number of bits set to 1.

    Args:
        bits (int): The number of bits to set to 1.

    Returns:
        int: value with the specified number of bits set to 1.
    """
    return (1 << bits) - 1


def generateTimestamp(dateTime: datetime = datetime.now(timezone.utc)) -> int:
    """
    Generates a timestamp for the specified date.

    Args:
        dateTime (datetime, optional): The date for which to generate the timestamp. Defaults to datetime.now().

    Returns:
        int: Value representing the timestamp for the specified date. In Milliseconds

    """

    def secondsToMilliseconds(seconds: int | float) -> int:
        return int(round(seconds * 1000))

    unixEpoch: int = secondsToMilliseconds(
        datetime(1970, 1, 1, 0, 0, tzinfo=timezone.utc).timestamp()
    )
    currentTimestamp: int = secondsToMilliseconds(dateTime.timestamp())
    return currentTimestamp - unixEpoch


def waitUntilNextTimestamp(currentTimestamp: int) -> int:
    """
    Waits until the next timestamp that is greater than the current timestamp.

    Args:
        currentTimestamp (int): The current timestamp.

    Returns:
        int: The next timestamp that is greater than the current timestamp.
    """
    nextTimestamp: int = generateTimestamp()
    while nextTimestamp <= currentTimestamp:
        nextTimestamp = generateTimestamp()

    return nextTimestamp
