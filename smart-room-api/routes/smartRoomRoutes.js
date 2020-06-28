const express = require('express')
const router = express.Router()
const User = require('../models/smartRoomModel')

//Getting all
router.get('/', async (req, res) => {
    try {
        const users = await User.find()
        res.json(users)
    } catch (err) {
        //500 error code means it was our fault and not the person using our API
        res.status(500).json({ message: err.message })
    }
})

//Getting one
router.get('/:id', getUserById, async (req, res) => {
    res.send(res.user)
})

//Creating one
router.post('/', async (req, res) => {
    const user = new User({
        _id: req.body._id,
        name: req.body.name,
        light_color: req.body.light_color,
        light_on: req.body.light_on,
        logged_in: req.body.logged_in
    })
    try {
        const newUser = await user.save()
        //201 is successful creation instead of 200. Better practice/
        res.status(201).json(newUser)
    } catch (err) {
        //400 is for user's fault. Nothing wrong with our server. They may have given wrong data
        res.status(400).json({ message: err.message })
    }

})

//Updating one
router.patch('/:id', getUserById, async (req, res) => {
    if (req.body.name != null) {
        res.user.name = req.body.name
    }
    if (req.body.light_color != null) {
        res.user.light_color = req.body.light_color
    }
    if (req.body.light_on != null) {
        res.user.light_on = req.body.light_on
    }
    try {
        const updatedUser = await res.user.save()
        res.json({ message: 'Updated subscriber' })
    } catch (err) {
        res.status(400).json({ message: err.message })
    }
})

//Deleting one
router.delete('/:id', getUserById, async (req, res) => {
    try {
        await res.user.remove()
        res.json({ message: 'Deleted user' })
    } catch (err) {
        res.status(500).json({ message: err.message })
    }
})

async function getUserById(req, res, next) {
    let user
    try {
        user = await User.findById(req.params.id)
        if (user == null) {
            return res.status(404).json({ message: 'Cannot find user' })
        }
    } catch (err) {
        return res.status(500).json({ message: err.message })
    }

    res.user = user
    next()
}

module.exports = router
