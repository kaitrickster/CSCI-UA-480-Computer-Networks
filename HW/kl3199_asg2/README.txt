Author: Kai Liao
Computer Networks: Assignment 2

kl3199_asg2.pdf				theory question writeup
uitls.py     				functions that plot results
window.txt   				window sizes from AIMD simulation
congestion_collapse.txt			throughputs from congestion collapse simulation
congestion_collapse_simulator.py	wrapper that simulates congestion collapse by running sliding window for different window size


Question 2 & 3: Results generated from manually running python scripts and recording them


Question 4: 	Run congestion_collapse_simulator.py in IDE; throughputs are stored in congestion_collapse.txt
		Make sure last few lines in simulator.py are not commented. I added several lines to write to txt file


Question 5: 	Run python3 simulator.py --loss_ratio 0.0 --seed 1 --host_type Aimd --rtt_min 20 --ticks 10000 --queue_limit 10
	    	Window sizes are stored in window.txt; make sure line 92 to 94 are not commented if you want to reproduce results

