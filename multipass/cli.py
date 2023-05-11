#  Copyright (C) 2023  Julian Fölsch
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>

"""multi-pass.

Usage:
  multi-pass -h | --help
  multi-pass --version
  multi-pass <command> [<args>...]

Options:
  -h --help     Show this screen.
  --version     Show version.

Usable commands:
  ls [SUBFOLDER]    Lists passwords.

See 'multi-pass <command> --help' for help on a specific command.
"""
from importlib import metadata
from docopt import docopt


def run():
    args = docopt(__doc__,
                  options_first=True,
                  version=f"multi-pass {metadata.version('multipass')}\n"
                          f"Copyright (C) 2023 Julian Fölsch\n"
                          f"This is free software licensed under the GNU GENERAL PUBLIC LICENSE,"
                          f"see the source for copying conditions.\n"
                          f"There is NO warranty; "
                          f"not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.",
                  )
    argv = [args["<command>"]] + args["<args>"]
    match args["<command>"]:
        case "ls":
            ls(argv)
        case _:
            print(__doc__)


def ls(argv):
    """
    Usage:
      multi-pass ls [SUBFOLDER]

    Lists password in optional subfolder.
    """
    arguments = docopt(ls.__doc__, argv=argv)
    print(arguments)


if __name__ == '__main__':
    run()
