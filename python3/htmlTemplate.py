# Provide HTML output templages.
from string import Template

htmlContents = """
<html>
<head>
<meta http-equiv="cache-control" content="no-cache, must-revalidate, post-check=0, pre-check=0" />
<meta http-equiv="cache-control" content="max-age=0" />
<meta http-equiv="expires" content="0" />
<meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
<meta http-equiv="pragma" content="no-cache" />
<meta http-equiv="refresh" content="120" />
<style>
    html { display: table; margin: auto; height: 100%; }
    body { display: table-cell; vertical-align: middle; height: 100%; background-color: black; }
    .UserInfo { 
        border: solid 1px gray; width: 480px; float: left; 
        padding: 10 10 10 10; margin: 10 10 10 10; 
        background-color: gray; 
     }
     .ContentFrame { margin-left: 100px; }
    .Avatar img { width: 220px; float: left; border: solid 1px black; }
    .Handle { 
        float: left; clear: both; width: 50px; font-size: 22px; font-weight: bold; font-family: "Verdana"; color: darkgray; 
    }

    .Followers, .Following, .Tweets, .Likes { 
        clear: right; text-align: right; 
        margin-top: 8px; 
        font-size: 36px;
        font-weight: bold; 
        font-family: "Verdana";
        color: white;
    }
    .Followers { color: orange; }
    .DataLabel { clear: right; text-align: right; font-size: 12px; font-variant: small-caps; color: black; }
    .Banner { color: white; text-align: center; font-size: 50px; font-variant: small-caps; }
    .Timestamp { clear: both; color: darkgray; text-align: center; font-size: 42px; font-variant: small-caps; }
</style>
</head>
<body>
    <div class="Banner">logicalsw.com - Twitter Dashboard</div>
    <div class="ContentFrame">
        ${contents}
    </div>
    <div class="Timestamp">${timeinfo}</div>
</body>
</html>
"""
htmlTemplate = Template(htmlContents)

