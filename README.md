# MyIntruder
## What is Intruder?
Intruder is a tool for web applications to enumerate or attack.
## How MyIntruder works?
It sends customized HTTP and HTTPS requests via the python requests library to serve information about response.
## How to use?
I would like to point out that the developer is not responsible for any action you take with the script.
Available tags for now:

"-p" payload wordlist location

"-u" URL

"-r" raw request's text file location
## Example Usage
Before we start, I would like to point out that the developer is not responsible for any action you take with the script, and the IPv4 address specified in the example is not a public address but belongs to a machine created for such tests!

I used the "Brute It" named room on the TryHackMe.
### Step 1: 
We need an HTTP request to send in a raw form.
You can use Burp Suite or your browser's developer tool to intercept the desired request.

![image](https://user-images.githubusercontent.com/91434618/211196245-b182b449-93da-4505-9631-581bf706a287.png)

### Step 2:
We need to mark the location with the "§" sign to specify where to position our payloads in the wordlist.

![image](https://user-images.githubusercontent.com/91434618/211197711-023a7ccf-8625-45fb-8f1f-6d0871c3e09e.jpeg)

Then, I saved the raw request as "text_req.txt".

### Step 3:
I gave the arguments to parameters using tags.

![image](https://user-images.githubusercontent.com/91434618/211198196-f7fa900a-7c78-4bf1-968c-f662c5d39c4b.png)

### Step 4:
Output:

![image](https://user-images.githubusercontent.com/91434618/211198762-5c885444-3f1f-4ce6-beeb-bdfabedbe994.jpeg)

If you want to see the output belong to a specific response length or status code you can change line 24 in "forward.py". It is not a complete project. I will update the project to be more user-friendly.


Fatih Öner
