# pylint: disable=unused-argument

"""All of hush's plugin hook specifications[1] live here.

[1]: https://pluggy.readthedocs.io/en/stable/#specifications
"""

from typing import Iterable, Optional

from ._hooks import hookspec


@hookspec(firstresult=True)  # type: ignore[misc]
def get_secret(
    key: str, namespace: Iterable[str], user: Optional[str]
) -> Optional[str]:
    """This hook is used to retrieve secrets.

    Args:
        key: The key that corresponds to the secret we are hoping to retrieve.
        namespace: The namespace that the secret belongs to (e.g. `["db",
          "foobar"]`). How this argument is used is specific to the tool being
          used to store and retrieve secrets (i.e. is specific to each hook
          implementation).
        user: If this argument is provided, secret retrieving commands are run
          as ``user`` when possible.
    """
