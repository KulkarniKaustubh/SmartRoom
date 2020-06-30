import { StyleSheet } from 'react-native'

const styles = StyleSheet.create({
    container: {
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
    buttons: {
        margin: 20,
        padding: 20,
        borderRadius: 10,
    },
    currentButton: {
        paddingLeft: 80,
        paddingRight: 80
    },
    redButton: {
        backgroundColor: '#ffcdd2',
        borderColor: '#b71c1c',
        borderWidth: 1,
        color: '#b71c1c',
    },
    blueButton: {
        backgroundColor: '#b3e5fc',
        borderColor: '#0d47a1',
        borderWidth: 1,
        color: '#0d47a1',
    },
    greenButton: {
        backgroundColor: '#dcedc8',
        borderColor: '#1b5e20',
        borderWidth: 1,
        color: '#1b5e20'
    },
    buttonsView: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
    },
})

export default styles
