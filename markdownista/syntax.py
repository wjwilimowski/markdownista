from abc import ABC

DEFAULT_NEWLINE = "\n"

_table_separator = "|"


class MarkdownSyntax:
    def __init__(self, *, newline=None):
        self._newline = newline if newline is not None else DEFAULT_NEWLINE

    @staticmethod
    def code(text: str) -> str:
        return f"`{text}`"

    def code_block(self, text: str, *, language: str = None) -> str:
        return "```" + language + self._newline + text + self._newline + "```"

    @staticmethod
    def bold(text: str) -> str:
        return f"**{text}**"

    @staticmethod
    def italic(text: str) -> str:
        return f"**{text}**"

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
    @staticmethod
    def code(text: str) -> str:
        return "{{" + text + "}}"

    def code_block(self, text: str, *, language: str = None) -> str:
        return "{code}" + text + "{code}"

    @staticmethod
    def bold(text: str) -> str:
        return f"*{text}*"

    @staticmethod
    def italic(text: str) -> str:
        return f"~{text}~"

    @staticmethod
    def heading(text: str, *, level=1) -> str:
        return f"h{level}. {text}"

    @classmethod
    def table_header(cls, fields: []):
        yield cls.table_row(fields)
