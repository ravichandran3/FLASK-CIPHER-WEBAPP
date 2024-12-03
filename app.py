from flask import Flask, render_template, request, flash
from CIPHER_CLASS import CIPHER

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def output():
    if request.method == "POST":
        flash("text")
        #input_data = list(request.form.values())
        input_data = request.form['enter your text here']
        selection_type = request.form.get("CIPHER")
        key = int(request.form.get("key_value"))
        #print("user input:{} \nkey value:{}\nselection type:{}".format(input_data, key, selection_type))
        #print(type(input_data), type(key), type(selection_type))
        if selection_type == "ENCIPHER":
            cipher = CIPHER(str(input_data), key)
            output = cipher.ENCRYPT()
            # print(output)
           # print(cipher.ENCRYPT())
        elif selection_type == "DECIPHER":
            cipher = CIPHER(input_data, key)
            output = cipher.DECRYPT()
            # print(output)
        #selection_type = selection_type.lower()
        output = output.lower()
        final_output = "your {} value is: {}".format(selection_type, output)
        return render_template("index.html", output=output, selection_type=selection_type)
    return render_template("index.html")


@app.route("/cipher", methods=["GET", "POST"])
def cipher():
    """if request.method=="GET":
        return render_template("index.html")"""
    if request.method == "POST":

        # return render_template("index.html", data=[{'cipher': 'ENCIPHER'}, {'cipher': 'DECIPHER'}])
        return render_template("index.html")


"""
@app.route("/ciphewwr", methods=['POST', 'GET'])
def fun_fun_fun():
    if request.method == "GET":
        return f"The url '/cipher' is accessed directly.Try going to '/' to submit form"
    if request.method == "POST":
        select = request.form.get('x')
        key = request.form.get('key_value')
        user_input = request.form.get('user_input')
        if select == "ECNIPHER":
            cipher = CIPHER(user_input, key)
            return "Your encipher value is:"+cipher.ENCRYPT()
        elif select == "DECIPHER":
            cipher = CIPHER(user_input, key)
            return "Your encipher value is:"+cipher.DECRYPT()

"""


"""
if request.method == "POST":
        select = request.form.get("x")
        key = request.form.get("key_value")
        user_input = request.form.get("user_input")
        print("key:", key)
        print("user input:", user_input)
        cipher=""
        if select == "ENCIPHER":
            cipher += CIPHER(user_input, key)
            print("key2:",key)
            #return "Your encipher value is:"+cipher.ENCRYPT()
        elif select == "DECIPHER":
            cipher += CIPHER(user_input, key)
            #print("Your encipher value is:"+cipher.DECRYPT())
            print("your {} value is {}".format(select,cipher))
    return render_template("index.html",cipher="your {} value is:{}".format(select,cipher))"""

if __name__ == "__main__":
    app.secret_key = 'mutinca "key" ah kandu pudi  neethan thairiyamana aal aachae😂😂😂😂😂😂😂😂'
    app.run(host="127.0.0.1",port=5000)
