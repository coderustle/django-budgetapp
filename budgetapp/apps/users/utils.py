"""
Utility function and classes
"""
from typing import Any

from django.http import HttpResponseRedirect

# htmx redirect
class HttpResponseHXRedirect(HttpResponseRedirect):
    """This class is adding HX-Redirect to response header
    Thus, will let the htmx to redirect to a specific location
    """

    def __init__(self, redirect_to: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(redirect_to, *args, **kwargs)
        self["HX-Redirect"] = self["Location"]
