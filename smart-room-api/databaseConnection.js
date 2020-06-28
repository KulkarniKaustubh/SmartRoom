const mongoose = require('mongoose')

const URI = 'mongodb+srv://kaustubh:kaustubh@smart-room.tdj0l.mongodb.net/smart-room?retryWrites=true&w=majority'

const connectDB = async () => {
    await mongoose.connect(URI, {
        useUnifiedTopology: true,
        useNewUrlParser: true
    })
    console.log('DB Connected')
}

module.exports = connectDB()
