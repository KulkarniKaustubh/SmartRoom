import { StyleSheet } from 'react-native'

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: 'white',
        alignItems: 'center',
        justifyContent: 'center',
    },
    settings_container: {
        alignItems: 'center',
        justifyContent: 'center',
    },
    textInput: {
        textAlign: 'center',
        borderColor: '#f57f17',
        borderRadius: 10,
        padding: 20,
        backgroundColor: '#fff8e1',
        color: '#ff8f00'
    },
    buttons: {
        margin: 20,
        padding: 20,
        borderColor: '#ff8f00',
        borderWidth: 1,
        borderRadius: 10,
        backgroundColor: '#fff8e1'
    },
    buttonText: {
        color: '#ff8f00'
    },
    name: {
        fontSize: 30
    }
})

export default styles
