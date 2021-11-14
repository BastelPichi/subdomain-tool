from flask import Flask, request, render_template
import CloudFlare

email = "cloudflareaccount@email.com"
token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
zoneid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/createsubdomain", methods=["POST"])
def createsubdomain():
    try:
        name = request.form.get("name")
        domain = request.form.get("domain")
        type = request.form.get("type")
        pointsto = request.form.get("pointsto")
        if name != "":
            if domain != None:
                if type != None:
                    if pointsto != "":
                        if type == "A" or type == "CNAME":
                            if domain == "s" or domain == "dot":
                                cf = CloudFlare.CloudFlare(email=email, token=token)    
                                dns_records = {"name": f"{name}.{domain}", "type": f"{type}", "content": f"{pointsto}", "proxied": False}
                                cf.zones.dns_records.post(zoneid, data=dns_records)
                                return "Your Subdomain was registered!"
                            else:
                                return "You can only register .s.pichisdns.com or .dot.pichisdns.com, Cheater"
                        else:
                            return "You can only create A or CNAME records, cheater"
                    else:
                        return "You cant point to something empty! <a href=/>try again</>"
                else:
                    return "You have to select the record type! <a href=/>try again</>"
            else:
                return "You have to select the domain! <a href=/>try again</>"
        else:
            return "The name you entered cannot be empty! <a href=/>try again</>"


    except Exception as e:
        print(e)
        return("There seams to be an Error with the api, the name you enetered was not coorect or there was an uknown error. <a href=/>try again</>")

if __name__ == "__main__":
    app.run()
