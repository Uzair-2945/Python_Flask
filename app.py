from flask import Flask,render_template,request,redirect,url_for,jsonify

app = Flask(__name__)
notes=[]

@app.route("/")
def home():
    return render_template("index.html",notes=notes)

@app.route('/addNum', methods=['POST'])
def add_numbers():
    data = request.get_json()   # get JSON data from Postman

    num1 = data.get('num1')
    num2 = data.get('num2')

    result = num1 + num2

    return jsonify({
        "num1": num1,
        "num2": num2,
        "sum": result
    })

@app.route("/add",methods=["POST"])
def add_note():
    note=request.form.get("note")
    if note:
        notes.append(note)
    return redirect(url_for("home"))
# Delete a note by index
@app.route("/delete/<int:index>")
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect(url_for("home"))

# Edit a note by index
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_note(index):
    if request.method == "POST":
        new_note = request.form.get("note")
        if new_note:
            notes[index] = new_note
        return redirect(url_for("home"))
    return render_template("edit.html", note=notes[index], index=index)




if __name__ == "__main__":
    app.run(debug=True)