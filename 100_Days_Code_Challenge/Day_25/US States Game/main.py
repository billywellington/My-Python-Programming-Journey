import turtle
import functions

screen = turtle.Screen()
screen.title("My U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
turtle.write(answer_state)
turtle.penup()
turtle.goto((100, 200))
turtle.mainloop()







screen.exitonclick()
