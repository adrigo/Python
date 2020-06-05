values = [
  #nan,
  0,
  1,
  -1,
  "0",
  "1",
  "-1",
  "php",
  '',
  True,
  False,
  None,
  [],
  ['']
]
format =  "{a: >7}    ==    {b: <7} :    {c: <5}"
formatBoolean =  "{a: >7}    ToBoolean    :    {c: <5}"

for value in values:
  print(formatBoolean.format(a=str(value), c=str(bool(value))))
print("\n")

for value in values:
    for value2 in values:
        print(format.format(a=str(value), b=str(value2), c=str(bool(value == value2))))
    print("\n")
 
