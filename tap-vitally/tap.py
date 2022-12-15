"""vitallyapi tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_vitallyapi.streams import (
    vitallyapiStream,
    AccountsStream,
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
  AccountsStream
]


class Tapvitallyapi(Tap):
    """vitallyapi tap class."""
    name = "tap-vitallyapi"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True, secret=True),
        th.Property("user_agent", th.StringType, default = "tap_vitallyapi"),
            
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


# if __name__ == "__main__":
#     Tapvitallyapi.cli()
