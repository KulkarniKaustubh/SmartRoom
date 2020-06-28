const mongoose = require('mongoose')

const UserSchema = new mongoose.Schema({
    _id: {
        type: Number,
        required: true,
        unique: true
    },
    name: {
        type: String,
        required: true
    },
    light_color: {
        type: String,
        default: 'white'
    },
    light_on: {
        type: Boolean,
        default: false
    },
    logged_in: {
        type: Boolean,
        default: false,
        required: true
    }
}, { id: false })

module.exports = mongoose.model('User', UserSchema)
