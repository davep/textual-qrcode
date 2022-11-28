"""Provides a QR code widget."""

##############################################################################
# Python imports.
from typing       import Any
from urllib.parse import quote

##############################################################################
# HTTPX imports.
import httpx

##############################################################################
# Textual imports.
from textual.app      import RenderResult
from textual.widget   import Widget

##############################################################################
class QRCode( Widget ):
    """A simple text-based QR code widget.

    **NOTE:** This is a wrapper around https://qrenco.de/ -- anything you
    encode with this widget will be sent to that site.

    **NOTE:** This widget, due to the nature of what it's designed to
    display, will change width and height depending on the data it is asked
    to display.
    """

    def __init__( self, text: str, *args: Any, **kwargs: Any ) -> None:
        """Initialise the QR code widget.

        Args:
            text (str): The text to encode.
        """
        super().__init__( *args, **kwargs )
        self._content              = text
        self._qr_code: list[ str ] = []

    def encode( self, text: str ) -> None:
        """Encode some new text.

        Args:
            text (str): The text to encode.
        """
        self._content = text
        self._qr_code = []
        self.refresh()

    @property
    def encoded_content( self ) -> str:
        """str: The content that was encoded in the QR code."""
        return self._content

    async def _get_qr_code( self ) -> None:
        """Get the QR code from the website."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://qrenco.de/{quote( self.encoded_content.strip() )}",
                headers={ "user-agent": "textual-qrcode (curl)" }
            )
            # TODO: Error checking and stuff.
            self._qr_code      = response.text.splitlines()
            self.styles.width  = len( self._qr_code[ 0 ] )
            self.styles.height = len( self._qr_code )
            self.refresh()

    def render( self ) -> RenderResult:
        """Render the QR code.

        Returns:
            RenderResult: The QR code content for rendering.
        """
        # We're being asked to render the QR code; but it's possible we've
        # not gone out and got it yet...
        if not self._qr_code:
            # Yup, we've not requested it yet. Let's set up a call to get it
            # and then when we swing by here again later we won't end up in
            # here because we'll have it.
            self.call_later( self._get_qr_code )
        # Render the result.
        return "\n".join( self._qr_code )

### qrcode.py ends here
