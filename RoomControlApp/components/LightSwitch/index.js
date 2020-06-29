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

    function displayLightStatus() {
        return (
            <Text>Light switch {switchStatus? "On" : "Off"}</Text>
        )
    }

    return (
        <View style={styles.container}>
            {displayLightStatus()}
        </View>
    )
}

export default LightSwitch
