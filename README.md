# AoC2022
Advent of Code 2022

To run the code:

```
python aoc2022.py --dir dir --day D --star S
```
with:

- dir is the input data directory name
- D is the day number
- S is the star number (1 or 2)

## My difficulties

### Day 1 - Calorie Counting

As usual, the first exercises aren't really difficult. My main point was that I hadn't prepared my environment yet.
I had to copy/update my 2019 setup (better than my 2020 one) and I really did the exercises so late!

### Day 2 - Rock Paper Scissors

I hesitated: should I rename ABC and XYZ to rock-paper-scissor, to really understand what are the fight? 
Should I at least remane XYZ to ABC?
Finally, I decided to create a map saying for each letter which letter it beats, eith ABC and XYZ letters.

### Day 3 - Rucksack Reorganization

I didn't really remember how the `re` library worked but after a quick check on Internet, I found this day easy.

### Day 4 - Camp Cleanup

For the partial overlap exercise, I had a moment when I thought: "Should I take into account the case that an intervall
would be described in the descending order?"
I decided not to do it and that was coll. Such easier to code if an overlap only means that the right number of the 
first interval is higher than the left number of the second interval, or the inverse.

### Day 5 - Supply Stacks

OK, serious data parsing starts here. I am not the one who copies her input data and reorders it manually. But I decided
that I could use numpy to transpose my array-like data :laughing:

The rest wasn't a big problem.

### Day 6 - Tuning Trouble

Actually, my answer was so short that I think that this problem wasn't for a Python developer.

### Day 7 - No Space Left On Device

Ouch, it hurted! I decided immediatly that I should be clean in my code: creating a Directory and a File class, methods
to navigate, to evaluate the sizes. I started it pretty well but it took so much time that I had to finish during the 
next week-end.

My Directory class had attributes `parentDirectory` and `childrenDirectories` but it wasn't so clear at the begining 
how I could navigate but keeping what I had already stored in my previous directory. 
I finally created a `__copy__` method. I imagine that anyone who has already studied the object programming would have
known it... I have learned all my knowledge about objects simply coding them. 
(_Yes, I should at least read a book about object-oriented programming._)

To be honest, I realized afterward that I was also helped by the fact that a friend from Ladies of Code said that two 
different directories could have the same name. Without this little sentence, I would have tried to define my 
directories by their names. Sorority is great.

### Day 8 - Treetop Tree House

It is not my cleanest piece of code, to be honest. And I know that making it clear wouldn't be so easy. 
Another point is that I was frustrated not to find a nice way to find the first digit in a list that if higher than a 
given input.

Well, I did it and at least it is readable.

### Day 9 - Rope Bridge

The first star was OK. But then... I thoght that extend the rope would be straightforward. Actually, not.

First, I decided to keep my "head" and create a "tail" with more than one node. And then, each node would have to 
follow the previous one. But it was a nightmare to understand what I was writing.
After my saturday shower, I realized that in fact what I could do was:
- first calculate the whole path of the head,
- then calculate the whole path of the first follower,
- and iterate on all the nodes

It was a way easier, even if I needed to refactor my first star code.

Then, the two test cases passed. But my first answer was too low! I couldn't figure the problem. I spent a certain 
amount of time then to print my rope last node path in an understandable way and checked. The problem occured only after
enough steps, with enough nodes in the rope. Sometimes, I jumped a cell! OK, it was because you can meet the case where
the previous node is 2 cells away both in the vertical and in the horizontal direction. It didn't happen with small 
ropes/small amount of steps.

### Day 10 - Cathode-Ray Tube

I am not like everyone. I didn't have hoard moments with the starting cycle at 0, but the starting X value set to 1. 
Even this question of "during the cycle" and "after the cycle" was pretty clear for me.

I had more problems with the second part and the sprite. My brain really wanted that the CRT would follow the 
instructions and the sprite would sweep along the screen. I had alwas to fight against my brain. At the end, I managed 
to obtain the result but:
- first I was not sure. I had to copy my answer, paste it in Excel and add a conditional formatting to read the letters.
- and finally... my first column is still wrong. I know that I have still an error in the code but anyway, haven't I 
proposed the good eight letters?

### Day 11 - Monkey in the Middle

This data was quite simple to parse, actually. 
My first thought was just: "I hope that the test is always about a division!"
What I don't like in my code is that I use an `eval` but that's the hard law of the life.

For the second part, obviously I got into a problem of too large numbers first. Then (after another shower) I realized 
that I could work with the rest of divisions for each item. So, in place of representing 42 by 42, if the monkeys 
divisors are 5 and 7, I represent it by `{5: 2, 7: 0}`. I took a sheet of paper to verify that I could work with a 
square function with this representation 
(My daughters: "What are you doing mum? We don't need any help in maths." Me: "Well, _I_ would need your help if you 
were nice mathematical daughters.")

And the day after, a friend from Ladies of Code told me that we had already run in such a problem in a previous AoC...

### Day 12 - Hill Climbing Algorithm

I was like "well, now Valérie you need to write a recursive function." And I was quite proud that I did it quite fast.
It ran well on the test example. But on my input data, it wasn't the same story. So after waiting tooo long, I decided 
to try something else.

Honestly, my husband was a great help. He just told me: "I did it like Liquid War." And anybody who knows the Liquid 
War algorithm(*) knows that there is a simple mapping that works very well here. 
Once you have the mapping, both exercises are easy to do.

(*) Well, that means: him, Thomas Colcombet, and me + the ones who have read this page: 
https://ufoot.org/liquidwar/v5/techinfo/algorithm

### Day 13 - Distress Signal

49 years old and still afraid by recursivity. It took me so many years to understand that you first define the stop
condition! But OK, let's go. At least, the parsing is easy in Python.

Then I had to make some small changes because I compared lists and integers in some cases, even if I really tried to
avoid this.

And last but not least: when I parse the data, I remove the last item by default. **It is not a good idea when the
separator is `\n\n` in place of `\n`.** Each time, I forget. Each time, my test passes and not my puzzle input.
Shame on me.

Finally: my program ran, the test was OK, but I didn't get the good answer. I think that it is because of this, in the
instructions: _If the lists are the same length and no comparison makes a decision about the order, continue checking
the next part of the input._. In my case, if the first list is empty, I say "OK", it is the smallest one. I forgot to
check if the right one is empty too. And it is not so easy: I have to keep the right side of my packets for this...

It took me so much time to deal with the equalities... Recursivity and my brain: not best friends.

For the second part, I simply decided to implement a merge sort algorithm because I discovered it not such long ago and
I liked the idea. It was really easy for me.

### Day 14: Regolith Reservoir

No problem to do the first star. But I decided to define the rocks only but a list of their coordinates. It was OK, but
for the second star it led me to a real performance problem. It wasn't such a deal to define the rocks in a matrix-like
map. But needed to do it again from scratch. Obviously, at a moment I got an error... OK, done. The second star needs
only concentration and precision.

### Day 15: Beacon Exclusion Zone

### Day 20: Grove Positioning System

My main problem was that I didn't deal well with the case when a number is higher than the length of the list. I had to
add another test, that I did manually on a sheet of paper. And then: I returned the good list, but the last digit on the
first place. It is totally OK, but as I also checked the complete list in my test, I had to figure out it... And to
change the expected value.

Concerning the second star, as I used congruences from the beginning, I had no difficulty. I only needed to ensure that
I didn't recalculate the position of each number before mixing the list again.

### Day 21: Monkey Math

First star: Always problems with recursivity. This time, I forgot to return something in the case I am not in the stop
condition. Once I did it, it was easy.

Second star: I thought a short time about recursivity. But in the end it was fun to "inverse the monkeys". I took a
facility, nevertheless: I knew that the human, was the left part of an addition. I didn't test to create the
corresponding monkey-human operation.

### Day 23: Unstable Diffusion

Once I decided to describe the problem correctly in two classes, it was pretty straightforward to do the part 1.
Problems:

- the elves depend on the map and the map depends on the elves. Must be cautious on it (when I move an elf, I move its 
  elves map at the same time).
- Also: never forget to add 1 in a range to get the last value.
- to round the orientations, I decided to create a sequence of directions for each first direction. The easiest way.

I had forecasted that the second step was to define the number of round to spread totally the elves. I decided to do it
like a dumb, and it worked: I increased my margins around the map and then ran the moves until the elves don't want to
change their places anymore. It was a little long (some seconds) but OK. I worried that my increased margins weren't
enough. With only 100 extra borders, it was OK! And thanks to my elfes objects that are able to tell me at any moment if
they want to move or not, it was really easy to define the stop condition.

### Day 24: Blizzard Basin

Talking with Christian, I realized that the map was deterministic, so actually, it is just a travel in a 3D map with
some limitations (you can't go to the Z-) So my idea is that I will map the 3D map and count like in day 12 the lengths
of the possible paths. Let's see.

Actually, I was able to do it easily. Only one point: Christian told me that I could have to wait before entering the
blizzards. It helped me to forecast this case from the beginning.