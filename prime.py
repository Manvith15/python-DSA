from flask import Flask
app= Flask(__name__)

@app.route("/<int:number>")
def prime(number):
    primes=""
    for i in range(2,number+1):
     for n in range(2,i):
        if(i%n==0):
            break

     else:
                    
          primes+=str(i)+","
    return primes

