# You can find the game at the URL below:
#http://www.codeskulptor.org/#user42_mmsEyIRlF9_5.py

#"Stopwatch: The Game"

###################################################
import simplegui 

# define global variables
counter = 0
total_attempts = 0
successful_stops = 0
running = True #True when the stopwatch is running and False when the stopwatch is stopped
print '**Try to stop the watch on a whole second**'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D    
def format(t):
    minutes = (t / 600) % 600
    tenth_of_min = (t / 100) % 6
    sec = (t / 10) % 10
    tenth_of_sec = t % 10
    return str(minutes) + ":" + str(tenth_of_min) + str(sec) + "." + str(tenth_of_sec)

# define event handler for timer with 0.1 sec interval       
def tick():
    """adds +1 to counter every 0.1 seconds"""
    global counter
    counter += 1
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"       
def start():
    """starts stopwatch"""
    timer.start()
    
    
def stop():
    """Stops timer, sets stop to False and adds 1 to successful_stops and/or total_attempts"""
    global total_attempts, successful_stops, running
    timer.stop()
    running = False
    if running == False:
        if counter % 10 == 0 and counter != 0:
            successful_stops += 1
            total_attempts += 1
        elif counter != 0:
            total_attempts += 1
    
    
def reset():
    """Stops stopwatch and resets all global variables"""
    global counter, total_attempts, successful_stops
    timer.stop()
    counter = 0
    total_attempts = 0
    successful_stops = 0
    
# define draw handler    
def draw(canvas):
    #actually draws on canvas
    #doesn't change the position, only uses it
    text = format(counter)
    canvas.draw_text(text, [50,100], 36, "green")
    canvas.draw_text(str(successful_stops) + '/' +str(total_attempts), (140,30), 20, "white")
    canvas.draw_text('Right ' + '|' + ' Tries', (115,50), 15, "red")
    
    
# Create frame and timer
frame = simplegui.create_frame("Stop Watch Game", 200, 190)
timer = simplegui.create_timer(100, tick) # 100 milliseconds
frame.set_draw_handler(draw)

# Event handlers for buttons        
button1 = frame.add_button('Start Timer', start, 100)

button2 = frame.add_button('Stop Timer', stop, 100)

button3 = frame.add_button('Reset', reset, 100)



# start frame
frame.start()
