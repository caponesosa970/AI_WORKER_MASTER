# Special Character Preservation Report

The controlled mode uses one payload containing:

- a newline;
- a section sign;
- a leading equals sign;
- a leading plus sign;
- Latin, Greek, Cyrillic, and CJK Unicode.

D3A AutoSheets writes use dedicated multi-character column and row separators that are rejected if they appear in a payload. Newline and section-sign data therefore cannot become structural separators.

Formula-leading sender, message, or ticker values receive the source-proven plain-text apostrophe prefix for the write. Exact logical readback must equal the original unprefixed value.

The XML stores added non-ASCII test characters as XML character references. UTF-8 parsing reconstructs the exact logical characters and the final file contains zero U+00C3 mojibake markers.

Phone behavior remains unproven until the exact package is audited and run.
