// const express = require('express');
// const app = express();
// app.get('/',function (req ,res) {
// res.send('hello ata ')
// });
// app.listen(3000,()=>{
// console.log('server is running on port 3000');
// });


// const fs = require('fs');
// fs.readFile('mysite.txt', 'utf8', (err,data)=>{
// if (err){
//     console.log( 'err readingfile :'+err);
//     return;
// }
// else  console.log('file content:' +data );
// });
// console.log('reading file..... (this runs frist)');


// const http = require('http');
// http.createServer((req,res )=>{
// res.writeHead(200,{'Content-type': 'text/plain'});
// res.end('heloo word!');
// }).listen(3000);

// let name = 'node.js';
// const version= 20 ;
// function greet(user) {
//     return `helooo ,${user}!`;   
// }
// const add = (a,b )=>a+b;
// console.log(greet('developer'));
// console.log(add(5,3));
// const user = {
//     name : ' ata ',
//     age :   17,
//     greet (){
//         console.log(`hi , im ${this.name}`);
        
//     }};

// const colors = ['red', ' green ' , ' black'];
// colors.forEach(color=>console.log(color));
// const lengths = colors.map(color=>color.length);


// function fetchData(callback) {
//   setTimeout(() => {
//     callback('Data received!');
//   }, 1000);
// }

// // 2. Promises (ES6+)
// const fetchDataPromise = () => {
//   return new Promise((resolve) => {
//     setTimeout(() => resolve('Promise resolved!'), 1000);
//   });
// };

// // 3. Async/Await (ES8+)
// async function getData() {
//   const result = await fetchDataPromise();
//   console.log(result);
// }

// getData(); // Call the async function
// console.log(`V8 version: ${process.versions.v8}`);




// const fs = require('fs');
// console.log('start of bloocking code ');
// const data = fs.readFileSync('myfile.txt',  'utf8');
// console.log(' bloocking operation completed');


// console.log( 'start of non bloocking code ');
// fs.readFile('myfile.txt', 'utf8', (err,data )=>{
// if (err) throw err;
// console.log('non bloocking operation complated ');
// });
// console.log(' this runs before the file is read ');


// const fs = require('fs');
// console.log('1. Starting sync read...');
// const data = fs.readFileSync('myfile.txt', 'utf8');
// console.log('2. File contents:', data);
// console.log('3. Done reading file');



//  const fs = require('fs');
// console.log('1. Starting async read...');
// fs.readFile('myfile.txt', 'utf8', (err, data) => {
//   if (err) throw err;
//   console.log('2. File contents:', data);
// });
// console.log('3. Done starting read operation');



// const express = require('express');
// const config = require('./config');
// const app = express();
// global.config = require('./config');

// app.use(express.static(__dirname + 'java')); // یا هر پوشه‌ای که داری

// // مسیر اصلی
// app.get('/', (req, res) => {
//   res.send('Welcome to my server!');
// });

// // مسیر با پارامتر username
// app.get('/:username', (req, res) => {
//   console.log(req.params);
//   res.send(`Hello ${req.params.username}`);
// });

// app.listen(config.port, () => {
//   console.log(`server is running on port ${config.port}`);
// });




// const fs = require('fs').promises;
// const promise1 = Promise.resolve('First result');
// const promise2 = new Promise((resolve) => setTimeout(() => resolve('Second result'), 1000));
// const promise3 = fs.readFile('myfile.txt', 'utf8'); // Read local file instead of fetch

// Promise.all([promise1, promise2, promise3])
//   .then(results => {
//     console.log('Results:', results);
//     // results[0] is from promise1
//     // results[1] is from promise2
//     // results[2] is the content of myfile.txt
//   })
//   .catch(error => {
//     console.error('Error in one of the promises:', error);
//   });


// const myPromise= new Promise((resolve,reject)=>{
// const succes = true ;
// if (succes){
//   resolve(' good luck ');
// }
// else{

//   reject('dosent luck')
// }


// }); 
//  myPromise
// .then(result => console.log('Success:', result)) // وقتی موفق شد
//  myPromise.catch(error => console.error('Error:', error)); 


// async function getData() {
//   console.log('Starting...');
//   const result = await someAsyncOperation();
//   console.log(`Result: ${result}`);
//   return result;
// }

// function someAsyncOperation() {
//   return new Promise(resolve => {
//     setTimeout(() => resolve('Operation completed'), 1000);
//   });
// }

// // Call the async function
// getData().then(data => console.log('Final data:', data));







// const fs = require('fs').promises;

// async function loadUserData(userId) {
//   try {
//     const data = await fs.readFile(`users/${userId}.json`, 'utf8');
//     const user = JSON.parse(data);

//     if (!user.email) {
//       throw new Error('Invalid user data: missing email');
//     }

//     return user;
//   } catch (error) {
//     // Handle different error types
//     if (error.code === 'ENOENT') {
//       throw new Error(`User ${userId} not found`);
//     } else if (error instanceof SyntaxError) {
//       throw new Error('Invalid user data format');
//     }
//     // Re-throw other errors
//     throw error;
//   } finally {
//     // Cleanup code that runs whether successful or not
//     console.log(`Finished processing user ${userId}`);
//   }
// }

// // Usage
// (async () => {
//   try {
//     const user = await loadUserData(123);
//     console.log('User loaded:', user);
//   } catch (error) {
//     console.error('Failed to load user:', error.message);
//     // Handle error (e.g., show to user, retry, etc.)
//   }
// })();







// describe('async',function(){...});







