__version__ = '3.2.4'

# Check Django compatibility before other imports which may fail if the
# wrong version of Django is installed.
from .utils import check_django_compatability

check_django_compatability()

from .functions import register_functions  # noqa
from .lookups import patch_lookups  # noqa

patch_lookups()
register_functions()
