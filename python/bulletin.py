from bottle import route, run, template, request, get, static_file
import fileUtil
import datetime

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="css")

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="js")

@route('/bulletin')
def bulletin():
    currentList = fileUtil.readFile("sample.txt")

    return template('index', text = currentList)

@route('/bulletin', method='POST')
def do_hello():
    name = request.forms.name
    txt = request.forms.message
    timeNum = ""

    if len(name) == 0:
        name = "名無しさん"

    for time in range(16):
        timeNum += str(datetime.datetime.now())[time]

    currentList = fileUtil.readFile("sample.txt")
    newList = currentList
    if len(txt) != 0:
        newList = currentList + "NAME: " + name + '<br>' + "TIME: " + "{}".format(timeNum) + "<br>" + "TEXT: " + txt + "<br><br>"

    fileUtil.writeFile("sample.txt", newList)

    return template('index', text=newList)

run(host='localhost', port=8080, debug=True)