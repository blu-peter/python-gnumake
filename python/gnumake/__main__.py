from textwrap import dedent
import os
import gnumake._gnumake

library = gnumake._gnumake.__file__

print(dedent(
        """\
        load {library}
        """.format(library=library)))
