const express = require('express')
const app = express()
const mongoose = require('mongoose')
const connect = require('./databaseConnection')

connect.connectDB

app.use(express.json())

const usersRouter = require('./routes/smartRoomRoutes')
app.use('/users', usersRouter)

app.listen(8080, () => console.log('Server started ' + mongoose.version))
