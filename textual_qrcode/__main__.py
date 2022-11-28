"""Provides a simple test/demo application for the widget."""

##############################################################################
# Textual imports.
from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, Input, Label

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

    Label {
        width: auto;
        text-style: bold;
        color: green;
    }

    .error {
        color: red;
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
        yield Label()
        yield Footer()

    def on_mount( self ) -> None:
        """Settle focus once the app has started up."""
        self.query_one( Input ).focus()

    def on_input_submitted( self, event: Input.Submitted ) -> None:
        """Handle the user submitting some input."""
        self.query_one( QRCode ).encode( event.input.value )

    def on_qrcode_encoded( self, _: QRCode.Encoded ) -> None:
        """Respond to the QR code being encoded fine."""
        label = self.query_one( Label )
        label.update( "Encoded without an error" )
        label.set_class( False, "error" )

    def on_qrcode_error( self, event: QRCode.Error ) -> None:
        """Respond to the QR code having a problem."""
        label = self.query_one( Label )
        label.update( f"Ugh: {event.error!r}" )
        label.set_class( True, "error" )

##############################################################################
# Main entry point.
if __name__ == "__main__":
    QRCoder().run()

### __main__.py ends here
