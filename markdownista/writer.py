from __future__ import annotations

from markdownista.output import Output, PrintOutput
from markdownista.syntax import MarkdownSyntax


class TableMdWriter:
    def __init__(self, *, output: Output = None, syntax: MarkdownSyntax = None):
        self.output = output or PrintOutput()
        self.syntax = syntax or MarkdownSyntax()
        self.write = self.output.write

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()

    def end(self) -> None:
        self.write("")

    def header(self, header) -> TableMdWriter:
        for row in self.syntax.table_header(header):
            self.write(row)

        return self

    def row(self, row):
        self.write(self.syntax.table_row(row))

    def rows(self, rows, *, header=False) -> TableMdWriter:
        if header:
            header, *rows = rows
            self.header(header)

        for row in rows:
            self.row(row)

        return self

    def csv_lines(self, csv_lines, *, separator=',', header=False) -> TableMdWriter:
        rows = [line.split(separator) for line in csv_lines]
        return self.rows(rows, header=header)


class MdWriter:
    def __init__(self, *, output: Output = None, syntax: MarkdownSyntax = None):
        self.output = output or PrintOutput()
        self.syntax = syntax or MarkdownSyntax()
        self.write = self.output.write

    def br(self):
        self.write(" ")

    def paragraph(self, text):
        self.write(text)
        self.br()

    def heading(self, title, *, level=1):
        self.write(self.syntax.heading(title, level=level))
        self.br()

    def table(self) -> TableMdWriter:
        return TableMdWriter(output=self.output, syntax=self.syntax)
