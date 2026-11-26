"""Write one museum placard line for an office stapler to /output/entry.txt."""
import os

ENTRY = "Stapler, c. 1987, pressed steel. Used in the binding rite of the Third Floor, where documents were joined forever and no one could take anything back. Gift of Mr. Hendricks."


def validate(entry):
    """Check the placard against the gate before writing it out.

    The gate refuses anything that is not UTF-8 text of 1-180
    characters, is only whitespace, or spans more than one line.
    A placard label reads as catalogue facts first, then the
    imagined rite, then the donor: every word earns its place.
    """
    assert isinstance(entry, str), "entry must be text"
    assert 1 <= len(entry) <= 180, "entry must be 1-180 characters"
    assert entry.strip(), "entry must not be only whitespace"
    assert "\n" not in entry.strip(), "entry must be a single line"
    # Label craft: a placard needs a catalogue date and a donor
    # line, or the curator's joke has nothing to hang on.
    assert ", c. " in entry, "entry must carry a catalogue date"
    assert entry.rstrip().endswith("."), "entry must end with a full stop"
    return entry


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the chosen line: no trailing newline, so the
    # file's byte count is the line itself and the gate reads it
    # as one line of 173 characters.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
