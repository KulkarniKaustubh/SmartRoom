import { StatusBar } from 'expo-status-bar'
import React from 'react'
import {
    StyleSheet,
    Text,
    View,
    TextInput,
    TouchableOpacity
} from 'react-native'

export default function App() {

    const [name, setName] = React.useState("")
    const [userJSON, setUserJSON] = React.useState(null)

    function showErrorText() {
        return (
            <Text>User not found.</Text>
        )
    }

    function getAllProperties(json) {
        return (
            <View>
                <Text>{json.name}</Text>
                <Text>Light Color : {json.light_color}</Text>
                <Text>Light:  {json.light_on? 'On' : 'Off'}</Text>
            </View>
        )
    }

    async function getUser(nameEntered) {
      try {
        let response = await fetch(
          'http://620854884fa3.ngrok.io/users'
        )
        let json = await response.json()
        for (let i=0; i < json.length; ++i) {
            if (nameEntered == json[i].name) {
                setUserJSON(json[i])
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

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
    textInput: {
        textAlign: 'center',
        borderColor: 'black',
        borderRadius: 10,
        borderWidth: 1,
        padding: 10
    },
    buttons: {
        margin: 10,
        padding: 10,
        borderColor: 'black',
        borderWidth: 1,
        borderRadius: 10,
        backgroundColor: 'black'
    },
    buttonText: {
        color: 'white'
    }
})
