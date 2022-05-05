
<h1 class="peupasswd">Peupasswd: Advanced Password Manager</h1>
<p><span class="peupasswd">peupasswd</span> is an advanced security software use in generating uniques password for each of each service i.e you can generate special password for each of your social media or services with just one master password.</p>
    
<h2>How It Works</h1>
<p><span class="peupasswd">peupasswd</span> takes in a master password, the service name you wanna use the password for and the length of the password u want(never worry about the length you can choose as much as possible you dont need to cram it). Then it encrypt the master password in a way you can nerver guess of. Also you can retrieve/check ur passwordagain by doing same way.</p>
    
<ol>
    <h2>Instructions:-</h2>
    <li>Create a master password in your brain.</li>
    <li>Enter the service name <span class="note">note: you will need this when trying to check/retrieve password</span>.</li>
    <li>Now click generate to generate the unique password. you can always generate the same password later by simply giving the same master password and service name. but no one could generate the same password as long as you dont share your master password to anyone. this is why I call it in-Brain password manager.</li>
</ol>

<form onsubmit="return false;" method="post" name="myForm">

    <label>masterpass</label>
    <input type="password" name="masterpass" id="mpass" oninput="encryp()"/> <br>

    <label for="">Service Name</label>
    <input type="text" name="sevice" id="service" oninput="encryp()"/> <br>

    <label for="">password length</label>
    <input type="text" id="length" placeholder=12 list="lengthlist" oninput="encryp()"/>

    <datalist id="lengthlist">
<option value="12">
<option value="16">
<option value="20">
<option value="24">
<option value="30">
    </datalist>

    <input type="submit" name="submit" onclick="init()" />
</form>