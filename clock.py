#!/usr/bin/python
import datetime
import Tkinter as tk

def NumWord(number):
  """
Just a bunch of numbers in word-form. Returns the 'number'th element which happens to be that number as a word. works for 0-99 should be good enough for a clock.
  """
  Words=["zero",
"one","two","three","four","five","six","seven","eight","nine","ten",
"eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"
"twenty-one","twenty-two","twenty-three","twenty-four","twenty-five","twenty-six","twenty-seven","twenty-eight","twenty-nine","thirty",
"thirty-one","thirty-two","thirty-three","thirty-four","thirty-five","thirty-six","thirty-seven","thirty-eight","thirty-nine","forty",
"forty-one","forty-two","forty-three","forty-four","forty-five","forty-six","forty-seven","forty-eight","forty-nine","fifty",
"fifty-one","fifty-two","fifty-three","fifty-four","fifty-five","fifty-six","fifty-seven","fifty-eight","fifty-nine","sixty",
"sixty-one","sixty-two","sixty-three","sixty-four","sixty-five","sixty-six","sixty-seven","sixty-eight","sixty-nine","seventy",
"seventy-one","seventy-two","seventy-three","seventy-four","seventy-five","seventy-six","seventy-seven","seventy-eight","seventy-nine","eighty",
"eighty-one","eighty-two","eighty-three","eighty-four","eighty-five","eighty-six","eighty-seven","eighty-eight","eighty-nine","ninety"]
  return Words[number]

def TimeWord(Hours,Minutes):
  """
Converts a time to words with lots of rounding...just like people. 
  """
  if Minutes==0:
    Minutesword=""
    Hoursword=NumWord(Hours)	
  elif Minutes<12:
    Minutesword=NumWord(Minutes)+" past"
    Hoursword=NumWord(Hours)
  elif Minutes<20:
    Minutesword="quarter past"
    Hoursword=NumWord(Hours)
  elif Minutes<45:
    Minutesword="half past"
    Hoursword=NumWord(Hours)
  elif Minutes<50:
    Minutesword="quarter till"
    if Hours==12:
      Hoursword=NumWord(1)
    else:
      Hoursword=NumWord(Hours+1)
  else:
    Minutesword=NumWord(60-Minutes)+" till"
    if Hours==12:
      Hoursword=NumWord(1)
    else:
      Hoursword=NumWord(Hours+1)
    
  return "It's "+Minutesword+" "+Hoursword

class clockapp():
  """
Full screen widget with an empty .label. Press ESC to quit.
  """
  def __init__(self):
    self.root = tk.Tk() 
    self.label = tk.Label() 
    self.root.overrideredirect(True) 
    self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight())) #fullscreen bit
    self.root.focus_set() # move focus to this widget
    self.root.bind("<Escape>", lambda e: e.widget.quit()) #press ESC to quit.
    self.update_clock() #we'll define this later
    self.root.mainloop()

  def update_clock(self):
    TheTime=datetime.datetime.now() #get the time.
    Hours=TheTime.hour #access just the hours
    Minutes=TheTime.minute # access just the minutes
    ampm="in the morning." # default to morning until proven later
    if Hours==12 and Minutes>45:
      ampm="in the afternoon"
    if Hours>12: # military time
      ampm="at night." # It's getting late
      Hours=Hours-12 # civilian time
      if Hours<5: # Not so late
        ampm="in the afternoon."
      elif Hours<6: # Just late enough
        ampm="in the evening."
    self.label.configure(text=TimeWord(Hours,Minutes)+' '+ampm, cursor='none', bg="black",fg="white",font=("Sans", 50),pady=self.root.winfo_screenheight()/2) # Fill out the label
    self.label.pack(fill='both') # make the background fill the whole widget
    self.root.after(20000, self.update_clock) #update every 20 seconds


def main():
  app=clockapp()
  app.mainloop()

if __name__ == '__main__':
  main()
