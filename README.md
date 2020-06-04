Milan Mauck - mmauck@pdx.edu
Graham Desmond - gdesmod@pdx.edu

The name of the project was Reverb effect (We changed it halfway through to a keyboard mouse instrument)

This project uses the keyboard and mouse as an instrument to play a synth. By swiping the mouse right, you can transpose up by an octave, and by swiping left, you can transpose down an octave.

To setup the project, you need Python 3.7, and run the following command to install dependancies:

pip install synthplayer pygame sounddevice synthesizer

Next, you can run our program with the following command:

python keyboard.py

In terms of testing we spent some time playing the keyboard and transposing it to make sure it was up to our specifications. Throughout the course of the project we also incrementally tested specific aspects of the code to make sure each subsection was working as it should before bringing it all together. Overall though, we are pretty happy with the results. We included a demo video of the instrument being played as part of our submission.

There are a few things that could be better that we had expected to be able to do but ran into complications in the code/libraries we were using. We used about 5 different audio libraries before landing on using sounddevice to play/stop the sound. However because we used this library we weren’t able to play several sounds at once which disappointed us. In the future, I think we would change 2 things. One, we would make it polyphonic, and 2 we would try to decrease the latency in playing and transposing the keyboard.