from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
  count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,
                                130,
                                text="00:00",
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

button_start = Button(text="start", highlightthickness=0, command= start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="reset", highlightthickness=0)
button_reset.grid(column=2, row=2)

window.mainloop()
