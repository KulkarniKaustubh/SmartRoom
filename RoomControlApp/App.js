import { StatusBar } from 'expo-status-bar'
import React from 'react'
import {
    StyleSheet,
    Text,
    View,
    TextInput,
    TouchableOpacity,
    Keyboard
} from 'react-native'
import styles from './styles.js'

import LightColor from './components/LightColor'
import LightSwitch from './components/LightSwitch'
import API_URL from './Globals'

export default function App() {

    const [name, setName] = React.useState("")
    const [userJSON, setUserJSON] = React.useState(null)
    const [userID, setUserID] = React.useState(0)

    function showErrorText() {
        return (
            <Text>Enter a valid username.</Text>
        )
    }

    function getAllSettings(json) {
        return (
            <View style={styles.settings_container}>
                <Text style={styles.name}>Hey {json.name}!</Text>
                <LightColor lightColor={json.light_color} id={json._id}/>
                <LightSwitch lightOn={json.light_on} id={json._id}/>
            </View>
        )
    }

    async function getUser(nameEntered) {
        Keyboard.dismiss()
        try {
            let response = await fetch(
                API_URL, {
                    method: 'GET'
                })
                let json = await response.json()
                for (let i=0; i < json.length; ++i) {
                    if (nameEntered == json[i].name) {
                        setUserJSON(json[i])
                        setUserID(json[i]._id)
                        break
                    }
                    setUserJSON(null)
                }
            } catch (error) {
                console.error(error)
            }
        }

        return (
            <View style={styles.container}>
                <TextInput
                    style={styles.textInput}
                    placeholder="Enter your name"
                    onChangeText={text => setName(text)}
                    ></TextInput>
                <TouchableOpacity
                    style={styles.buttons}
                    onPress={() => getUser(name)}
                    >
                    <Text style={styles.buttonText}>Get my settings</Text>
                </TouchableOpacity>
                {userJSON? getAllSettings(userJSON) : showErrorText()}

            </View>
        )
}
