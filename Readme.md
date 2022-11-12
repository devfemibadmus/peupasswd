<h1><strong>Peupasswd</strong> Advanced Password Security Software</h1>
<p><a href="https://blackstackhub.github.io/Peupasswd" >Peupasswd</a> is an advanced password security software written in python use in generating unique password for each of each service i.e you can generate special password for each of your social media or services with just one master password; see also <a href="https://github.com/kcubeterm/neupasswd">neupasswd</a></p>
    
    
<h2>How It Works</h2>
<p><a href="https://blackstackhub.github.io/Peupasswd">Peupasswd</a> takes in a master password, the service name you wanna use the password for and the length of the password u want(never worry about the length you can choose as much as possible you dont need to cram it). Then it encrypt the master password in a way you can nerver guess of. Also you can retrieve/check ur password again by doing same way.</p>
    

<h2>How to:-</h2>

## Install through pip
```
pip install peupasswd
```
 
```
from peupasswd import peupasswd
print(peupasswd("master password", "instagram", 12))
```

## Running on web
```
https://blackstackhub.github.io/Peupasswd
```