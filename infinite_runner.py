import core, time

core.slowMode(False)
inf_seed = 9232
while True:
    time.sleep(0.8)
    core.main_loop(inf_seed)
    inf_seed = inf_seed + 1



