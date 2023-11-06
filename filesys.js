const fs = require("fs"); const path = require("path")

const dirPath = path.join(__dirname, 'test');
const filePath = dirPath + "\\hello.txt";

fs.writeFileSync(filePath, `${filePath} Created !!`);

const data = fs.readFileSync(filePath, 'utf-8'); console.log(data);

const apErr = fs.appendFileSync(filePath, "\nThis is append data")

if (apErr) console.log(apErr);
else console.log("Appended");

const renameErr = fs.renameSync(filePath, dirPath + "\\newtest.txt");
if (renameErr) console.log(renameErr);
else console.log("Renamed");

const delErr = fs.unlinkSync(dirPath + "\\newtest.txt");
if (delErr) console.log(delErr);
else console.log("deleted")
