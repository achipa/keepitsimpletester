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
#
#    <div class="waiting_since">2010-06-14 05:45 UTC</div>
#</div>

    def resetPackage(self):
        self.package = { 
            "name" : "",
            "pname" : "",
            "version" : "",
            "karma" : 0,
            "voted" : False,
            "link" : "",
            "imageurl" : ""
            }
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.parentlist = []
        self.packages = {}
        self.resetPackage()
        
    def handle_starttag(self, tag, attrs):
        if (tag == div):
            try:
                self.parentlist.append(attrs["class"])
            except:
                self.parentlist.append("")
            
        if (tag == "img" and self.parentlist[-1] == "package_icon"):
            self.package["imageurl"] = attrs["src"]
         
        print "Encountered the beginning of a %s tag" % tag

    def handle_endtag(self, tag):
        if (tag == "div"):
            if (self.parentlist.pop() == "repository_list_item"):
                self.packages["z"] = dict(self.package)
                self.resetPackage()
            
        print "Encountered the end of a %s tag" % tag
