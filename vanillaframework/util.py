"""Utility functions for handling Vanilla Framework in Django."""
from urllib import request
from urllib.error import HTTPError
import json


def get_latest_release_version():
    """Check Vanilla Framework's GitHub repo for the latest release tag."""
    try:
        with request.urlopen("https://api.github.com/repos/canonical/vanilla-framework/tags") as url_data:
            json_output = json.loads(url_data.read().decode())
            for tag in json_output:
                if "name" in tag and tag["name"][0] == "v":
                    return tag["name"][1::]
    except HTTPError:
        pass

    return None
