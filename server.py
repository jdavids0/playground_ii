from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')          
def enter():
    print ("Playground")
    return render_template ('index.html')

@app.route('/play')
def play():
    return render_template('index.html', boxes = 3)

@app.route('/play/<int:boxes>')
def playNumber(boxes):
    return render_template('index.html', boxes=boxes)

@app.route('/play/<int:boxes>/<color>')
def playColor(boxes, color="lightblue"):
    change_color = color
    return render_template('index.html', boxes=boxes, change_color=change_color)

if __name__=="__main__": 
    app.run(debug=True)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 