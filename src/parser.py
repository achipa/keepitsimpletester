from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

#<div class="repository_list_item">
#<div class="package_icon">
#    <img src="http://static.maemo.org/static/3/35b586d4164f11dfa42fdb254870f7b5f7b5_netmon_icon" />
#</div>
#    <div class="title"><a title="QA test page for netmon" href="/packages/package_instance/view/fremantle_extras-testing_free_armel/netmon/0.6-1/">netmon</a></div>
#    <div class="version"><a title="QA test page for 0.6-1 of netmon" href="/packages/package_instance/view/fremantle_extras-testing_free_armel/netmon/0.6-1/">0.6-1</a></div>
#    <div class="karma">Karma: -2 </div>
#    <div class="karma">Karma: <span style="color:#00aa00">13</span> </div>
#    <div class="karma">Karma: -2 <div class="net_nemein_favourites"><div class="bury_btn" title="You have voted on this item already."></div></div></div>
#    <div class="karma">Karma: <span style="color:#00aa00">22</span> <div class="net_nemein_favourites"><div class="fav_btn" title="You have voted on this item already."></div></div></div>
#    <div class="waiting_since">2010-06-14 05:45 UTC</div>
#</div>

    def resetPackage(self):
        self.package = { 
            "name" : "",
            "pname" : "",
            "version" : "",
            "karma" : 0,
            "voted" : False,
            "myvote" : True,
            "status" : "",
            "link" : "",
            "imageurl" : "",
            "waiting" : ""
            }
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.parentlist = []
        self.packages = {}
        self.pages = 0
        self.resetPackage()
        self.lasttag = ""
        
    def handle_starttag(self, tag, attrlist):
        self.lasttag = tag
        attrs = dict(attrlist)
        if (tag == "div"):
            try:
                self.parentlist.append(attrs["class"])
            except:
                self.parentlist.append("")
            
        try:
            if tag == "img" and self.parentlist[-1] == "package_icon":
                self.package["imageurl"] = attrs["src"]
        except: pass
         
        try:
            if tag == "a" and attrs["class"] == "last_page":
                self.pages = int(attrs["href"].split("=")[1])
        except: pass
            
        try:
            if tag == "div" and (attrs["class"]=="fav_btn" or attrs["class"]=="bury_btn"):
                self.package["voted"] = True
                self.package["myvote"] = attrs["class"]=="fav_btn"
        except: pass
            
        try:
            if self.parentlist and tag == "a" and self.parentlist[-1] == "title":
                if attrs["href"].startswith("/packages/package_instance"):
                    self.package["link"] = attrs["href"]
                    self.package["version"] = attrs["href"].split("/")[-2]
                    self.package["pname"] = attrs["href"].split("/")[-3]
        except: pass
         
#        print "Encountered the beginning of a %s tag" % tag

    def handle_data(self, data):
        try:
            if len(self.parentlist) > 2 and self.parentlist[-1] == "karma" and self.parentlist[-2] == "repository_list_item":
                self.package["karma"] = int(data.split(":")[1])
        except: pass
    
        try:
            if len(self.parentlist) > 2 and self.parentlist[-1] == "karma" and self.parentlist[-2] == "repository_list_item" and self.lasttag == "span":
                self.package["karma"] = int(data)
                self.package["status"] = " (Unlocked)"
        except: pass
        
        try:
            if self.parentlist[-1] == "waiting_since" and self.parentlist[-2] == "repository_list_item":
                self.package["waiting"] = data
        except: pass
        
        try:
            if self.parentlist[-1] == "title" and self.parentlist[-2] == "repository_list_item":
                self.package["name"] = data
        except: pass
        
    def handle_endtag(self, tag):
        if (tag == "div" and self.parentlist):
            if (self.parentlist.pop() == "repository_list_item"):
                if self.package["pname"]:
                    self.packages[self.package["pname"]] = dict(self.package)
                self.resetPackage()
            
#        print "Encountered the end of a %s tag" % tag
