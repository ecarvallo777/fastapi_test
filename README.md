## fastapi-Id-and-Patent-generator.
# Simple two endpoints that generates:

> **An Id** based on an Patent typed by the user. i,e:  
> input: AAAA000  
> **output:** 1  
>   
> **An Patent** based on an Id typed by the user. i,e:  
> input: 456976000  
> **output:** ZZZZ999  

# How to run?

You need to run the image builded by docker with this command:  
    
    docker run -d -p 80:80 imageName

So, in your browser, use the endpoints to send your querys. 
    
    Endpoints:
        localhost/get_id/
        localhost/get_patent/

If you need to generate an ID based on a Patent:  

    Type:
        localhost/get_id/ABCD987
        
        this return: {"ABCD987":731988}

If you need to generate an Patent based on an Id:

    Type:
        localhost/get_patent/731988
        
        this return: {"731988":"ABCD987"}

    
