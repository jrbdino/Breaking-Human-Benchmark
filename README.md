# Breaking Human Benchmark Test

### Currently Working
- Reaction Time
- Accuracy Test
- Typing Speed
- Number Memory
- Chimp Test

5 of 7 Human Benchmark tests have been broken with our Python scripts.
> made using pyautogui


### Reaction Time
The first and easiest solution we have implemented.  The User starts the clock, then the code watches the cursor's point for when it turns green and clicks then.
Plain and simple.

### Accuracy Test
This task was a bit more difficult. Implementing image matching and finding we could find the target on the screen.  Our image we look for is actually a 3 by 3 group of pixels of a light blue color.

### Typing Speed
Here we get a complex.  Implementing Tesserect for Python, we can now recongnize characters from images.  Using this we can pull plain text from the window and use type_write to type it blazingly fast into the prompt box.

