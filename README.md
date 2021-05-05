# Markdownista
 
**Markdownista** writes *Markdown*.
 
|Who|Does what|
|---|---|
|Barista|Makes coffee|
|Markdownista|Writes markdown|

You can use `with` to keep using the table and have it end automatically.
 
|Number|Square|Cube|
|---|---|---|
|0|0|0|
|1|1|1|
|2|4|8|
|3|9|27|
|4|16|64|

# Customization
 
## Syntax
 
You can swap out the syntax you're using.
 
```python3
from markdownista.writer import MdWriter
from markdownista.syntax import ConfluenceMarkdownSyntax

md = MdWriter(syntax=ConfluenceMarkdownSyntax())
```

## Output
 
You can swap out the output as well.
 
```python3
from markdownista.writer import MdWriter
from markdownista.output import BufferedOutput

output = BufferedOutput()
md = MdWriter(output=output)

# write some stuff

output.print()              # print to the console
with open("README.md", "w") as file:
    output.print(file=file) # or to a file
```

# How it's done
 
```python3
def demo(md):
    md.heading("Markdownista")

    md.paragraph(f"{md.syntax.bold('Markdownista')} writes {md.syntax.italic('Markdown')}.")

    rows_with_header = [
        ["Who", "Does what"],
        ["Barista", "Makes coffee"],
        ["Markdownista", "Writes markdown"]
    ]
    md.table().rows(rows_with_header, header=True).end()

    md.paragraph("You can use " + md.syntax.code("with") + " to keep using the table and have it end automatically.")

    with md.table().header(["Number", "Square", "Cube"]) as table:
        for i in range(5):
            table.row([i, i*i, i*i*i])

    md.heading("Customization")

    md.heading("Syntax", level=2)

    md.paragraph("You can swap out the syntax you're using.")

    code = """from markdownista.writer import MdWriter
from markdownista.syntax import ConfluenceMarkdownSyntax

md = MdWriter(syntax=ConfluenceMarkdownSyntax())"""
    md.write(md.syntax.code_block(text=code, language="python3"))

    md.heading("Output", level=2)

    md.paragraph("You can swap out the output as well.")

    code = """from markdownista.writer import MdWriter
from markdownista.output import BufferedOutput

output = BufferedOutput()
md = MdWriter(output=output)

# write some stuff

output.print()              # print to the console
with open("README.md", "w") as file:
    output.print(file=file) # or to a file"""
    md.write(md.syntax.code_block(text=code, language="python3"))

    md.heading("How it's done")

    demo_code = inspect.getsource(demo)
    md.write(md.syntax.code_block(text=demo_code, language="python3"))

```

