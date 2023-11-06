var express = require('express');
var app=express();
var PORT=9000;
var router1=express.Router();
var router2=express.Router();
var router3=express.Router();

router1.get('/',function(req,res,next){
    console.log("User Router Working");
    res.send("This is my home page");
})

router1.get('/admin',function(req,res,next){
    console.log("Admin Router Working");
    res.send("This is my admin page");
})

router1.get('/student',function(req,res,next){
    console.log("Student Router Working");
    res.send("This is my student page");
})
