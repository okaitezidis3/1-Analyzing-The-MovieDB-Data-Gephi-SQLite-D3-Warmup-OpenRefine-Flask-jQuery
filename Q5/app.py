from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/signUp')
def signUp():
    return render_template('signup.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username']
    password = request.form['password']
    if (len(return_check_matrix(user,password)) == 0):
        return json.dumps({'status':'OK','user':user,'pass':password})
    else:
        return json.dumps({'status':'BAD','user':user,'pass':return_check_matrix(user,password)})


def return_check_matrix(username,input_password):
#Reference https://stackoverflow.com/questions/17140408/if-statement-to-check-whether-a-string-has-a-capital-letter-a-lower-case-letter
    check_matrix = [0]*3
    #Check Password*/
    #Check 8 character length*/
    if (len(input_password) > 8):
        check_matrix[0] = 1
    else:
        check_matrix[0] = 0
    #at least 1 uppercase character*/
    if any(x.isupper() for x in input_password):
        check_matrix[1] = 1
    else:
        check_matrix[1] = 0
    #at least 1 number*/
    if any(x.isdigit() for x in input_password):
        check_matrix[2] = 1
    else:
        check_matrix[2] = 0

    return_matrix = []
    for j in range(3):
        if (check_matrix[j] == 0):
            return_matrix.append(j+1)
    print(check_matrix)
    print("return check matrix",return_matrix)

    return return_matrix


if __name__=="__main__":
    app.run()
