from bottle import route, run, template, request
import fileUtil

@route('/bulletin')
def bulletin():
    currentList = fileUtil.readFile("sample.txt")

    return template('index', text = currentList)


@route('/bulletin', method='POST')
def do_hello():
    txt = request.forms.message
    currentList = fileUtil.readFile("sample.txt")
    newList = currentList + txt + '<br>'

    fileUtil.writeFile("sample.txt", newList)

    return template('index', text=newList)

run(host='localhost', port=8080, debug=True)