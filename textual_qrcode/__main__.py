"""Provides a simple test/demo application for the widget."""

##############################################################################
# Textual imports.
from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, Input

##############################################################################
# Local imports.
from . import QRCode

##############################################################################
class QRCoder( App[ None ] ):
    """A simple demonstration of the QR code widget."""

    CSS = """
    Screen {
        align: center middle;
    }

    Input {
        dock: top;
        width: 100%;
    }
    """

    TITLE = "QR code demo"
    """The title of the application."""

    def compose( self ) -> ComposeResult:
        """Compose the test/demo app.

        Returns:
            ComposeResult: The layout of the main screen.
        """
        yield Header()
        yield Input( placeholder="Enter some text to encode" )
        yield QRCode( "https://textual.textualize.io/" )
        yield Footer()

    def on_mount( self ) -> None:
        """Settle focus once the app has started up."""
        self.query_one( Input ).focus()

    def on_input_submitted( self, event: Input.Submitted ) -> None:
        """Handle the user submitting some input."""
        self.query_one( QRCode ).encode( event.input.value )

##############################################################################
# Main entry point.
if __name__ == "__main__":
    QRCoder().run()

### __main__.py ends here
