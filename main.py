def main():
  return "Grüßgöddle"

def handler(event, ctx):
  return event

print(
  main(),
  "from my push",
  handler({"message": "Habe die Ehre, der Test läuft durch, zum vierten Mal"}, None)
)
