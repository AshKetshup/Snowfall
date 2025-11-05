# Snowfall

Snowfall is a Python implementation of a Snowflake ID generator, inspired by the project [PedroCavaleiro/avalanche](https://github.com/PedroCavaleiro/avalanche).
It allows for the generation of unique, time-sortable 64-bit integers that can be used as primary keys in distributed systems.

## Installation

Install the package from PyPI using pip:

```bash
pip install PySnowfall
```

## Usage

### Generating a Snowflake ID

The primary method for generating a new ID is `Snowfall.generateSnowflake()`. By default, it uses a global configuration.

```python
from snowfall import Snowfall

# Generate a new unique ID
new_id = Snowfall.generateSnowflake()
print(f"Generated Snowflake ID: {new_id}")
```

### Custom Configuration

You can customize the generation by providing a custom `epoch` and `workerID`. The epoch is a timestamp in milliseconds that marks the beginning of your ID generation period.

1.  Create an instance of `SnowfallConfig`.
2.  Assign it to `Snowfall.Configuration`.

```python
from snowfall import Snowfall
from snowfallConfig import SnowfallConfig

# Custom epoch (e.g., your project's launch time in milliseconds)
# This example uses 2024-07-19 00:00:00 UTC
custom_epoch = 1_721_347_200_000
worker_id = 5

# Create and set the custom configuration
custom_config = SnowfallConfig(epoch=custom_epoch, workedID=worker_id)
Snowfall.Configuration = custom_config

# Generate an ID with the new configuration
new_id = Snowfall.generateSnowflake()
print(f"Generated ID with custom config: {new_id}")
```

### Parsing a Snowflake ID

You can deconstruct a Snowflake ID into its constituent parts: timestamp, machine ID, and sequence number. The library provides helper functions for easy parsing.

```python
from parsers import toSnowflake
from snowfall import Snowfall
from snowfallConfig import SnowfallConfig

# Assume this ID was generated with worker ID 0 and a custom epoch
snowflake_id = "62937765418893312"
custom_epoch = 1_721_347_200_000

# Set the global configuration to match the one used for generation
Snowfall.Configuration = SnowfallConfig(epoch=custom_epoch, workedID=0)

# Parse the snowflake using the global configuration
decoded_snowflake = toSnowflake(snowflake_id)

# Access the components
print(f"Snowflake ID: {decoded_snowflake.SnowflakeID}")
print(f"Timestamp (ms): {decoded_snowflake.Timestamp}")
print(f"Date & Time (UTC): {decoded_snowflake.Time}")
print(f"Machine ID: {decoded_snowflake.MachineID}")
print(f"Sequence: {decoded_snowflake.Sequence}")

# Example Output:
# Snowflake ID: 62937765418893312
# Timestamp (ms): 1736352732603
# Date & Time (UTC): 2025-01-08 16:12:12.603000+00:00
# Machine ID: 0
# Sequence: 0
```
If you need to parse a Snowflake using a configuration different from the global one, you can use `toSnowflakeCustom`.

```python
from parsers import toSnowflakeCustom
from snowfallConfig import SnowfallConfig

snowflake_id = "62937765418893312"
custom_config = SnowfallConfig(epoch=1_721_347_200_000, workedID=0)

# Parse the snowflake using a specific configuration instance
decoded_snowflake = toSnowflakeCustom(snowflake_id, custom_config)
print(f"Time (UTC): {decoded_snowflake.Time}")
```

## API Overview

### `Snowfall` Class

This class is the generator.
*   `generateSnowflake(date: datetime) -> int`: The core class method that produces a new 64-bit integer ID. It optionally accepts a `datetime` object to generate an ID for a specific time.

### `SnowfallConfig` Class

Used to configure the `Snowfall` generator.
*   `__init__(self, epoch: int, workedID: int)`: Creates a configuration instance.
    *   `epoch`: The start time for your IDs in milliseconds since the UNIX epoch. Default is `1275350400000`.
    *   `workedID`: A unique ID for the worker/machine generating the Snowflakes, from 0-1023. Default is `1`.

### `Snowflake` Class

Represents a decoded Snowflake ID.
*   `Timestamp`: The timestamp part of the ID in milliseconds.
*   `MachineID`: The worker ID that generated the ID.
*   `Sequence`: The sequence number for IDs generated in the same millisecond.
*   `Time`: A `datetime` object representing the creation time of the ID in UTC.

## Development

To set up a local development environment and run tests:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AshKetshup/Snowfall.git
    cd Snowfall
    ```

2.  **Install dependencies:**
    The project uses `pytest` for testing.
    ```bash
    pip install pytest
    ```

3.  **Run tests:**
    Execute pytest from the root directory.
    ```bash
    pytest
    ```

## License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
