g1=" "
g3=" "*26

print("="*100)
print('*' * 37, end='')
print(f"{'1st DEAL':^26s}", end='')
print(f"{'*' * 37:^20}")
print(f"{'Time:':^37s}{'Flight Duration:':^26s}{'Stops:':^37s}")
time=(time1p1.text, time1p2.text)
jtime="-".join(time)
print(f"{jtime:^37s}{dura1.text:^26s}{stops1.text:^37s}")
print(f"{'Airlines:':^37}{g3}{'Ticket Price (KWD):':^37}")
print(f"{air1.text:^37}{g3}{price1.text:^37}")
print("-"*100)
