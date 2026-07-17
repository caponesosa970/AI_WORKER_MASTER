# ChatGPT Artifact Audit Checklist

- Verify source SHA `71A766AE8D550C139AABCEC53DE3B1025CAF26C68561583CBF20AC6D5A5138B3`.
- Verify R1 XML SHA `535A163DA2FCEF1A655AB7DBBA4EBE5E9A991C7BF63CD74525244820D4BCA2A1`.
- Verify ZIP SHA `B47A4BC32FF33BD444F4EC9A710345F354F16DE451C8608F93E1F23C6552D0F9`.
- Verify ZIP contains exactly one byte-identical XML.
- Compare all 89 task nodes and require Task 235 as the only changed task.
- Verify Task 235 actions remain 243.
- Verify `act119` sets `%http_response_code` to numeric `0`.
- Verify `act162` keeps the error guard and uses `(?s)^\s*$|^%.*$|^0$`.
- Verify Task 233 SHA remains `39F35EFD2C56483D3B02299EBCC79E29540534C4FFFAC9F814B82FC8B7860188`.
- Verify Task 237, profiles, scene, and project registry are unchanged.
- Verify the explicit 429 injections overwrite code 0 before classification.
- Verify attempts remain capped at two and retries at one.
- Verify public files contain no credential, phone number, private path, Drive link, or raw runlog.
- Keep tracker at `13/14 locked = 93%`.
- Do not merge PR #9 or approve production release.
