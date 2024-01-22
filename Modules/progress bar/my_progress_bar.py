from tqdm import tqdm
import time 
import progressbar

# https://www.scaler.com/topics/python-progress-bar/


for i in tqdm (range (5)):
    time.sleep(1)
    # 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 5/5 [00:05<00:00,  1.00s/it]

for i in tqdm (range (0, 100), 
               desc="Task in progress", 
               ascii=False, ncols=75, total=200, mininterval=0.1, unit="ticks", initial=100):
    time.sleep(0.01)
    # Task in progress: 100%|███████████████| 200/200 [00:01<00:00, 98.86ticks/s]
      

for i in progressbar.progressbar(range(500)):
    time.sleep(0.01)

bar = progressbar.ProgressBar(maxval=500)
for i in range(500):
    # Do some work
    time.sleep(0.01)
    bar.update(i)
bar.finish()
# 100% |######################################################################################################################################|

  
# widgets = [' [',
#          # Use {elapsed} instead of %(elapsed)s
#          'elapsed time: {elapsed}',
#          '] ',
#            tqdm.format_meter(0, 100, 0, '$', ' (', ') ', 'ascii'),
#           ]

# # Create a progress bar object with total=100 and widgets
# bar = tqdm(total=100, 
#                 widgets=widgets)

# # Loop over 100 iterations
# for i in range(100):
#     # Do some work
#     time.sleep(0.1)
#     # Update the progress bar
#     bar.update(1)

# # Finish the progress bar
# bar.close()
