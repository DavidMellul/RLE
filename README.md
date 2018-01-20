# RLE
Simple Run-Length-Encoding tool that lets you encode and decode rle files

## How to use

    $ Would you rather encode(e) or decode(d) a file : d
    $ Input file path : encoded.rle
    $ Output file path : decoded.rle
    $ Done!

## Which standard does it follow

This tool works with strings following this pattern :

    3A2B4C => AAABBCCCC
    AAABBCCCC => 3A2B4C
It won't accept strings composed of digits as it would confuse the decoding process as there is no separator support.
