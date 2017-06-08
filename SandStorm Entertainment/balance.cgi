#! /bin/bash
echo "Content-type: text/html"
echo ""
sent=""
if [[ ! -z "$QUERY_STRING" ]]; then
        name=$(echo "$QUERY_STRING" | sed -n 's/^.*name=\([^&]*\).*$/\1/p' | sed 's/+/ /g')
        email=$(echo "$QUERY_STRING" | sed -n 's/^.*email=\([^&]*\).*$/\1/p' | sed 's/%40/@/g')
        reason=$(echo "$QUERY_STRING" | sed -n 's/^.*reason=\([^&]*\).*$/\1/p' | sed 's/+/ /g')
        message=$(echo "$QUERY_STRING" | sed -n 's/^.*message=\([^&]*\).*$/\1/p' | sed 's/+/ /g' | sed 's/%0D%0A/\n/g')
        recipient=$(echo "$QUERY_STRING" | sed -n 's/^.*recipient=\([^&]*\).*$/\1/p' | sed 's/%40/@/g')
        test -e message.txt && rm -rf message.txt
        echo "Name: $name" >> message.txt
        echo "Email Address: $email" >> message.txt
        echo "Reason for Contacting Us: $reason" >> message.txt
        echo "$message" >> message.txt
        cat message.txt | mail $recipient
        sent="<h3 style="color:blue">Your message has been sent. Thank you!</h3>"
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
                                        <li><a class="active href=#ContactUs">Contact Us</a></li>
                                        <li><a href="http://cit160lab.sandbox.csun.edu/~team20/cgi-bin/balance.cgi">Balance</a></li>
                                        <li><a href="http://cit160lab.sandbox.csun.edu/~team20/cgi-bin/redeem.cgi">Redeem</a></li>
                                        <li><a href="http://cit160lab.sandbox.csun.edu/~team20/cgi-bin/register.cgi">Register</a></li>
              </ul>
              </div>
                     <header>Contact Us</header>
         <p>Wade Hart wade.hart.936@my.csun.edu</p>
         <p> Section 3 - Team 20 </p>
         <p> Aaron Habana aaron.habana.877@my.csun.edu </p>
         <p> Section 3 - Team 20 </p>
<p> Taylor Bennington taylor.bennington.316@my.csun.edu </p>
        <p> Section 3 - Team 20 </p>
         <p> Mark Lawton - mark.lawton.509@my.csun.edu </p>
         <p> Section 3 - Team 20 </p>
                                
 <form>
Questions? Comments? Concerns? Use the form below to get in touch with one of the members of our team!<br>
    <br>
      $sent
    <br>
         Who would you like to contact?<br>
    <select name="recipient">
    <option value="wrh78393@cit160lab.sandbox.csun.edu">Wade Hart</option>
    <option value="amh91725@cit160lab.sandbox.csun.edu">Aaron Habana</option>
    <option value="ttb14392@cit160lab.sandbox.csun.edu">Taylor Bennington</option>
    <option value="mrl29907@cit160lab.sandbox.csun.edu">Mark Lawton</option>
                                </select>
 <br>
 <br>
   Enter your name:
 <br>
<input type="text"  name="name">
 <br><br>
   Enter your email address:
 <br>
    <input type="text" name="email">
<br><br>
    Why are you contacting us?<br>
    <input type="text" name="reason">
<br><br>
   Write your message:<br>
     <textarea name="message" cols="60" rows="15"></textarea>
<br><br>
     <input type="submit">
</form>
                        
<div id="footer">
<p>Copyright &copy; 2016 SandStorm Entertainment (TEAM 20)</p>
</div>
</div><!--end of content-->
</div><!--end of page-->
</body>
</html>

EOF

exit 0











                              



