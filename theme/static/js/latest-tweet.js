window.pf = {
    key: "latest-tweet",
    tweetCallback: function(data){
        this.handleData(data);
        lscache.set(this.key, data, 60);
    },
    handleData: function(data){
         var p = document.createElement('p'),
            txt,
            link = document.createElement('a'),
            tweetNode = document.getElementById("latest-tweet");
        if (data && data[0] && data[0].text) {
            txt = document.createTextNode("Latest tweet: " + data[0].text);
            link.appendChild(txt);
            link.href="https://twitter.com/projectfondue/status/" + data[0].id_str;
            link.className = "shadow-txt";
            p.appendChild(link);
            p.className = "tweet";
            tweetNode.appendChild(p);
        }
    },
    init: function(){
        var json = lscache.get(this.key);
        if (json) {
            this.handleData(json);
        } else {
            this.makeScriptNode();
        }
    },
    makeScriptNode: function(){
        var scr = document.createElement("script");
        scr.src = "https://api.twitter.com/1/statuses/user_timeline.json?screen_name=projectfondue&callback=pf.tweetCallback&count=1";
        console.log(scr);
        scr.type = "text/javascript";
        document.body.appendChild(scr);
    }
}
pf.init();

