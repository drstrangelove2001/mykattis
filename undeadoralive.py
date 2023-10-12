msg = input()
if ":)" in msg and ":(" in msg:
    print("double agent")
elif ":)" in msg:
    print("alive")
elif ":(" in msg:
    print("undead")
else:
    print("machine")
