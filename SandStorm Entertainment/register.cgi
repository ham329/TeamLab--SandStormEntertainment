#! /bin/bash
echo "Content-type: text/html"
echo ""

success=""
if [[ ! -z "$QUERY_STRING" ]]; then
        username=$(echo "$QUERY_STRING" | sed -n 's/^.*username=\([^&]*\).*$/\1/p' | sed 's/ //g')
        exist=$(grep $username pointsdb | sed 's/ .*$//')
        if [[ $username == $exist ]]; then
                success="<h3 style="color:red">Sorry. That username is already taken.</h3>"
        else
                echo "$username 0" >> pointsdb
                success="<h3>You have successfully registered.</h3>"
        fi
fi

cat << EOF

<html>
<head>
        <title>Contact Us</title>
        <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
        <div>
                <h1>SandStorm
                <img src="http://www.harvesttrail.com/ss_logo.gif" width=30px height=30px>
                Entertainment
                </h1>
        </div>
        <div id="page">
                <div id="content">
                        <div class="transbox">
                                <ul>
                                        <li><a href="http://cit160lab.sandbox.csun.edu/~team20/index.html">Home</a></li>
                                        <li><a href="http://cit160lab.sandbox.csun.edu/~team20/about.html">About Us</a></li>
                                        <li><a href="http://cit160lab.sandbox.csun.edu/~team20/cgi-bin/contact.cgi">Contact Us</a></li>
                                        <li><a href="http://cit160lab.sandbox.csun.edu/~team20/cgi-bin/balance.cgi">Balance</a></li>
                                        <li><a href="http://cit160lab.sandbox.csun.edu/~team20/cgi-bin/redeem.cgi">Redeem</a></li>
                                        <li><a class="active href=#Register">Register</a></li>
                                </ul>
                        </div>
                        <form>
                                Enter your username:<br>
                                <input type="text" name="username">
                                <br>
                                <input type="submit">
             </form>
                        <br>
                        $success
                        <br>
                        <div id="footer">
                                <p>Copyright &copy; 2016 SandStorm Entertainment (TEAM 20)</p>
                        </div>
                </div>
        </div>
</body>

</html>

EOF

exit 0








