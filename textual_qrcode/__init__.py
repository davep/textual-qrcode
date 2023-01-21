"""A library and terminal wrapper around qrenco.de."""

######################################################################
# Main app information.
__author__     = "Dave Pearson"
__copyright__  = "Copyright 2022-2023, Dave Pearson"
__credits__    = [ "Dave Pearson" ]
__maintainer__ = "Dave Pearson"
__email__      = "davep@davep.org"
__version__    = "0.2.0"
__licence__    = "MIT"

##############################################################################
# Local imports.
from .qrcode import QRCode

##############################################################################
# Export the imports.
__all__ = [
    "QRCode"
]

### __init__.py ends here
