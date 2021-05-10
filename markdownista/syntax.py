DEFAULT_NEWLINE = "\n"

_table_separator = "|"


class MarkdownSyntax:
    def __init__(self, *, newline=None):
        self._newline = newline if newline is not None else DEFAULT_NEWLINE

    @staticmethod
    def code(text: str) -> str:
        return f"`{text}`"

    def code_block(self, *, text=None, lines=None, language: str = None) -> str:
        if text is None and lines is None or text is not None and lines is not None:
            raise ValueError("Provide either text or lines for code_block")

        if lines is not None:
            text = self._newline.join(lines)

        return self._begin_code_block(language) + text + self._end_code_block()

    def _begin_code_block(self, language: str):
        return f"```{language}" + self._newline

    def _end_code_block(self):
        return self._newline + "```" + self._newline

    @staticmethod
    def bold(text: str) -> str:
        return f"**{text}**"

    @staticmethod
    def italic(text: str) -> str:
        return f"*{text}*"

    @staticmethod
    def heading(text: str, *, level=1) -> str:
        return "#" * level + " " + text

    @staticmethod
    def _table_row_item(item):
        if item is None:
            return " "

        str_item = str(item)
        if len(str_item) == 0:
            return " "

        return str_item

    @classmethod
    def table_row(cls, items: []) -> str:
        formatted_items = [cls._table_row_item(i) for i in items]

        return _table_separator.join(["", *formatted_items, ""])

    @classmethod
    def table_header(cls, fields: []):
        yield cls.table_row(fields)
        yield cls.table_row(["---" for _ in fields])


class ConfluenceMarkdownSyntax(MarkdownSyntax):
    def __init__(self, *, bold_table_headers=False):
        super().__init__()
        self.bold_table_headers = bold_table_headers

    @staticmethod
    def code(text: str) -> str:
        return "{{" + text + "}}"

    def _begin_code_block(self, language: str):
        return "{code}"

    def _end_code_block(self):
        return "{code}"

    @staticmethod
    def bold(text: str) -> str:
        return f"*{text}*"

    @staticmethod
    def italic(text: str) -> str:
        return f"~{text}~"

    @staticmethod
    def heading(text: str, *, level=1) -> str:
        return f"h{level}. {text}"

    def table_header(self, fields: []):
        header = [self.bold(f) for f in fields] if self.bold_table_headers else fields
        yield self.table_row(header)
