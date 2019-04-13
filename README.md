# Mensakreationen

a python based single-serving-site that serves interesting dishes based on a markov-chain generator based on real world dishes.

You can enjoy a live demo [here](https://8sq.de/mensakreationen).
Enjoy!

## Usage
Make sure you have `docker`.
Then it is as simple as
1. Build the container with `docker build -t mensakreationen .`.
2. Run with something like the command in `run.sh` (or directly go with `bash run.sh`).

## And the data?
I do not know, whether I am allowed to include the real dish-name data I have scraped. To replicate this, you will need a file called `speisen2.txt` (you can use a another name, make sure you modify the CMD directive in the `Dockerfile` accordingly) with your dishnames separated with newlines and without any parentheses or quotation marks (because the package **markovify** will fail on those characters).
