# textual-qrcode

## Introduction

While, I admit, likely of little utility really, this library aims to show
one possible way of writing and "shipping" a custom widget for
[Textual](https://textual.textualize.io/). Key here is that the library
contains and provides a custom widget which can be imported and used in an
application; but it also provides a simple application that can be run to
see the widget in action.

## Please note!

This library is just a thin wrapper around <https://qrenco.de/>. Each time
you create a QR code the content you encode is sent to that website. It also
means, of course, that this is only usable with a working net connection.
Please keep these things in mind if you do decide to actually use this for
something.

## Installing

The library itself can be installed with `pip`:

```sh
$ pip install textual-qrcode
```

or with your Python environment manager of choice.

## Running the test application

The demo/test application can be run like this:

```sh
$ python -m textual_qrcode
```

When you've finished testing, press <kbd>Ctrl</kbd>+<kbd>C</kbd> to quit.

## Using the widget

To make use of the `QRCode` widget, import it into your code:

```python
from textual_qrcode import QRCode
```

The widget itself takes all of the arguments that a normal Textual `Widget`
takes, but has the addition of an initial positional argument which is some
text to encode. An example use of it could look like:

```python
    def compose( self ) -> ComposeResult:
        yield Header()
        yield QRCode( "https://textual.textualize.io/" )
        yield Footer()
```

The widget also has a `encode` method, that lets you update the QR code to
display something else. For example:

```python
self.query_one( QRCode ).encode( "Now I've changed it to this" )
```

The widget will send out one of two messages when an attempt is made to
encode some content. If the content was encoded fine a `QRCode.Encoded`
message is sent out, which can be caught like this:

```python
def on_qrcode_encoded( self, event: QRCode.Encoded ) -> None:
    # Do something now that the QR code was updated fine.
```

If there is an error encoding the content `QRCode.Error` will be sent out.
this can be used like this:

```python
def on_qrcode_error( self, event: QRCode.Error ) -> None:
    # Do something about the error.
```

In both cases the event sent out has a `qr_code` property which is the
`QRCode` widget involved.

[//]: # (README.md ends here)
