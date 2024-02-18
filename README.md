# Breaking Human Benchmark
## Inspiration
We originally saw the Human Benchmark tests on the website [Human Benchmark](https://humanbenchmark.com/) and we wanted to complete as many of the tasks as we could as fast as possible.  

## What it does
Breaking Human Benchmark completes the tests on [Human Benchmark](https://humanbenchmark.com/) using optical character recognition (OCR) and image detection.

## How we built the different functions
### Packages and Dependencies
- python 3.9
- pyautogui
- pytesseract
- PIL
- pyinstaller
- [UB Mannheim fork of Tesseract](https://github.com/UB-Mannheim/tesseract)


### Reaction Time
The first and easiest solution we have implemented.  The User starts the clock, then the code watches the cursor's point for when it turns green and clicks then. Plain and simple.

### Accuracy Test
This task was a bit more difficult. Implementing image matching and finding we could find the target on the screen.  Our image we look for is actually a 3 by 3 group of pixels of a light blue color.

### Typing Speed
Here we get a complex.  Implementing Tesseract for Python, we can now recognize characters from images.  Using this we can pull plain text from the window and use type_write to type it blazingly fast into the prompt box.

### Number Memory
Using the pytesseract package again, we now pull the numbers shown, and type them into the answer bar simply.  However, the Tesseract Package is sometimes unreliable, getting up level 17, but sometimes getting stuck on level 1.

### Chimp Test
With a library of enough boxed numbers, we search and order the numbered boxes.  Then after collecting the level amount, we rapidly click through.

### Sequence Memory
Using precise timing we record the sequence of dots that turn white. Then replicate the pattern using clicks.  We see no end to this program.

## Challenges we ran into
Some of the benchmarks are resolution and browser specific due to the way we used pyautogui.

## Accomplishments that we're proud of
We are only expected to be able to complete 2-3 of the tests over the course of the weekend.  We exceeded that and completed 6 of the 8 benchmarks. We already have progress on 1 of the 2 remaining tests.

## What we learned
We learned how to use pyautogui to automate and control mouse and keyboard inputs.  We learned how pytesseract to do optical character recognition (OCR) on text and how to refine its accuracy.

## What's next for Breaking Human Benchmark
We would like to complete the 2 remaining benchmarks, so we could have all 8 completed automatically.

### Currently Working
- Reaction Time
- Accuracy Test
- Typing Speed
- Number Memory
- Chimp Test
- Sequence Memory

### Yet To Be Broken
- Visual Memory
- Verbal Memory

6 of 8 Human Benchmark tests have been broken with our Python scripts.

## Collaborators
- John Behrens
- Carson Mead
- Klayton Pagel
