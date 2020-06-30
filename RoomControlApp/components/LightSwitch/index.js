import React from 'react'
import {
    Text,
    View,
    TouchableOpacity
} from 'react-native'

import styles from './styles'
import API_URL from '../../Globals'

function LightSwitch({ lightOn, id }) {

    const [switchStatus, setSwitchStatus] = React.useState(lightOn)

    React.useEffect(() => {
      setSwitchStatus(lightOn);
    }, [lightOn])

    function displayLightStatus() {
        return (
            <Text>{switchStatus? "On" : "Off"}</Text>
        )
    }

    async function toggleLight(id) {
        let value = !switchStatus
        setSwitchStatus(!switchStatus)
        try {

            let response = await fetch(
                API_URL + '/' + id, {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    light_on: value
                })
            })
            console.log('Status ' + response.status)

        } catch (err) {
            console.log('Error is ' + err)
        }
    }

    return (
        <View style={styles.container}>
            <Text style={{color: 'grey'}}>Toggle the light switch by tapping on it.</Text>
            <TouchableOpacity
                style={[styles.buttons, (switchStatus)? styles.onButton : styles.offButton]}
                onPress={() => toggleLight(id)}
                >
                {displayLightStatus()}
            </TouchableOpacity>
        </View>
    )
}

export default LightSwitch
