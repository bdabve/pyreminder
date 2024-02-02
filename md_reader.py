#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# author        : el3arbi bdabve@gmail.com
# created       : 09-December-2022
#
# description   : Print markdown files in console with rich.markdown
# ----------------------------------------------------------------------------

from rich.markdown import Markdown
from rich.console import Console
import typer

console = Console()


def md_reader(fname: str = typer.Argument(..., help='Enter markdown file name')):
    with open(fname) as w:
        md_content = Markdown(w.read())
        console.print(md_content)


if __name__ == '__main__':
    typer.run(md_reader)
