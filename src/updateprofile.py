import tornado.web
import json
import Profile

class updateHandler(tornado.web.RequestHandler):
    def get(self):
        L = self.request.path.split("/")
        uname = L[2]
        print(uname);
        info = Profile.D[uname]
    
        self.render("updateprofile.html", currentname = info["name"])


    def post(self):            
            J=json.loads(self.request.body)
            preferredName = J["preferredName"]
            dob = J["birthdate"]
            ppic = base64.b64decode(J["pic"])
            print("WE GOT:",preferredName,dob,ppic[:20])

            L = self.request.path.split("/")
            uname = L[2]
            info = Profile.D[uname]
            info["name"] = preferredName
            info["dob"] = dob

            resp={"ok": True}
            self.write( json.dumps(resp) )