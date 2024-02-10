#48report by Khalid Saif


in this report, i will be summarizing the programs 45-47.

##Report of [45dndstats.py](https://github.com/Khalidsaif11/mcb185_homework/blob/63efdad4f42013ea90d26c06c16cbe88a3221e27/45dndstats.py)
====================================================

in this report, i will present how we created a program that 
			determines the **average stat value** using four different rules.
i co-authored with ethan & george to create this program.

1. for rolling a 3 six sided dice, we assigned the 
			three dices(d1, d2, d3) to <random.randint(1, 6)>. 
			we also just used one loop.
then, we just used 10000 trials, and in each trial, those three dices add up.
			for the finalization, we just got the average, then printed average.

2. for rolling 3 six-sided dice, but re-rolling any 1s, 
			it is exactly same procedure as before. except, we put 3 <if> conditions.
those conditions states that if any of those three dices 
			result in one, that dice should be re rolled again.

3. for rolling pairs of six-sided 3 times, and taking 
			the maximum each time, it was a mix of the previous two.
			we used two loops & conditions. 
we put a condition that compares the results of a 
			pair dice, and takes the maximum. this applies to all trials.

4. lastly, for rolling 4 six-sided dice, and then dropping
			the lowest die roll, it is similar to the second rule above. 
			we assigned the four dices to the <random.randint(1, 6)>.
then, we put several conditions that drops the lowest score, 
			and takes the other three dices. 

for result, we got :

3D6      10.4623
3D6r1    11.7803
3D6x2    13.4
4D6d1    12.2574

this is close enough to the expected estimation. we use the <\t> in 
			the print statement to make our output look like a table and organized.



##Result of [46savingthrows.py](https://github.com/Khalidsaif11/mcb185_homework/blob/63efdad4f42013ea90d26c06c16cbe88a3221e27/46savingthrows.py)
==================================================

for this program, we created a program that
				**simulates saving throws against dcs of 5, 10, and 15**. 
				and, getting the probability of success
					*normally* or with *advantage/disadvantage*.

1. for the advantage, we want to take the highest of the two dices. 
				and, this high score should be greater
				than the difficulty class in order to gain a success.
2. for the disadvantage, we want to take the lowest of the two dices. 
				and, this low score chose also should 
				be greater than the difficulty class to gain a success.
3. for normal, we just used one dice basically. 
				the only condition was that the dice
				score needs to be greater than difficulty class in order to gain a success.

to summarize, we used mix of conditions & loops to create this program. 
				we just divided the total successes 
				over total trial to get the probaility of each of three conditions wanted.
we also put a print statement before each outer loop to 
				make the headers so that the output appears as a table.

our result was:

DC      adv
5       0.968
10      0.798
15      0.506


DC      dis
5       0.641
10      0.295
15      0.089


DC      norm
5       0.79
10      0.568
15      0.298

this is close enough to the expected estimation.


##Result of [47deathsaves.py](https://github.com/Khalidsaif11/mcb185_homework/blob/63efdad4f42013ea90d26c06c16cbe88a3221e27/47deathsaves.py)
==================================================

for this program, we wanted to create a 
	program that **simulates death saves**. 
				then, we need to get the *probability one dies, stabilizes or revives*.

for this program, we used conditions, one loop, and while. 
				we could not think of a way to solve this with another 'for' loop.

-we first used an outer loop that takes care of the number of trials. 
				then, we used a 'while' loop. 
					this loop will continue as long as success & failures below 3.
if any of the two is 3, then this while loop will break. 
-then, we used a bunch of increments for 
	deaths, successes, failures, & revives.
-for finalization, we just wrote the probabilities of deaths, 
				stabilizations, & revives.
-lastly, we printed each of the probabilities.

our result was:

die 0.407
stabilize 0.4103
revive 0.1827

this is close enough to the expected estimation.

**END**
------------------------------------------------------