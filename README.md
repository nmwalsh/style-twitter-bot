# style-twitter-bot

🌃 Reimagine any image in the style of Van Gogh's _The Starry Night_! 🌕

This is a twitterbot that performs the following steps in order once initialized:
    
    - listen for tweets targeted at a given twitter account
    - pull the image from the tweet 
    - perform neural style transfer on the input image
    - reply to the tweeter with the output image in a reply tweet (also saves output to local disk)

## Examples
Here are examples from my own bot, implemented with this code as-is. To see more examples, you can visit the bot [@StarryNightBot](https://twitter.com/starrynightbot). 

*note* Due to recent changes in the Twitter dev API 😞, my bot is no longer live, so tweets to it won't return anything. Sorry!

Baseball Stadium Example
![Baseball Stadium Example](/examples/baseball-example.png)

Stanford University Example
![Stanford University](/examples/stanford-example.png)

Star Wars Example
![Star Wars Poster](/examples/starwars-example.png)

## Install
- For Ubuntu, ```$ pip install Pillow``` in place of PIL. No changes to import necessary.
- For Ubuntu, ```$ chmod a+x style_transfer.sh``` to allow the shell script to run

## Run
```$ python twitterbot.py```

## Credit
Uses the `starry_night.t7` weights file found in the [fast-neural-style](https://github.com/jcjohnson/fast-neural-style) repo from the paper [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://cs.stanford.edu/people/jcjohns/eccv16/)