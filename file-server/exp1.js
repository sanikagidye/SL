const http=require('http'); const fs=require('fs'); const port=9090 
const server=http.createServer(function(req,res){     
    res.writeHead(200,{'content-type':'text/html'})     
    fs.readFile('page.html',function(error,data){         
        if(error){             
            res.write(404)             
            res.write('error:file not found') 
        }else{ 
            res.write(data) 
        } 
        res.end() 
    }) 
}) 
server.listen(port,function(error){         
    if(error){             
        console.log('Something went wrong',error) 
        }         else{             
            console.log('Server is listening on port'+port) 
        } 
    }) 
