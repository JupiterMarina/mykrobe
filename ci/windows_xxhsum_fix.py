#!/usr/bin/env python3

import os


def fix_file(filename, to_replace):
    lines = []
    with open(filename) as f:
        for line in f:
            if line in to_replace:
                print(f"Replacing in {filename}:\n", line, to_replace[line], sep="")
                line = to_replace[line]
            lines.append(line)

    with open(filename, "w") as f:
        print(*lines, sep="", file=f)


filename = os.path.join("mccortex", "libs", "xxHash", "xxhsum.c")
to_replace = {
    "#if defined(MSDOS) || defined(OS2) || defined(WIN32) || defined(_WIN32) || defined(__CYGWIN__)\n": "#if defined(MSDOS) || defined(OS2) || defined(WIN32) || defined(_WIN32)\n"
}
fix_file(filename, to_replace)



filename = os.path.join("mccortex", "libs", "bit_array", "bit_array.c")
to_replace = {
    "  c = (word_t)(w * ((word_t)~(word_t)0/255)) >> (sizeof(word_t) - 1) * 8;\n": "  return (word_t)(w * ((word_t)~(word_t)0/255)) >> (sizeof(word_t) - 1) * 8;\n",
    "static word_t __inline windows_popcount(word_t w)\n": "static word_t __inline windows_popcountl(word_t w)\n",
}
fix_file(filename, to_replace)


filename = os.path.join("mccortex", "libs", "seq_file", "Makefile")
to_replace = {
    "LINKING=$(HTSARGS) -lpthread -lz\n": "LINKING=$(HTSARGS) -lpthread -lws2_32 -lz -llzma -lbz2\n",
}
fix_file(filename, to_replace)

