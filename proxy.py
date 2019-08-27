from flask import Flask, request
import subprocess
import json

try:
    with open('auth.cfg', 'r') as auth:
        auth_path = auth.readline().rstrip()
except:
    auth_path = None
    pass
with open('getb64.sh', 'w') as b64:
    b64.write('cat %s'%(auth_path) + ' | base64')
authB64 = subprocess.Popen(['sh', 'getb64.sh'], stdout=subprocess.PIPE).stdout.read().rstrip()

def toggle_snapshot(req, operation):
    print("toggle_snapshot called")
    config = None
    for k in req:
        cfg = k
        with open('tmp_json', 'w') as tmp:
            tmp.write(k)
        with open('tmp_json', 'r') as tmp:
            config = json.load(tmp)
    cluster = config["cluster"]
    managedVolume = config["manageVolumeId"]

    print("{op} called for {cluster} on ManagedVolume:::{id}".format(
        op = operation,
        cluster=cluster,
        id=managedVolume
    ))
    path = 'https://{cluster}/api/internal/managed_volume/ManagedVolume:::{id}/{operation}'.format(
        cluster=cluster,
        id=managedVolume,
        operation=operation
    )
    
    response = subprocess.Popen(['curl', '-X', 'POST', '-H', "Authorization: Basic %s"%(authB64), path, '--insecure'], stdout=subprocess.PIPE)
    result = response.stdout.read()
    return result

app = Flask(__name__)
@app.route("/begin_snapshot")
def begin_snapshot():
    #return {"message": toggle_snapshot(request.form,'begin_snapshot')}, "OK"
    try:
        return {"message": toggle_snapshot(request.form,'begin_snapshot')}, "OK"
    except:
        return ("<h1>500 - Server did not receive correct parameters or could not handle request</h1>", "Internal Server Error")
#@app.route("/end_snapshot/<cdm>")
@app.route("/end_snapshot")
def end_snapshot():
    #return {"message": toggle_snapshot(request.form,'end_snapshot')}, "OK"
    try:
        return {"message": toggle_snapshot(request.form,'end_snapshot')}, "OK"
    except:
        return ("500 - Server did not receive correct parameters or could not handle request", "Internal Server Error")
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        app.run(str(sys.argv[1]), sys.argv[2], debug=True)
    else:
        print("Did not provid host port, defaulting to listening on 0.0.0.0:12345")
        app.run('0.0.0.0', 12345, debug=True)