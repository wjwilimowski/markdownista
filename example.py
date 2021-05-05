from markdownista.writer import MdWriter

md = MdWriter()

md.heading("Markdownista")
with md.table().header(["Number", "Square", "Cube"]) as table:
    for i in range(5):
        table.row([i, i*i, i*i*i])

md.br()
md.table().header(["A", "B"]).rows([[i, i+2] for i in range(6)])


rows_with_header = [
    ["Header1", "Header2"],
    ["Value11", "Value21"],
    ["Value12", "Value22"],
    ["Value13", "Value23"]
]

md.br()
md.table().rows(rows_with_header, header=True)
