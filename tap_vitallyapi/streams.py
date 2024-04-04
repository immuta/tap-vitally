"""Stream type classes for tap-vitallyapi."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_vitallyapi.client import vitallyapiStream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class AccountsStream(vitallyapiStream):
    """Define custom stream."""
    name = "accounts"
    path = "/accounts"
    primary_keys = ["id"]
    replication_key = None
    replication_method = "FULL_TABLE"
    schema_filepath = SCHEMAS_DIR / "accounts.json"

class UsersStream(vitallyapiStream):
    """Define custom stream."""
    name = "users"
    path = "/users"
    primary_keys = ["id"]
    replication_key = None
    replication_method = "FULL_TABLE"
    schema_filepath = SCHEMAS_DIR / "users.json"


