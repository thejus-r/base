from collections import defaultdict
class Spreadsheet:

    def __init__(self, rows: int):
        self.data = {}
        self.maxRows = rows

    def setCell(self, cell: str, value: int) -> None:
        row, col = cell[0], cell[1:]
        self.data[f'{row}_{col}'] = value

    def resetCell(self, cell: str) -> None:
        row, col = cell[0], cell[1:]
        if f'{row}_{col}' in self.data:
            del self.data[f'{row}_{col}']

    def getValue(self, formula: str) -> int:

       # =A1+6
       parsed = formula[1:]
       fcell, scell = map(str, parsed.split("+"))
       sum = 0

       if not fcell.isdigit():
           row, col = fcell[0], fcell[1:]
           sum += self.data.get(f'{row}_{col}', 0)
       else:
           sum += int(fcell)

       if not scell.isdigit():
           row, col = scell[0], scell[1:]
           sum += self.data.get(f'{row}_{col}', 0)
       else:
           sum += int(scell)

       return sum

sp = Spreadsheet(10)
print(sp.getValue("=5+7"))
sp.setCell("A1", 10)
print(sp.getValue("=A1+6"))
sp.setCell("B2", 15)
print(sp.getValue("=A1+B2"))
sp.resetCell("A1")
print(sp.getValue("=A1+B2"))
print(sp.data)