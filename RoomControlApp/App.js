import { StatusBar } from 'expo-status-bar'
import React from 'react'
import {
    StyleSheet,
    Text,
    View,
    TextInput,
    TouchableOpacity
} from 'react-native'
import styles from './styles.js'

export default function App() {

    const [name, setName] = React.useState("")
    const [userJSON, setUserJSON] = React.useState(null)
    const [userID, setUserID] = React.useState(0)

    function showErrorText() {
        return (
            <Text>User not found.</Text>
        )
    }

    function getAllProperties(json) {
        return (
            <View>
                <Text style={styles.name}>Hey {json.name}!</Text>
                <Text>Light Color : {json.light_color}</Text>
                <Text>Light:  {json.light_on? 'On' : 'Off'}</Text>
            </View>
        )
    }

    async function getUser(nameEntered) {
      try {
        let response = await fetch(
          'https://6c43cf0b82b1.ngrok.io/users',
          {
              method: 'GET'
          }
        )
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
            {userJSON? getAllProperties(userJSON) : showErrorText()}



        </View>
    )
}
