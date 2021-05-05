from __future__ import annotations

from markdownista.output import Output, PrintOutput


class TableMdWriter:
    def __init__(self, *, output: Output = None):
        self.output = output or PrintOutput()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @staticmethod
    def _table_row(items):
        return "|" + "|".join([(str(i) if i is not None else " ") for i in items]) + "|"

    def header(self, header) -> TableMdWriter:
        self.row(header)
        self.row(["---" for _ in header])

        return self

    def row(self, row):
        self.output.write(self._table_row(row))

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
    def __init__(self, *, output: Output = None):
        self.output = output or PrintOutput()

    def write(self, line):
        self.output.write(line)

    def br(self):
        self.write(" ")

    @staticmethod
    def _create_heading(title, *, depth=1):
        return f"{'#' * depth} {title}"

    def heading(self, title, *, depth=1):
        self.write(self._create_heading(title, depth=depth))
        self.br()

    def table(self) -> TableMdWriter:
        return TableMdWriter(output=self.output)
