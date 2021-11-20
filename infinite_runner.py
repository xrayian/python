from core import print_outputs, main_loop
from time import sleep

print_outputs(False)
inf_seed = 1 #9232 #test
while True:
    sleep(0.8)
    main_loop(inf_seed)
    inf_seed = inf_seed + 1



