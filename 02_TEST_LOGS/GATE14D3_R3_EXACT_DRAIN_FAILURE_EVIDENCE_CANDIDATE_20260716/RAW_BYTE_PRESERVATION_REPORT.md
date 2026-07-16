# Raw Byte Preservation Report

Base topology: 93 tasks / 4 profiles / 1 scene.

Final topology: 97 tasks / 4 profiles / 1 scene.

Existing task comparison:

- authorized changed existing tasks: 8;
- raw-byte-identical other existing tasks: 85/85;
- added tasks: 242, 243, 244, 245;
- profiles raw-byte identical: 4/4 and disabled;
- scene raw-byte identical: 1/1.

Processing, OpenAI, TextNow, Send, confirmation, DONE, Archive, timer, profiles, and final-interface behavior are outside the change set.

Credential equality was verified without printing the credential.

Encoding comparison: base and R3 both contain zero `Â§` sequences. The added state-machine delimiters use the intended section-sign character; no baseline mojibake drift remains.
