import React from 'react'
import {
    Text,
    View,
    TouchableOpacity
} from 'react-native'

import styles from './styles'
import API_URL from '../../Globals'

function LightColor({ lightColor, id }) {

    const [currentColor, setCurrentColor] = React.useState(lightColor)

    React.useEffect(() => {
      setCurrentColor(lightColor);
    }, [lightColor])

    function displayCurrentColor() {
        return (
            <Text style={[
                    styles.buttons,
                    (currentColor == "red")? styles.redButton :
                    (currentColor == "blue")? styles.blueButton :
                    styles.greenButton,
                    styles.currentButton
                ]}
                >
                {currentColor}
            </Text>
        )
    }

    async function changeToRed(id) {
        setCurrentColor('red')
        try {

            let response = await fetch(
                API_URL + '/' + id, {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    light_color: 'red'
                })
            })
            console.log('Status ' + response.status)

        } catch (err) {
            console.log('Error is ' + err)
        }
    }

    async function changeToBlue(id) {
        setCurrentColor('blue')
        try {

            let response = await fetch(
                API_URL + '/' + id, {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    light_color: 'blue'
                })
            })
            console.log('Status ' + response.status)

        } catch (err) {
            console.log('Error is ' + err)
        }
    }

    async function changeToGreen(id) {
        setCurrentColor('green')
        try {

            let response = await fetch(
                API_URL + '/' + id, {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    light_color: 'green'
                })
            })
            console.log('Status ' + response.status)

        } catch (err) {
            console.log('Error is ' + err)
        }
    }

    return (
        <View style={styles.container}>
            {displayCurrentColor()}
            <Text style={{color: 'grey'}}>Tap on the buttons to change the color of your light.</Text>
            <View style={styles.buttonsView}>
                <TouchableOpacity
                    style={[styles.buttons, styles.redButton]}
                    onPress={() => changeToRed(id)}
                    >
                    <Text style={{color: '#b71c1c'}}>red</Text>
                </TouchableOpacity>
                <TouchableOpacity
                    style={[styles.buttons, styles.greenButton]}
                    onPress={() => changeToGreen(id)}
                    >
                    <Text style={{color: '#1b5e20'}}>green</Text>
                </TouchableOpacity>
                <TouchableOpacity
                    style={[styles.buttons, styles.blueButton]}
                    onPress={() => changeToBlue(id)}
                    >
                    <Text style={{color: '#0d47a1'}}>blue</Text>
                </TouchableOpacity>
            </View>
        </View>
    )
}

export default LightColor
