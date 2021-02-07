values = [
  float('nan'),
  float('inf'),
  -float('inf'),
  0,
  1,
  -1,
  "0",
  "1",
  "-1",
  "string",
  '',
  True,
  False,
  None,
  [],
  ['']
]
formatBoolean =  "{a: >10}    To BOOLEAN    :    {c: <5}"
format =  "{a: >9}    ==    {b: <8} :    {c: <5}"

for value in values:
  print(formatBoolean.format(a=repr(value), c=str(bool(value))))
print("\n----------------------------------------\n")

for value in values:
    for value2 in values:
        print(format.format(a=repr(value), b=repr(value2), c=str(bool(value == value2))))
    print("\n")
 
